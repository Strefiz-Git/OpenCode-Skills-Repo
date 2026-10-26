# Workflow

Como um agente planeia, decide, regista o progresso e passa uma sessão a quem vem a seguir.

> Gerado por `python scripts/build-catalog.py`.

| Skill | Usar quando |
|---|---|
| [`agents-md`](agents-md/SKILL.md) | Usa quando for preciso acrescentar, alterar ou revogar uma regra do AGENTS.md, ou atualizar o seu índice. |
| [`automation-pipeline`](automation-pipeline/SKILL.md) | End-to-end automation recipe for a whole goal with no supervision — prepare, plan, start autopilot, work loop, review, handoff — plus overnight safeguards. ALWAYS use when the user runs /auto or /noite, asks you to "faz… |
| [`autonomous-workflow`](autonomous-workflow/SKILL.md) | How to work autonomously during long sessions (~2 hours or more) without interrupting the user. ALWAYS use when the user asks for long/autonomous work, uses /autopilot, says "continue", "work on your own", "do whatever… |
| [`decide-without-asking`](decide-without-asking/SKILL.md) | 5-angle decision method for resolving doubts on your own before asking the user. ALWAYS use whenever you feel like asking a question, have two or more options, ambiguous requirements, a design/library/structure choice,… |
| [`ideias`](ideias/SKILL.md) | Usa para guardar uma ideia ainda sem decisão em ideias.md, ou para promover uma ideia a tarefa. |
| [`loop-recovery`](loop-recovery/SKILL.md) | Detect and break out of loops — the agent repeating the same text, tool call, error fix or idea, or producing degenerate/random repeated output — and restart cleanly from the files. ALWAYS use when the user runs… |
| [`planning`](planning/SKILL.md) | Break down goals, features or milestones into small, ordered, verifiable tasks, with acceptance criteria, priority and size. ALWAYS use when the user asks to "plan", "/plan", for a new feature, a milestone, a big (L) or… |
| [`progress-tracking`](progress-tracking/SKILL.md) | Mantém o progresso.md atualizado (tarefas das fases F0-F7, estado global, log de decisões, perguntas em aberto). Usa sempre que concluíres uma tarefa, tomares uma decisão de design ou o utilizador responder a uma… |
| [`progresso`](progresso/SKILL.md) | Como manter o registo docs/progresso.md. Usar no fim de cada bloco de trabalho concluído e no fim de cada sessão, sempre que se corrigir um bug, se descobrir algo sobre o jogo ou a memória, se tomar uma decisão de… |
| [`project-bootstrap`](project-bootstrap/SKILL.md) | Set up a new project or a template just copied — detect the stack, fill in commands in AGENTS.md, ARCHITECTURE.md, docs/CONVENTIONS.md, README, ROADMAP and the initial TODO, make sure scripts/check.sh works and get… |
| [`project-docs`](project-docs/SKILL.md) | How to read, write and maintain the project's management .md files (README, ROADMAP, TODO, PROGRESS, DECISIONS, QUESTIONS, BUGS, REVIEW, IDEAS, ARCHITECTURE, CHANGELOG, docs/*). ALWAYS use whenever you are about to… |
| [`project-progress-tracker`](project-progress-tracker/SKILL.md) | MANDATORY progress tracking for this repository. A cada tarefa que muda o estado do projeto (código, docs, builds, decisões), atualiza PROGRESS.md na raiz: fase atual, o que mudou, o próximo passo. Carrega (lê)… |
| [`sessao-de-trabalho`](sessao-de-trabalho/SKILL.md) | Como trabalhar com eficiência neste repositório, em Windows. Usar no INÍCIO de qualquer sessão ou tarefa e no FIM dela. Diz por onde começar sem ler o AGENTS.md inteiro, como procurar antes de abrir ficheiros grandes,… |
| [`session-handoff`](session-handoff/SKILL.md) | Session start and end rituals to avoid losing context — startup (read PROGRESS, QUESTIONS, TODO, ROADMAP), checkpoints, pauses, and the final handoff (update docs, verify, commit, summarize). ALWAYS use at the start of… |
| [`thinking-levels`](thinking-levels/SKILL.md) | How deeply to deliberate before and while acting — levels baixo (low), medio (medium) and alto (high), set with /pensamento and stored in .opencode/thinking.level. ALWAYS use at the start of every task, when the user… |
| [`todo`](todo/SKILL.md) | Usa para ler, priorizar, acrescentar ou fechar tarefas em TODO.md. |
