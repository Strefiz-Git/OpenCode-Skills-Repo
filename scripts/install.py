#!/usr/bin/env python3
"""Instala skills deste repo num projeto (ou globalmente) para o OpenCode as encontrar.

Exemplos:
  python scripts/install.py auto-commit planning            # skills por nome -> ./.opencode/skills/
  python scripts/install.py --category minecraft            # uma categoria inteira
  python scripts/install.py --bundle all-generic            # um bundle de bundles/*.txt
  python scripts/install.py --bundle all --target ../meu-projeto
  python scripts/install.py --global planning               # ~/.config/opencode/skills/
  python scripts/install.py --list                          # lista nomes e categorias

Copia a pasta da skill (SKILL.md + scripts/references). Não apaga nada; usa --force para substituir.
"""
import os, sys, shutil, glob, argparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
avail = {os.path.basename(os.path.dirname(p)): os.path.dirname(p)
         for p in glob.glob(os.path.join(ROOT, 'skills', '*', '*', 'SKILL.md'))}

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument('names', nargs='*')
ap.add_argument('--category'); ap.add_argument('--bundle')
ap.add_argument('--target', default='.', help='raiz do projeto (por omissão: pasta atual)')
ap.add_argument('--global', dest='glob', action='store_true', help='instalar em ~/.config/opencode/skills')
ap.add_argument('--force', action='store_true'); ap.add_argument('--list', action='store_true')
a = ap.parse_args()

if a.list:
    for n, p in sorted(avail.items(), key=lambda x: (x[1], x[0])):
        print(f'{os.path.basename(os.path.dirname(p)):16} {n}')
    sys.exit(0)

want = list(a.names)
if a.category: want += [n for n, p in avail.items() if os.path.basename(os.path.dirname(p)) == a.category]
if a.bundle:
    f = os.path.join(ROOT, 'bundles', a.bundle + '.txt')
    if not os.path.exists(f): sys.exit(f'bundle desconhecido: {a.bundle}')
    want += [l.split('#')[0].strip() for l in open(f, encoding='utf-8') if l.split('#')[0].strip()]
if not want: sys.exit('nada para instalar (usa nomes, --category ou --bundle; --list para ver tudo)')

dest_root = os.path.join(os.path.expanduser('~'), '.config', 'opencode', 'skills') if a.glob \
    else os.path.join(os.path.abspath(a.target), '.opencode', 'skills')
os.makedirs(dest_root, exist_ok=True)
done = skipped = 0
for n in dict.fromkeys(want):
    if n not in avail: print(f'! skill desconhecida: {n}'); continue
    d = os.path.join(dest_root, n)
    if os.path.exists(d):
        if not a.force: print(f'- {n}: já existe (usa --force)'); skipped += 1; continue
        shutil.rmtree(d)
    shutil.copytree(avail[n], d, ignore=shutil.ignore_patterns('__pycache__'))
    print(f'+ {n}'); done += 1
print(f'{done} instalada(s), {skipped} ignorada(s) em {dest_root}')
