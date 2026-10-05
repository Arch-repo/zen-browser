#!/usr/bin/env python3
"""Render Zen chrome and internal pages from the shared desktop material."""
from pathlib import Path
import argparse
import colorsys
import json
import re

ROOT = Path(__file__).resolve().parent


def render(palette, material, output):
    for role, value in palette.items():
        if not isinstance(value, str) or not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
            raise ValueError('Invalid palette role: ' + role)
    def color(expression):
        expression = expression.strip()
        if expression.startswith('@'):
            value = palette[expression[1:].replace('-', '_')]
            return tuple(int(value[i:i + 2], 16) / 255 for i in (1, 3, 5)) + (1.,)
        match = re.fullmatch(r'(alpha|mix|shade)\((.*)\)', expression)
        if not match:
            raise ValueError('Invalid material expression: ' + expression)
        name, body = match.groups()
        arguments, start, depth = [], 0, 0
        for index, char in enumerate(body):
            depth += (char == '(') - (char == ')')
            if char == ',' and depth == 0:
                arguments.append(body[start:index]); start = index + 1
        arguments.append(body[start:])
        if len(arguments) != (3 if name == 'mix' else 2):
            raise ValueError('Invalid material arguments')
        first, amount = color(arguments[0]), float(arguments[-1])
        if not 0 <= amount <= 1:
            raise ValueError('Invalid color amount')
        if name == 'alpha':
            return first[:3] + (first[3] * amount,)
        if name == 'mix':
            second = color(arguments[1])
            return tuple(a * (1 - amount) + b * amount for a, b in zip(first, second))
        hue, light, saturation = colorsys.rgb_to_hls(*first[:3])
        return colorsys.hls_to_rgb(hue, light * amount, saturation * amount) + (first[3],)
    opacity = material['material']['opacity']
    if type(opacity) not in (int, float) or not 0 < opacity <= 1:
        raise ValueError('Invalid material opacity')
    values = dict(palette, opacity=f'{opacity:g}')
    values.setdefault('popover', palette['surface'])
    declarations = []
    for name, expression in material['colour'].items():
        channels = color(expression.replace('{{material.opacity}}', str(opacity)))
        css = 'rgba(' + ', '.join(str(round(v * 255)) for v in channels[:3]) + f', {channels[3]:.6g})'
        declarations.append(f'  --anto-{name}: {css} !important;')
    for group in ('radius', 'spacing', 'control'):
        for name, value in material[group].items():
            if type(value) not in (int, float) or not 0 < value <= 1024:
                raise ValueError('Invalid material measure: ' + name)
            declarations.append(f'  --anto-{group}-{name.replace("_", "-")}: {value:g}px !important;')
    values['shared_tokens'] = '\n'.join(declarations)
    def substitute(text):
        return re.sub(r'\{\{(\w+)\}\}', lambda match: values[match[1]], text)
    output.mkdir(parents=True, exist_ok=True)
    managed = output / 'anto426'
    managed.mkdir(exist_ok=True)
    roles = substitute((ROOT / 'roles.css.in').read_text())
    (managed / 'roles.css').write_text(roles)
    for name in ('chrome', 'tabs', 'popups'):
        (managed / (name + '.css')).write_text(substitute((ROOT / (name + '.css.in')).read_text()))
    content = substitute((ROOT / 'content.css.in').read_text()).replace('/* SHARED_ROLES */', roles)
    (managed / 'content.css').write_text(content)
    for kind, name in (('Chrome', 'chrome'), ('Content', 'content')):
        (output / ('user' + kind + '.css')).write_text(f'/* Anto426 Monet: managed import */\n@import url("anto426/{name}.css");\n')
    (output / 'theme.json').write_text(json.dumps({'name': 'Anto426 Monet', 'version': '1.0.0', 'zen': '1.23b', 'gecko': '157.0', 'opacity': opacity}, indent=2) + '\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--palette', type=Path, required=True)
    parser.add_argument('--material', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    render(json.loads(args.palette.read_text()), json.loads(args.material.read_text()), args.output)


if __name__ == '__main__':
    main()
