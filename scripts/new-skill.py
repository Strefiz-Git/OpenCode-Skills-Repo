#!/usr/bin/env python3
"""Cria uma skill nova a partir de templates/skill/SKILL.md.

    python scripts/new-skill.py <categoria> <nome-da-skill> "<descrição numa linha>"

Cria skills/<categoria>/<nome-da-skill>/SKILL.md; depois preenche-a e corre
validate.py e build-catalog.py.
"""
import os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if len(sys.argv) != 4: sys.exit(__doc__)
cat, name, desc = sys.argv[1:]
rx = r'^[a-z0-9]+(-[a-z0-9]+)*$'
if not re.match(rx, name) or len(name) > 64: sys.exit('nome da skill: minúsculas, dígitos, hífenes simples, máx. 64 carateres')
if not re.match(rx, cat): sys.exit('categoria: minúsculas, dígitos, hífenes')
d = os.path.join(ROOT, 'skills', cat, name)
if os.path.exists(d): sys.exit(f'{d} já existe')
t = open(os.path.join(ROOT, 'templates', 'skill', 'SKILL.md'), encoding='utf-8').read()
t = t.replace('{{NAME}}', name).replace('{{CATEGORY}}', cat).replace('{{DESCRIPTION}}', desc.replace('\\', '\\\\').replace('"', '\\"'))
os.makedirs(d)
open(os.path.join(d, 'SKILL.md'), 'w', encoding='utf-8', newline='\n').write(t)
print(f'criada {os.path.relpath(d, ROOT)}/SKILL.md - preenche-a e corre validate.py e build-catalog.py')
