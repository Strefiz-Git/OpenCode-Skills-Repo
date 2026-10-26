# Comandos

Comandos do OpenCode copiados do `Repo-Template`. Copia os ficheiros para `.opencode/commands/` do teu projeto (ou usa o `templates/project-kit/`, que traz tudo ligado).

Muitos comandos dependem de skills (`automation-pipeline`, `autonomous-workflow`, `thinking-levels`, `planning`...) e de scripts em `templates/project-kit/scripts/`. Instala também essas partes, senão o comando não encontra o que precisa.

| Comando | O que faz |
|---|---|
| `/auto-commit` | Liga/desliga ou mostra o auto commit — /auto-commit status\|auto\|on\|off\|push-on\|push-off |
| `/auto` | Automação total de um objetivo — planeia, implementa, verifica, faz commits e revê, sem perguntas. /auto <objetivo> [--min N] |
| `/autonomia` | Define quanto a IA decide sozinha vs. pergunta — /autonomia guiada\|normal\|alta\|total\|status |
| `/autopilot-stop` | Stop the autopilot and hand off |
| `/autopilot` | Long autonomous work (default 120 min) — only stops on real blockers |
| `/bootstrap` | Set up the project (first run) — detects the stack and fills in docs, commands and the initial roadmap |
| `/checkpoint` | Ponto de guardar a meio da sessão — docs em dia + commit, sem fechar a sessão |
| `/comandos` | Lista todos os comandos disponíveis com uma linha de explicação cada |
| `/commit` | Tidy commits (Conventional Commits) of the pending work |
| `/continuar` | Retoma o trabalho a partir dos ficheiros (depois de /new, crash, compactação ou /desbloquear-pensamento) |
| `/decide` | 5-angle analysis of a question + decision registered in DECISIONS.md |
| `/desbloquear-pensamento` | Tira a IA de um loop/bug (repete a mesma coisa) — reset suave a partir dos ficheiros. Usa "hard" para sessão nova |
| `/handoff` | Close the session — update docs, commit and summarize |
| `/module` | Create a new module (structure, public API, README, tests) and register it in docs/MODULES.md |
| `/noite` | Sessão longa sem supervisão (por defeito 8 h) com mais iterações e travões de segurança. /noite [horas] |
| `/pensamento` | Define quanto a IA pensa antes de agir — /pensamento baixo\|medio\|alto\|auto [tarefa] |
| `/plan` | Breaks a goal down into tasks with acceptance criteria and updates TODO.md |
| `/review` | Self-review of recent work → REVIEW.md (and fix the blockers) |
| `/start` | Session start ritual and immediate start of work |
| `/status` | Quick summary of the project state |
| `/structure` | Audit folder organization, documentation and code reuse, then fix |
