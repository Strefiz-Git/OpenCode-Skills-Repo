# OpenCode-Skills-Repo

Biblioteca central de **skills, plugins, comandos e agentes do OpenCode** extraídos dos projetos de [Strefiz-Git](https://github.com/Strefiz-Git). Qualquer projeto novo vai buscar aqui o que precisa em vez de reescrever as mesmas instruções.

- **104 skills** em 17 categorias (86 genéricas, 18 exemplos específicos de projeto) - ver [CATALOG.md](CATALOG.md).
- **2 plugins**, **21 comandos** e **2 agentes** em `plugins/`, `commands/`, `agents/`.
- Um **kit de projeto** pronto a copiar (`templates/project-kit/`): AGENTS.md, opencode.json, scripts e documentos de gestão.
- Scripts para **validar**, **gerar o catálogo** e **instalar** skills.

## Categorias

| Categoria | Skills | Para quê |
|---|---|---|
| [Workflow](skills/workflow/README.md) | 16 | Como um agente planeia, decide, regista o progresso e passa uma sessão a quem vem a seguir. |
| [Engineering](skills/engineering/README.md) | 18 | Depuração, revisão, segurança, estrutura, reutilização, documentação e verificação. |
| [Git e release](skills/git-release/README.md) | 11 | Commits, pushes, fluxo GitHub, deploy e checklists de release. |
| [Design](skills/design/README.md) | 2 | Design de interfaces e estilo visual. |
| [Windows desktop](skills/desktop-windows/README.md) | 2 | WinForms e pequenos executáveis Windows autónomos. |
| [Minecraft](skills/minecraft/README.md) | 22 | Mods Fabric: setup, mixins, portar entre versões, rede, HUD, builds, performance. |
| [Discord](skills/discord/README.md) | 2 | Bots de Discord: arquitetura de bot de música e templates de servidor. |
| [Web](skills/web/README.md) | 4 | Flask/Socket.IO, front-end e sites de conversão. |
| [Bases de dados](skills/database/README.md) | 1 | Esquemas e persistência para apps e bots. |
| [Python](skills/python/README.md) | 1 | Ferramentas e scripts Python. |
| [Cross-language](skills/cross-language/README.md) | 1 | Manter várias implementações idênticas. |
| [Mobile](skills/mobile/README.md) | 17 | Apps Android / Kotlin / Compose. |
| [C / C++](skills/c-cpp/README.md) | 1 | Pequenos programas nativos e builds. |
| [DevOps](skills/devops/README.md) | 1 | Correr software como serviço e operá-lo. |
| [Integrações](skills/integrations/README.md) | 2 | Pesquisar e ligar APIs de terceiros. |
| [Godot](skills/godot/README.md) | 2 | Jogos Godot 4: consola de debug, Steam e multiplayer. |
| [Dados e telemetria](skills/data-telemetry/README.md) | 1 | Painéis de telemetria e interpretação de dados de jogos. |

## Como usar

Cada skill é uma pasta com um `SKILL.md` (frontmatter YAML + instruções) e, por vezes, `scripts/` e `references/`. O OpenCode procura skills em `.opencode/skills/<nome>/SKILL.md` (projeto) ou `~/.config/opencode/skills/<nome>/` (global).

### Instalar com o script (recomendado)

```bash
git clone https://github.com/Strefiz-Git/OpenCode-Skills-Repo.git
cd OpenCode-Skills-Repo
pip install pyyaml                      # só para validate/build-catalog

python scripts/install.py --list                                  # ver tudo
python scripts/install.py planning auto-commit --target ../meu-projeto
python scripts/install.py --category minecraft --target ../meu-mod
python scripts/install.py --bundle all-generic --target ../meu-projeto
python scripts/install.py --global planning                       # instalação global
```

Opções: `--force` substitui skills já instaladas; sem `--target`, instala na pasta atual.

### Instalar à mão

Copia a pasta da skill (por exemplo `skills/workflow/planning/`) para `.opencode/skills/planning/` no projeto. Na conversa, o agente carrega-a com `skill("planning")`.

### Bundles

`bundles/*.txt` são listas de nomes de skills (um por linha). Há `all.txt`, `all-generic.txt` e um `cat-<categoria>.txt` por categoria; são gerados por `scripts/build-catalog.py`. Podes criar os teus (as linhas com `#` são comentários); o `validate.py` confirma que só listam skills existentes.

### Plugins, comandos, agentes e kit de projeto

| Pasta | Conteúdo | Como usar |
|---|---|---|
| `plugins/` | `auto-commit.js`, `autopilot.js` (OpenCode plugin API V2) e `autocommit.example.json` | copiar para `.opencode/plugins/` |
| `commands/` | comandos `/auto`, `/autopilot`, `/plan`, `/review`, `/handoff`... | copiar para `.opencode/commands/` |
| `agents/` | `critic` e `reviewer` (só leitura) | copiar para `.opencode/agents/` |
| `templates/project-kit/` | AGENTS.md, opencode.json, scripts/, docs/, ROADMAP, TODO, PROGRESS... | copiar para a raiz de um projeto novo |
| `templates/skill/` | esqueleto de skill nova | usado por `scripts/new-skill.py` |

Ver o `README.md` de cada pasta para detalhes.

## Estrutura do repositório

```
skills/<categoria>/<skill>/SKILL.md   # as skills (mais scripts/ e references/ quando existem)
skills/<categoria>/README.md          # índice gerado da categoria
archive/<repo>/<skill>/               # versões antigas ou quase duplicadas, só para referência
plugins/  commands/  agents/          # artefactos do OpenCode
templates/                            # skill/ e project-kit/
bundles/                              # listas de skills para instalação em lote
scripts/                              # validate.py, build-catalog.py, install.py, new-skill.py
docs/                                 # convenções e origem das skills
catalog.json  CATALOG.md              # catálogo para máquinas e para humanos (gerado)
```

## Formato de uma skill

```yaml
---
name: nome-da-pasta                    # igual à pasta; minúsculas, dígitos e hífenes; máx. 64
description: "Quando usar e o que faz" # 1-1024 carateres; é o que o agente lê para decidir
license: MIT
compatibility: opencode
metadata:
  category: workflow                   # igual à pasta da categoria
  source: ["Repo-Template"]            # repo(s) de origem
  origin: imported                     # imported = copiada; derived = escrita para este repo
  language: pt-PT                      # língua do texto
  scope: generic                       # generic | project-specific
---
```

- **imported**: corpo copiado sem alterações do repo fonte (guardam-se também `source-commit`, `original-name` e `source-path`). Só o frontmatter é normalizado.
- **derived**: escrita aqui a partir do que os projetos fazem; a secção *Proveniência* diz de onde vem e o que é sugestão.
- **generic** serve em qualquer projeto do domínio; **project-specific** é um exemplo trabalhado, útil como modelo.

## Manutenção

```bash
python scripts/new-skill.py minecraft minha-skill "Quando usar..."   # cria a partir do template
python scripts/validate.py                                           # tem de dar OK
python scripts/build-catalog.py                                      # regenera catálogo, READMEs e bundles
python scripts/build-catalog.py --check                              # CI: falha se estiver desatualizado
```

A CI (`.github/workflows/validate.yml`) corre `validate.py` e `build-catalog.py --check` em cada push. Convenções de contribuição em [CONTRIBUTING.md](CONTRIBUTING.md); origem de cada skill em [docs/ORIGEM.md](docs/ORIGEM.md).

## Licenças

- Raiz do repo, scripts, templates, catálogo e skills derivadas: **MIT**.
- Skills importadas mantêm a licença do repo de origem (campo `license`). **11 skills vêm do ScreenMine (AGPL-3.0-only)**: `git-github`, `release-checklist`, `api-verification`, `build-and-test`, `crash-debugging`, `dependency-check`, `fabric-loom-setup`, `input-and-lwjgl`, `mc-port-workflow`, `mixin-migration`, `render-gui-migration`. Antes de as incorporares num produto fechado, avalia as implicações da AGPL.
- Nenhum ficheiro contém segredos; o `validate.py` procura padrões comuns (`ghp_`, `github_pat_`, `AKIA`, chaves privadas, tokens Slack/Discord). Nunca comites chaves reais.
