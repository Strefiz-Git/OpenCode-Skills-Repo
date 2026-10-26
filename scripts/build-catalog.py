#!/usr/bin/env python3
"""Gera CATALOG.md, skills/<categoria>/README.md, catalog.json e os bundles gerados.

Corre depois de adicionares ou editares uma skill:   python scripts/build-catalog.py
Verificação para CI (falha se os ficheiros gerados estiverem desatualizados):   python scripts/build-catalog.py --check
Requer: Python 3.8+ e PyYAML.
"""
import os, re, sys, json, glob
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHECK = '--check' in sys.argv

CATEGORY_INFO = {
 'workflow':        ('Workflow', 'Como um agente planeia, decide, regista o progresso e passa uma sessão a quem vem a seguir.'),
 'engineering':     ('Engineering', 'Depuração, revisão, segurança, estrutura, reutilização, documentação e verificação.'),
 'git-release':     ('Git e release', 'Commits, pushes, fluxo GitHub, deploy e checklists de release.'),
 'design':          ('Design', 'Design de interfaces e estilo visual.'),
 'desktop-windows': ('Windows desktop', 'WinForms e pequenos executáveis Windows autónomos.'),
 'minecraft':       ('Minecraft', 'Mods Fabric: setup, mixins, portar entre versões, rede, HUD, builds, performance.'),
 'discord':         ('Discord', 'Bots de Discord: arquitetura de bot de música e templates de servidor.'),
 'web':             ('Web', 'Flask/Socket.IO, front-end e sites de conversão.'),
 'database':        ('Bases de dados', 'Esquemas e persistência para apps e bots.'),
 'python':          ('Python', 'Ferramentas e scripts Python.'),
 'cross-language':  ('Cross-language', 'Manter várias implementações idênticas.'),
 'mobile':          ('Mobile', 'Apps Android / Kotlin / Compose.'),
 'c-cpp':           ('C / C++', 'Pequenos programas nativos e builds.'),
 'devops':          ('DevOps', 'Correr software como serviço e operá-lo.'),
 'integrations':    ('Integrações', 'Pesquisar e ligar APIs de terceiros.'),
 'godot':           ('Godot', 'Jogos Godot 4: consola de debug, Steam e multiplayer.'),
 'data-telemetry':  ('Dados e telemetria', 'Painéis de telemetria e interpretação de dados de jogos.'),
}

def read_fm(p):
    t = open(p, encoding='utf-8').read().replace('\r\n', '\n')
    return yaml.safe_load(re.match(r'^---\n(.*?)\n---\n', t, re.S).group(1))

def norm_source(src):
    if isinstance(src, list): return ', '.join(map(str, src))
    if isinstance(src, str) and src.startswith('['):
        try: return ', '.join(json.loads(src))
        except Exception: pass
    return str(src)

skills = []
for p in sorted(glob.glob(os.path.join(ROOT, 'skills', '*', '*', 'SKILL.md'))):
    fm = read_fm(p); md = fm.get('metadata') or {}
    skills.append(dict(name=fm['name'], category=md.get('category'), description=fm['description'],
                       source=norm_source(md.get('source', '')), origin=md.get('origin', 'imported'),
                       language=md.get('language', ''), scope=md.get('scope', ''), license=fm.get('license', ''),
                       path=os.path.relpath(os.path.dirname(p), ROOT).replace(os.sep, '/')))

def short(d, n=150):
    d = d.replace('|', '\\|').replace('\n', ' ')
    return d if len(d) <= n else d[:n].rsplit(' ', 1)[0] + '…'

outputs = {}
cats = [c for c in CATEGORY_INFO if any(s['category'] == c for s in skills)]
cats += sorted({s['category'] for s in skills} - set(cats))

L = ['# Catálogo', '', '> Gerado por `python scripts/build-catalog.py` — não editar à mão.', '',
     f'**{len(skills)} skills** em {len(cats)} categorias '
     f'({sum(s["scope"]=="generic" for s in skills)} genéricas, {sum(s["scope"]=="project-specific" for s in skills)} exemplos específicos de projeto).', '',
     'Legenda — **origem**: `imported` = copiada de um repo do autor (corpo inalterado), `derived` = escrita para este repo a partir do que os projetos fazem. '
     '**âmbito**: `generic` = reutilizável em qualquer projeto do domínio, `project-specific` = exemplo trabalhado ligado a um projeto. **lang** = língua do texto da skill.', '']
for c in cats:
    title, purpose = CATEGORY_INFO.get(c, (c, ''))
    L += [f'## {title}', '', purpose, '', '| Skill | O que faz | Origem | Âmbito | Lang | Fonte |', '|---|---|---|---|---|---|']
    for s in [x for x in skills if x['category'] == c]:
        L.append(f'| [`{s["name"]}`]({s["path"]}/SKILL.md) | {short(s["description"])} | {s["origin"]} | {s["scope"]} | {s["language"]} | {s["source"]} |')
    L.append('')
outputs['CATALOG.md'] = '\n'.join(L)

for c in cats:
    title, purpose = CATEGORY_INFO.get(c, (c, ''))
    L = [f'# {title}', '', purpose, '', '> Gerado por `python scripts/build-catalog.py`.', '', '| Skill | Usar quando |', '|---|---|']
    for s in [x for x in skills if x['category'] == c]:
        L.append(f'| [`{s["name"]}`]({s["name"]}/SKILL.md) | {short(s["description"], 220)} |')
    L.append('')
    outputs[f'skills/{c}/README.md'] = '\n'.join(L)

by = {}
for s in skills:
    for r in [x.strip() for x in s['source'].split(',') if x.strip()]: by.setdefault(r, []).append(s['name'])
O = ['# Origem das skills', '', 'Gerado por `python scripts/build-catalog.py` a partir de `metadata.source`; não editar à mão.', '',
     '| Repositório | Skills |', '|---|---|']
for r in sorted(by): O.append(f"| [{r}](https://github.com/Strefiz-Git/{r}) | " + ', '.join(f'`{n}`' for n in sorted(by[r])) + ' |')
O += ['', '## Repos analisados sem skills do OpenCode', '',
      'AFK-BOT--NO-MODS-, Auto-key-presser, ChestTracker_Update, Craftify-NeoForge, Create-Bigger-Storage-NeoForge, Organize-Clips, Uni-1ano, journeymap-webmap, programing_repo. Não têm `SKILL.md`; quando ganharem, voltar a correr a extração.', '',
      '## Variantes arquivadas', '', 'Em `archive/<repo>/<skill>/` ficam versões antigas ou quase duplicadas de skills que já existem no catálogo com outra origem (ver `archive/README.md`).', '']
outputs['docs/ORIGEM.md'] = '\n'.join(O)

outputs['catalog.json'] = json.dumps(skills, indent=1, ensure_ascii=False) + '\n'
gen = lambda names, title: f'# {title}\n# Gerado por scripts/build-catalog.py - não editar.\n' + '\n'.join(sorted(names)) + '\n'
outputs['bundles/all-generic.txt'] = gen([s['name'] for s in skills if s['scope'] == 'generic'], 'Todas as skills genéricas')
outputs['bundles/all.txt'] = gen([s['name'] for s in skills], 'Todas as skills, incluindo exemplos específicos de projeto')
for c in cats:
    outputs[f'bundles/cat-{c}.txt'] = gen([s['name'] for s in skills if s['category'] == c], f'Categoria: {c}')

stale = []
for rel, content in outputs.items():
    p = os.path.join(ROOT, rel)
    if CHECK:
        if not os.path.exists(p) or open(p, encoding='utf-8').read() != content: stale.append(rel)
    else:
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8', newline='\n').write(content)
if CHECK:
    if stale: print('Ficheiros gerados desatualizados:', *stale, sep='\n  '); sys.exit(1)
    print('catálogo atualizado')
else:
    print(f'{len(skills)} skills, {len(cats)} categorias -> {len(outputs)} ficheiros escritos')
