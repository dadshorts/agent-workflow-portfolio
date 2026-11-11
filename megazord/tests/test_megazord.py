"""Offline unit tests. No CLI/model invocation; all process calls are mocked."""
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

spec = importlib.util.spec_from_file_location('megazord', Path(__file__).resolve().parents[1] / 'scripts' / 'megazord.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class WorkflowTests(unittest.TestCase):
    def test_complete_requires_all_three(self):
        with tempfile.TemporaryDirectory() as d:
            report = m.orchestrate('synthetic', Path(d), lambda *a: m.result(True, 'fixture'))
            self.assertTrue(report['ok'])
            self.assertEqual(report['status'], 'complete')
            self.assertTrue((Path(d) / 'synthesis.md').exists())

    def test_failed_synthesis_is_partial(self):
        with tempfile.TemporaryDirectory() as d:
            def invoke(p, prompt, stage):
                return m.result(error='fixture failure') if stage == 'synthesis' else m.result(True, 'fixture')
            report = m.orchestrate('synthetic', Path(d), invoke)
            self.assertFalse(report['ok'])
            self.assertEqual(report['status'], 'partial')

    def test_single_review_failure_is_disclosed(self):
        seen = []
        with tempfile.TemporaryDirectory() as d:
            def invoke(p, prompt, stage):
                seen.append((stage, prompt))
                return m.result(error='fixture failure') if stage == 'codex' else m.result(True, 'fixture')
            report = m.orchestrate('synthetic', Path(d), invoke)
            self.assertEqual(report['status'], 'partial')
            self.assertIn('[UNAVAILABLE]', dict(seen)['synthesis'])
            self.assertEqual(dict(seen)['grok'], dict(seen)['codex'])

    def test_both_fail_skips_synthesis(self):
        seen = []
        with tempfile.TemporaryDirectory() as d:
            def invoke(p, prompt, stage):
                seen.append(stage)
                return m.result(error='fixture failure')
            self.assertEqual(m.orchestrate('synthetic', Path(d), invoke)['status'], 'failed')
            self.assertNotIn('synthesis', seen)

    def test_lock_refuses_and_releases(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            with m.singleton(root):
                with self.assertRaises(RuntimeError):
                    with m.singleton(root):
                        pass
            self.assertFalse((root / '.megazord.lock').exists())

    def test_lock_releases_on_exception(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                with m.singleton(Path(d)):
                    raise ValueError('fixture')
            self.assertFalse((Path(d) / '.megazord.lock').exists())

    def test_recursion_refuses_before_io(self):
        with patch.dict(os.environ, {'MEGAZORD_ACTIVE': '1'}), patch.object(m, 'process') as process, redirect_stdout(io.StringIO()):
            self.assertEqual(m.main(['--demo']), 3)
            process.assert_not_called()

    def test_environment_is_allowlisted(self):
        with patch.dict(os.environ, {'PATH': 'fixture', 'FAKE_API_KEY': 'synthetic', 'CUSTOM_TOKEN': 'synthetic'}, clear=True):
            self.assertEqual(m.child_env(), {'PATH': 'fixture', 'MEGAZORD_ACTIVE': '1'})

    def test_preflight_fails_closed(self):
        with patch.object(m, 'process', return_value=subprocess.CompletedProcess([], 0, '--help', '')):
            with self.assertRaises(ValueError):
                m.preflight('fixture', 'grok', Path('.'))

    def test_bad_json_and_empty_text_fail(self):
        for stdout in ('not-json', '{}', '[]', '{"text":""}', '{"text":123}', '{"type":"error","text":"ignored"}'):
            with self.subTest(stdout=stdout), tempfile.TemporaryDirectory() as d:
                with patch.object(m, 'process', return_value=subprocess.CompletedProcess([], 0, stdout, '')):
                    self.assertFalse(m.call_cli('grok', 'fixture', 'synthetic', Path(d) / 'stage', 1)['ok'])

    def test_nonzero_exit_discards_output(self):
        with tempfile.TemporaryDirectory() as d, patch.object(m, 'process', return_value=subprocess.CompletedProcess([], 1, '{"text":"fixture"}', 'diagnostic')):
            r = m.call_cli('grok', 'fixture', 'synthetic', Path(d) / 'stage', 1)
            self.assertFalse(r['ok'])
            self.assertEqual(r['output'], '')

    def test_timeout_is_failure(self):
        with tempfile.TemporaryDirectory() as d, patch.object(m, 'process', side_effect=subprocess.TimeoutExpired('fixture', 1)):
            r = m.call_cli('grok', 'fixture', 'synthetic', Path(d) / 'stage', 1)
            self.assertFalse(r['ok'])
            self.assertIn('timed out', r['error'])

    def test_codex_contract_is_read_only(self):
        with tempfile.TemporaryDirectory() as d:
            def process(cmd, cwd, timeout, text=None):
                self.assertEqual(cmd[cmd.index('--sandbox') + 1], 'read-only')
                self.assertEqual(cmd[-1], '-')
                Path(cmd[cmd.index('--output-last-message') + 1]).write_text('fixture', encoding='utf-8')
                return subprocess.CompletedProcess(cmd, 0, '', '')
            with patch.object(m, 'process', side_effect=process):
                self.assertTrue(m.call_cli('codex', 'fixture', 'synthetic', Path(d) / 'stage', 1)['ok'])

    def test_demo_never_starts_process(self):
        with tempfile.TemporaryDirectory() as d, patch.dict(os.environ, {}, clear=True), patch.object(m, 'process') as process, redirect_stdout(io.StringIO()) as output:
            self.assertEqual(m.main(['--demo', '--output-dir', d]), 0)
            process.assert_not_called()
            report = json.loads(output.getvalue())
            self.assertEqual(report['mode'], 'synthetic-fixture-demo')
            self.assertTrue(report['ok'])
            self.assertTrue((Path(report['run_dir']) / 'meta.json').exists())


if __name__ == '__main__':
    unittest.main()
