#!/usr/bin/env python3
from pathlib import Path
import importlib.util
import json
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('renderer', ROOT / 'palette/render.py')
renderer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(renderer)


class Palette(unittest.TestCase):
    def setUp(self):
        self.palette = json.loads((ROOT / 'palette/default.json').read_text())
        self.material = json.loads((ROOT / 'palette/material.json').read_text())

    def test_shared_material_and_role_changes_reach_chrome_and_internal_pages(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder)
            renderer.render(self.palette, self.material, output)
            roles = (output / 'anto426/roles.css').read_text()
            self.assertIn('--anto-accent: ' + self.palette['accent'], roles)
            self.assertIn('--anto-radius-control: 12px', roles)
            self.assertIn('--anto-ui-panel:', roles)
            self.assertIn(', 0.46)', roles)
            self.assertNotIn('{{', roles)
            self.palette['accent'] = '#66aacc'
            self.material['material']['opacity'] = .37
            self.material['radius']['control'] = 14
            renderer.render(self.palette, self.material, output)
            for name in ('roles', 'content'):
                text = (output / f'anto426/{name}.css').read_text()
                self.assertIn('--anto-accent: #66aacc', text)
                self.assertIn('--anto-radius-control: 14px', text)
                self.assertIn(', 0.37)', text)

    def test_ordinary_websites_are_not_targeted(self):
        with tempfile.TemporaryDirectory() as folder:
            renderer.render(self.palette, self.material, Path(folder))
            content = (Path(folder) / 'anto426/content.css').read_text()
            self.assertIn('@-moz-document', content)
            self.assertNotIn('url-prefix("http', content)
            self.assertNotIn('url-prefix("about:")', content)
            self.assertTrue(content.index(':root {') > content.index('@-moz-document'))

    def test_invalid_inputs_do_not_create_partial_themes(self):
        for opacity in (True, 0, -1, 2):
            with tempfile.TemporaryDirectory() as folder:
                self.material['material']['opacity'] = opacity
                with self.assertRaises(ValueError):
                    renderer.render(self.palette, self.material, Path(folder) / 'output')
                self.assertFalse((Path(folder) / 'output').exists())


if __name__ == '__main__':
    unittest.main()
