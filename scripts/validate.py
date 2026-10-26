#!/usr/bin/env python3
"""Valida todas as skills, bundles e ficheiros de texto deste repositório.

Verificações (código de saída 1 se houver erros):
  * cada skills/<categoria>/<nome>/SKILL.md tem frontmatter YAML válido;
  * `name` == nome da pasta e cumpre ^[a-z0-9]+(-[a-z0-9]+)*$ (máx. 64 carateres);
  * `description` tem 1-1024 carateres;
  * metadados obrigatórios (category, source, language, scope) existem e category == pasta;
  * nomes de skills únicos entre categorias (os instaladores aplanam as pastas);
  * cada bundle só lista skills existentes;
  * sem segredos óbvios, sem BOM e sem mojibake nos ficheiros de texto.

Uso:  python scripts/validate.py [--quiet]
Requer: Python 3.8+ e PyYAML (pip install pyyaml).
"""
import os, re, sys, glob
try:
    import yaml
except ImportError:
    sys.exit("É preciso PyYAML: pip install pyyaml")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME_RE = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
SECRET_RES = [re.compile(p) for p in (
    r'ghp_[A-Za-z0-9]{36,}', r'github_pat_[A-Za-z0-9_]{50,}', r'AKIA[0-9A-Z]{16}',
    r'-----BEGIN [A-Z ]*PRIVATE KEY-----', r'xox[baprs]-[A-Za-z0-9-]{20,}',
    r'[MN][A-Za-z0-9]{23}\.[A-Za-z0-9_-]{6}\.[A-Za-z0-9_-]{27,}')]
# ficheiros que contêm padrões de deteção de segredos de propósito
SECRET_ALLOW = ('plugins/', 'templates/project-kit/scripts/', 'skills/git-release/', 'archive/', 'scripts/validate.py')
TEXT_EXT = ('.md', '.js', '.json', '.sh', '.ps1', '.py', '.txt', '.yml', '.yaml')
errors = []

def err(msg): errors.append(msg)

def frontmatter(path):
    t = open(path, encoding='utf-8').read().replace('\r\n', '\n')
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    return yaml.safe_load(m.group(1)) if m else None

names = {}
for p in sorted(glob.glob(os.path.join(ROOT, 'skills', '*', '*', 'SKILL.md'))):
    rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
    cat, name = rel.split('/')[1], rel.split('/')[2]
    try:
        fm = frontmatter(p)
    except Exception as e:
        err(f'{rel}: frontmatter YAML inválido ({e})'); continue
    if not isinstance(fm, dict): err(f'{rel}: frontmatter em falta'); continue
    if fm.get('name') != name: err(f'{rel}: name {fm.get("name")!r} != pasta {name!r}')
    if not NAME_RE.match(name) or len(name) > 64: err(f'{rel}: nome de skill inválido')
    d = fm.get('description')
    if not isinstance(d, str) or not 1 <= len(d) <= 1024: err(f'{rel}: description deve ter 1-1024 carateres')
    md = fm.get('metadata') or {}
    for k in ('category', 'source', 'language', 'scope'):
        if k not in md: err(f'{rel}: metadata.{k} em falta')
    if md.get('category') != cat: err(f'{rel}: metadata.category {md.get("category")!r} != pasta {cat!r}')
    if md.get('scope') not in ('generic', 'project-specific'): err(f'{rel}: metadata.scope tem de ser generic|project-specific')
    if name in names: err(f'{rel}: nome de skill duplicado (também em {names[name]})')
    names[name] = rel

for b in sorted(glob.glob(os.path.join(ROOT, 'bundles', '*.txt'))):
    for i, line in enumerate(open(b, encoding='utf-8'), 1):
        s = line.split('#')[0].strip()
        if s and s not in names: err(f'bundles/{os.path.basename(b)}:{i}: skill desconhecida {s!r}')

for dirpath, dirs, files in os.walk(ROOT):
    dirs[:] = [d for d in dirs if d not in ('.git', 'node_modules', '__pycache__')]
    for f in files:
        if not f.endswith(TEXT_EXT): continue
        p = os.path.join(dirpath, f); rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
        raw = open(p, 'rb').read()
        try: t = raw.decode('utf-8')
        except UnicodeDecodeError: err(f'{rel}: UTF-8 inválido'); continue
        if rel.startswith('archive/') or rel == 'scripts/validate.py': continue
        if raw.startswith(b'\xef\xbb\xbf'): err(f'{rel}: tem BOM (usar UTF-8 sem BOM)')
        if '\ufffd' in t or '\u00e2\u20ac' in t or '\u00c3\u00a7' in t or '\u00c3\u00a3' in t: err(f'{rel}: parece mojibake')
        if not rel.startswith(SECRET_ALLOW):
            for r in SECRET_RES:
                if r.search(t): err(f'{rel}: possível segredo ({r.pattern[:20]}...)')

if '--quiet' not in sys.argv:
    print(f'{len(names)} skills verificadas')
for e in errors: print('ERRO   ', e)
print('OK' if not errors else f'{len(errors)} erro(s)')
sys.exit(1 if errors else 0)
