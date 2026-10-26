# Catálogo

> Gerado por `python scripts/build-catalog.py` — não editar à mão.

**104 skills** em 17 categorias (86 genéricas, 18 exemplos específicos de projeto).

Legenda — **origem**: `imported` = copiada de um repo do autor (corpo inalterado), `derived` = escrita para este repo a partir do que os projetos fazem. **âmbito**: `generic` = reutilizável em qualquer projeto do domínio, `project-specific` = exemplo trabalhado ligado a um projeto. **lang** = língua do texto da skill.

## Workflow

Como um agente planeia, decide, regista o progresso e passa uma sessão a quem vem a seguir.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`agents-md`](skills/workflow/agents-md/SKILL.md) | Usa quando for preciso acrescentar, alterar ou revogar uma regra do AGENTS.md, ou atualizar o seu índice. | imported | generic | pt-PT | TugaConverte |
| [`automation-pipeline`](skills/workflow/automation-pipeline/SKILL.md) | End-to-end automation recipe for a whole goal with no supervision — prepare, plan, start autopilot, work loop, review, handoff — plus overnight… | imported | generic | en | Repo-Template |
| [`autonomous-workflow`](skills/workflow/autonomous-workflow/SKILL.md) | How to work autonomously during long sessions (~2 hours or more) without interrupting the user. ALWAYS use when the user asks for long/autonomous… | imported | generic | en | Repo-Template |
| [`decide-without-asking`](skills/workflow/decide-without-asking/SKILL.md) | 5-angle decision method for resolving doubts on your own before asking the user. ALWAYS use whenever you feel like asking a question, have two or… | imported | generic | en | Repo-Template |
| [`ideias`](skills/workflow/ideias/SKILL.md) | Usa para guardar uma ideia ainda sem decisão em ideias.md, ou para promover uma ideia a tarefa. | imported | generic | pt-PT | TugaConverte |
| [`loop-recovery`](skills/workflow/loop-recovery/SKILL.md) | Detect and break out of loops — the agent repeating the same text, tool call, error fix or idea, or producing degenerate/random repeated output — and… | imported | generic | en | Repo-Template |
| [`planning`](skills/workflow/planning/SKILL.md) | Break down goals, features or milestones into small, ordered, verifiable tasks, with acceptance criteria, priority and size. ALWAYS use when the user… | imported | generic | en | Repo-Template |
| [`progress-tracking`](skills/workflow/progress-tracking/SKILL.md) | Mantém o progresso.md atualizado (tarefas das fases F0-F7, estado global, log de decisões, perguntas em aberto). Usa sempre que concluíres uma… | imported | project-specific | pt-PT | OtimizedTNT |
| [`progresso`](skills/workflow/progresso/SKILL.md) | Como manter o registo docs/progresso.md. Usar no fim de cada bloco de trabalho concluído e no fim de cada sessão, sempre que se corrigir um bug, se… | imported | generic | pt-PT | AssetoCorsaTelemetry |
| [`project-bootstrap`](skills/workflow/project-bootstrap/SKILL.md) | Set up a new project or a template just copied — detect the stack, fill in commands in AGENTS.md, ARCHITECTURE.md, docs/CONVENTIONS.md, README,… | imported | generic | en | Repo-Template |
| [`project-docs`](skills/workflow/project-docs/SKILL.md) | How to read, write and maintain the project's management .md files (README, ROADMAP, TODO, PROGRESS, DECISIONS, QUESTIONS, BUGS, REVIEW, IDEAS,… | imported | generic | en | Repo-Template |
| [`project-progress-tracker`](skills/workflow/project-progress-tracker/SKILL.md) | MANDATORY progress tracking for this repository. A cada tarefa que muda o estado do projeto (código, docs, builds, decisões), atualiza PROGRESS.md na… | imported | generic | pt-PT | DailyCompany |
| [`sessao-de-trabalho`](skills/workflow/sessao-de-trabalho/SKILL.md) | Como trabalhar com eficiência neste repositório, em Windows. Usar no INÍCIO de qualquer sessão ou tarefa e no FIM dela. Diz por onde começar sem ler… | imported | generic | pt-PT | AssetoCorsaTelemetry |
| [`session-handoff`](skills/workflow/session-handoff/SKILL.md) | Session start and end rituals to avoid losing context — startup (read PROGRESS, QUESTIONS, TODO, ROADMAP), checkpoints, pauses, and the final handoff… | imported | generic | en | Repo-Template |
| [`thinking-levels`](skills/workflow/thinking-levels/SKILL.md) | How deeply to deliberate before and while acting — levels baixo (low), medio (medium) and alto (high), set with /pensamento and stored in… | imported | generic | en | Repo-Template |
| [`todo`](skills/workflow/todo/SKILL.md) | Usa para ler, priorizar, acrescentar ou fechar tarefas em TODO.md. | imported | generic | pt-PT | TugaConverte |

## Engineering

Depuração, revisão, segurança, estrutura, reutilização, documentação e verificação.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`app-code-organizer`](skills/engineering/app-code-organizer/SKILL.md) | Organiza os ficheiros de código DENTRO da app - packages, camadas, features, nomes de ficheiros, recursos (res/), e módulos Python/Flask. Usar SEMPRE… | imported | generic | pt-PT | DailyCompany |
| [`code-documentation`](skills/engineering/code-documentation/SKILL.md) | Document code and the project in layers — docstrings on everything public, a README in each module, a docs/MODULES.md catalog, comments only for the… | imported | generic | en | Repo-Template |
| [`code-review`](skills/engineering/code-review/SKILL.md) | Rigorous self-review of your own work (and of other people's code) before closing a large task, a milestone or a long block of autonomous work,… | imported | generic | en | Repo-Template |
| [`codigo-modular`](skills/engineering/codigo-modular/SKILL.md) | Regras para escrever código que não engorda. Usar SEMPRE que se criar ou alterar código (Python, JavaScript, CSS ou HTML), antes de acrescentar mais… | imported | generic | pt-PT | AssetoCorsaTelemetry |
| [`debugging`](skills/engineering/debugging/SKILL.md) | Systematic method to diagnose and fix bugs, test failures, build errors, crashes and unexpected behavior. ALWAYS use when something fails, a test… | imported | generic | en | Repo-Template |
| [`documentacao`](skills/engineering/documentacao/SKILL.md) | Como manter o AGENTS.md, o README.md e a pasta docs/. Usar quando se descobrir uma armadilha que outra pessoa cairia (vira Regra), quando mudar a… | imported | generic | pt-PT | AssetoCorsaTelemetry |
| [`mesma-convencao`](skills/engineering/mesma-convencao/SKILL.md) | Como os dois jogos (Assetto Corsa e F1 25) têm de dizer a mesma coisa no painel. Usar sempre que se acrescentar, renomear ou reformatar um valor que… | imported | project-specific | pt-PT | AssetoCorsaTelemetry |
| [`performance`](skills/engineering/performance/SKILL.md) | Usa para medir ou melhorar a velocidade do site (carregamento, uploads, conversões, memória) ou antes de acrescentar uma dependência. | imported | project-specific | pt-PT | TugaConverte |
| [`project-folder-organizer`](skills/engineering/project-folder-organizer/SKILL.md) | Organiza a estrutura de pastas de um projeto ao nível do repositório (raiz, docs, scripts, assets, módulos, backend/app). Usar SEMPRE que o… | imported | generic | pt-PT | DailyCompany |
| [`project-structure`](skills/engineering/project-structure/SKILL.md) | Organize the project's folders and files clearly and predictably — where everything lives, structure by feature, clean root, tests mirroring the… | imported | generic | en | Repo-Template |
| [`readme`](skills/engineering/readme/SKILL.md) | Usa quando o README.md ficou desatualizado (motor novo, variável nova, endpoint novo) ou for preciso reescrever partes dele. | imported | generic | pt-PT | TugaConverte |
| [`refactoring-modular`](skills/engineering/refactoring-modular/SKILL.md) | Write modular code and refactor safely — clear responsibilities, small files and functions, low coupling, no duplication — without changing behavior.… | imported | generic | en | Repo-Template |
| [`research-first`](skills/engineering/research-first/SKILL.md) | Verify facts and APIs in the official documentation and in the repo itself before assuming. ALWAYS use when you're about to use a library, framework,… | imported | generic | en | Repo-Template |
| [`reusable-modules`](skills/engineering/reusable-modules/SKILL.md) | Write code in modules and functions reusable enough that any other part of the program can call them — reuse before writing, pure functions with… | imported | generic | en | Repo-Template |
| [`security-review`](skills/engineering/security-review/SKILL.md) | Practical security checklist for code and repositories — secrets, input validation, authentication/authorization, files and paths, network,… | imported | generic | en | Repo-Template |
| [`seguranca`](skills/engineering/seguranca/SKILL.md) | Usa ao mexer em uploads, downloads, nomes de ficheiros, processos externos, limpeza de ficheiros ou qualquer coisa exposta à internet. | imported | project-specific | pt-PT | TugaConverte |
| [`testes`](skills/engineering/testes/SKILL.md) | Como verificar alterações e acrescentar testes neste projecto. Usar depois de qualquer alteração de código antes de commitar, ao criar um teste, ao… | imported | generic | pt-PT | AssetoCorsaTelemetry |
| [`testing-verification`](skills/engineering/testing-verification/SKILL.md) | Prove the work is really done — write tests, run scripts/check.sh, define reproducible manual verification, and apply the Definition of Done. ALWAYS… | imported | generic | en | Repo-Template |

## Git e release

Commits, pushes, fluxo GitHub, deploy e checklists de release.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`auto-commit-powershell`](skills/git-release/auto-commit-powershell/SKILL.md) | Fazer commit do trabalho por conta própria, com mensagem útil, depois de verificar testes, segredos e ficheiros que não devem entrar. Use quando o… | imported | generic | pt-PT | QrCodeGenerator |
| [`auto-commit-pt`](skills/git-release/auto-commit-pt/SKILL.md) | Faz commit automático, seguro e em commits lógicos das alterações do projeto, com mensagens Conventional Commits em PT-PT. Usa ao concluir uma… | imported | generic | pt-PT | OtimizedTNT |
| [`auto-commit`](skills/git-release/auto-commit/SKILL.md) | Make small, frequent, well-described git commits (Conventional Commits), with secrets checking, and understand the auto commit plugin that saves… | imported | generic | en | Repo-Template |
| [`auto-push`](skills/git-release/auto-push/SKILL.md) | Envia os commits para o GitHub de forma segura (verifica build, faz rebase se necessário, nunca usa force). Usa depois do auto-commit ou quando o… | imported | generic | pt-PT | OtimizedTNT |
| [`deploy`](skills/git-release/deploy/SKILL.md) | Usa para construir a imagem Docker, correr em produção, configurar variáveis, proxy reverso ou volumes. | imported | project-specific | pt-PT | TugaConverte |
| [`git-auto-commit-push`](skills/git-release/git-auto-commit-push/SKILL.md) | Usa para fazer commit e push automáticos no fim de uma unidade de trabalho, com scripts/auto-commit.mjs. Define quando commitar e como escrever a… | imported | generic | pt-PT | TugaConverte |
| [`git-commit-workflow`](skills/git-release/git-commit-workflow/SKILL.md) | MANDATORY git workflow for every coding task - inspect repository state before starting, create a branch for experimental, large or risky changes,… | imported | generic | en | DailyCompany |
| [`git-github`](skills/git-release/git-github/SKILL.md) | Fluxo git/GitHub para o port: branches, remote, push, tags e releases. Usar ao iniciar o repo, ao criar branches ou ao preparar uma versão. | imported | generic | pt-PT | ScreenMine |
| [`git-workflow`](skills/git-release/git-workflow/SKILL.md) | Obrigatória em todos os projectos. Commita automaticamente cada alteração concluída, cria branches para trabalho grande, e mantém o histórico legível… | imported | generic | pt-PT | AssetoCorsaTelemetry |
| [`release-checklist`](skills/git-release/release-checklist/SKILL.md) | Checklist para publicar uma versão do mod portado (jar, metadados, licença, changelog, tag). Usar quando o port está pronto para release. | imported | generic | pt-PT | ScreenMine |
| [`release-github`](skills/git-release/release-github/SKILL.md) | Prepara e publica uma release do mod no GitHub (versão, build, tag, jar). Usa apenas quando o utilizador pedir explicitamente para fazer… | imported | generic | pt-PT | OtimizedTNT |

## Design

Design de interfaces e estilo visual.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`estilizacao`](skills/design/estilizacao/SKILL.md) | Guia de estilo visual da interface do AccMaker (tema escuro, tokens de cor, tipografia, espaçamento, estados e acessibilidade) para uma UI limpa,… | imported | project-specific | pt-PT | AccMaker |
| [`ui-design`](skills/design/ui-design/SKILL.md) | Design and review interfaces to a professional standard — visual hierarchy, spacing, typography, color and contrast, component states, accessibility,… | imported | generic | en | Repo-Template |

## Windows desktop

WinForms e pequenos executáveis Windows autónomos.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`build-exe-leve`](skills/desktop-windows/build-exe-leve/SKILL.md) | Escolher a linguagem e as flags de compilação para o AccMaker ficar num único .exe muito leve e standalone, e medir o tamanho. Usar ao criar o… | imported | generic | pt-PT | AccMaker |
| [`winforms-design`](skills/desktop-windows/winforms-design/SKILL.md) | Construir e rever a interface WinForms em C#, com o layout declarado em vez de contagens de píxeis. Usar quando se acrescenta um campo, uma categoria… | imported | generic | pt-PT | QrCodeGenerator |

## Minecraft

Mods Fabric: setup, mixins, portar entre versões, rede, HUD, builds, performance.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`api-verification`](skills/minecraft/api-verification/SKILL.md) | Confirmar nomes reais de classes, métodos e assinaturas da versão destino antes de os usar. Usar sempre que um nome é duvidoso, em renames e quando o… | imported | generic | pt-PT | ScreenMine |
| [`benchmark-optimization`](skills/minecraft/benchmark-optimization/SKILL.md) | Método para medir e otimizar o desempenho das explosões (microbenchmarks, spark in-game, métricas do mod, regras de hot loop sem alocações) e decidir… | imported | project-specific | pt-PT | OtimizedTNT |
| [`build-and-test`](skills/minecraft/build-and-test/SKILL.md) | Compilar, correr o cliente e validar o mod, registando resultados. Usar depois de cada grupo de alterações e antes de commits importantes. | imported | generic | pt-PT | ScreenMine |
| [`crash-debugging`](skills/minecraft/crash-debugging/SKILL.md) | Diagnosticar crashes e erros de arranque lendo crash reports, latest.log e stack traces. Usar quando o jogo crasha, o mod não carrega ou há exceções. | imported | generic | pt-PT | ScreenMine |
| [`dependency-check`](skills/minecraft/dependency-check/SKILL.md) | Verificar se as dependências (Fabric API, ModMenu, libs, outros mods) existem para a versão destino e decidir alternativas. Usar na fase 2 ou quando… | imported | generic | pt-PT | ScreenMine |
| [`fabric-client-config-modmenu`](skills/minecraft/fabric-client-config-modmenu/SKILL.md) | Add a persistent JSON config and an in-game settings screen to a Fabric mod, exposed through Mod Menu as an optional dependency. Use when a Fabric… | derived | generic | en | RocketWithSpearMod, ClientHarvestMod, Minecraft-MultyCore-Mod, Slime-Chunk-Finder-Helper-Mod |
| [`fabric-hud-overlay`](skills/minecraft/fabric-hud-overlay/SKILL.md) | Render a HUD element or world overlay in a Fabric client mod for Minecraft 26.x, register a keybinding, and read vanilla debug flags (such as F3+G… | derived | generic | en | Slime-Chunk-Finder-Helper-Mod, easy-building-minecraft-mod |
| [`fabric-known-good-baseline`](skills/minecraft/fabric-known-good-baseline/SKILL.md) | Reuse a known-good Fabric build baseline (Minecraft 26.3, Loom, Gradle wrapper, Java 25, Fabric API, Mod Menu versions) taken from a sibling mod that… | derived | generic | en | Minecraft-MultyCore-Mod, RocketWithSpearMod, Slime-Chunk-Finder-Helper-Mod, easy-building-minecraft-mod, ScreenMine, OtimizedTNT |
| [`fabric-loom-setup`](skills/minecraft/fabric-loom-setup/SKILL.md) | Configurar Gradle, Fabric Loom, versões e fabric.mod.json para a versão destino do Minecraft. Usar na fase de setup e quando o build falha por… | imported | generic | pt-PT | ScreenMine |
| [`fabric-mod-setup`](skills/minecraft/fabric-mod-setup/SKILL.md) | Monta o esqueleto do mod Fabric server-side (fase F0 do progresso.md) - Gradle/Loom, fabric.mod.json, mixins.json, wrapper e arranque do runServer,… | imported | generic | pt-PT | OtimizedTNT |
| [`fabric-optional-server-payload`](skills/minecraft/fabric-optional-server-payload/SKILL.md) | Design a Fabric client mod that works on vanilla servers and only uses a custom network payload when the server also has the mod. Use when adding C2S… | derived | generic | en | RocketWithSpearMod, Slime-Chunk-Finder-Helper-Mod, Minecraft-MultyCore-Mod |
| [`gradle-build-verify`](skills/minecraft/gradle-build-verify/SKILL.md) | Compila, testa e valida o mod com Gradle (build, compileJava, test, runServer), interpreta erros comuns de Loom/Mixin/Java 25 e localiza o jar final.… | imported | generic | pt-PT | OtimizedTNT |
| [`input-and-lwjgl`](skills/minecraft/input-and-lwjgl/SKILL.md) | Migrar teclado, rato, scroll, atalhos e janela quando o backend de input mudou (GLFW, SDL ou eventos novos). Usar em keybindings e envio de input… | imported | generic | en | ScreenMine |
| [`mc-port-workflow`](skills/minecraft/mc-port-workflow/SKILL.md) | Roteiro completo para portar um mod de Minecraft para outra versão. Usar no início do port e sempre que precisares de decidir o próximo passo. | imported | generic | pt-PT | ScreenMine |
| [`minecraft-server-parallelism`](skills/minecraft/minecraft-server-parallelism/SKILL.md) | Plan or review a Minecraft server mod that spreads work across threads (worker pools, regionised ticking, offloading chunk IO, light or pathfinding)… | derived | generic | en | Minecraft-MultyCore-Mod |
| [`mixin-explosion`](skills/minecraft/mixin-explosion/SKILL.md) | Regras para escrever e manter os mixins do mod (ServerExplosionMixin em calculateExplodedPositions e CommandsMixin para /optimizedtnt sem Fabric… | imported | project-specific | pt-PT | OtimizedTNT |
| [`mixin-migration`](skills/minecraft/mixin-migration/SKILL.md) | Migrar mixins, accessors e invokers para a versão destino. Usar quando há erros de mixin no arranque ou ao tocar em classes do Minecraft. | imported | generic | pt-PT | ScreenMine |
| [`mixin-stale-static-state-fix`](skills/minecraft/mixin-stale-static-state-fix/SKILL.md) | Fix crashes in a third-party Minecraft mod caused by static state that survives leaving a world (NullPointerException when Minecraft.player becomes… | derived | generic | en | fix-easybuilding, easy-building-minecraft-mod |
| [`neoforge-kotlin-mod-setup`](skills/minecraft/neoforge-kotlin-mod-setup/SKILL.md) | Set up a NeoForge 1.21.1 mod written in Kotlin with KotlinForForge: clone the official skeleton, configure gradle.properties, build.gradle.kts and… | derived | generic | en | NeoForge-Mods-Repo |
| [`render-gui-migration`](skills/minecraft/render-gui-migration/SKILL.md) | Migrar render (mundo 3D) e GUI entre versões do Minecraft quando o pipeline de render mudou. Usar em ecrãs, HUD, render de entidades/blocos e… | imported | generic | pt-PT | ScreenMine |
| [`unit-testing-parity`](skills/minecraft/unit-testing-parity/SKILL.md) | Estratégia de testes do mod - núcleo do algoritmo em Java puro testável com JUnit 5, comparação de paridade wavefront vs raios vanilla, cenários de… | imported | project-specific | pt-PT | OtimizedTNT |
| [`wavefront-algorithm`](skills/minecraft/wavefront-algorithm/SKILL.md) | Especificação e guia de implementação do algoritmo wavefront (Dijkstra por blocos com bucket queue) que substitui os 1352 raios do vanilla, incluindo… | imported | project-specific | pt-PT | OtimizedTNT |

## Discord

Bots de Discord: arquitetura de bot de música e templates de servidor.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`discord-music-bot-architecture`](skills/discord/discord-music-bot-architecture/SKILL.md) | Structure a Discord music bot in TypeScript with discord.js v14 and @discordjs/voice: per-guild player manager, queue, extractors with fallback,… | derived | generic | en | Discord-Easy-Music-Bot |
| [`discord-server-template-from-html`](skills/discord/discord-server-template-from-html/SKILL.md) | Turn a pasted Discord sidebar HTML dump into a server-template JSON for a Discord server-builder bot, and know the limits of what a template can… | derived | generic | en | Discord-server-builder-bot |

## Web

Flask/Socket.IO, front-end e sites de conversão.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`flask-socketio-lan-app`](skills/web/flask-socketio-lan-app/SKILL.md) | Build or maintain a Flask + Flask-SocketIO + vanilla-JS real-time app (chat, WebRTC voice, file uploads) that runs on a local network with JSON-file… | derived | generic | en | SocialCord |
| [`frontend`](skills/web/frontend/SKILL.md) | Usa ao alterar a interface em public/ (HTML, CSS, JS do browser). Mantém a UI leve, acessível e sem framework. | imported | project-specific | pt-PT | TugaConverte |
| [`novo-conversor`](skills/web/novo-conversor/SKILL.md) | Usa para acrescentar um formato a um motor existente ou um motor novo (binário externo) ao TugaConverte. | imported | project-specific | pt-PT | TugaConverte |
| [`sem-limites`](skills/web/sem-limites/SKILL.md) | Usa sempre que estiveres tentado a pôr um limite (tamanho, quantidade, tempo, quota) ou quando o utilizador pedir para limitar. Garante que "sem… | imported | project-specific | pt-PT | TugaConverte |

## Bases de dados

Esquemas e persistência para apps e bots.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`prisma-sqlite-bot-state`](skills/database/prisma-sqlite-bot-state/SKILL.md) | Model per-guild or per-user state for a Node/TypeScript bot with Prisma and SQLite: settings, a persisted queue, liked items, upserts and cascade… | derived | generic | en | Discord-Easy-Music-Bot |

## Python

Ferramentas e scripts Python.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`resilient-external-tool-runner`](skills/python/resilient-external-tool-runner/SKILL.md) | Wrap an external tool or flaky network step (such as yt-dlp) in Python with classified failures, bounded exponential-backoff retries, per-item debug… | derived | generic | en | Spotify_Playlist_Download_x64 |

## Cross-language

Manter várias implementações idênticas.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`multi-language-spec-parity`](skills/cross-language/multi-language-spec-parity/SKILL.md) | Implement the same format or algorithm in several languages or stacks (C#, Java, Kotlin, Python, web) and keep them byte-identical using one written… | derived | generic | en | QrCodeGenerator |

## Mobile

Apps Android / Kotlin / Compose.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`android-alarms-notifications`](skills/mobile/android-alarms-notifications/SKILL.md) | Implement reliable alarms, reminders and notifications in Android apps written in Kotlin - AlarmManager exact alarms, setAlarmClock, notification… | imported | generic | en | DailyCompany |
| [`android-backup-restore`](skills/mobile/android-backup-restore/SKILL.md) | Export and import EVERYTHING of an offline Kotlin Jetpack Compose Android app in one zip - all domain data (wardrobe, outfits, tasks, events,… | imported | generic | en | DailyCompany |
| [`android-compose-ui-design`](skills/mobile/android-compose-ui-design/SKILL.md) | Design and build Jetpack Compose screens and components for the DailyCompany Android app - stateless screens with UiState… | imported | generic | en | DailyCompany |
| [`android-core-app-split`](skills/mobile/android-core-app-split/SKILL.md) | Structure a Kotlin project as a pure JVM :core module plus an Android :app module, test the core with Gradle, and verify the app by building the APK… | derived | generic | en | QrCodeGenerator |
| [`android-daily-planner`](skills/mobile/android-daily-planner/SKILL.md) | Design and build the core of a personal daily-planner Android app in Kotlin and Jetpack Compose - Today screen combining tasks, notes, events,… | imported | project-specific | en | DailyCompany |
| [`android-data-offline`](skills/mobile/android-data-offline/SKILL.md) | Build the data layer of Android apps in Kotlin - Room database, Retrofit + kotlinx.serialization networking, DataStore preferences, repositories,… | imported | generic | en | DailyCompany |
| [`android-debugging-adb`](skills/mobile/android-debugging-adb/SKILL.md) | Debug Android apps using adb, logcat, emulator commands and stack-trace analysis - installing and launching the app, reading crashes (FATAL… | imported | generic | en | DailyCompany |
| [`android-gradle-build`](skills/mobile/android-gradle-build/SKILL.md) | Configure and fix Gradle builds for Android projects (Kotlin DSL) - version catalog (libs.versions.toml), Android Gradle Plugin, Kotlin, KSP and… | imported | generic | en | DailyCompany |
| [`android-hilt-di`](skills/mobile/android-hilt-di/SKILL.md) | Use this skill whenever the task involves dependency injection in this Android app - Hilt modules, @InstallIn, @HiltViewModel, qualifiers for… | imported | generic | en | DailyCompany |
| [`android-i18n-theme`](skills/mobile/android-i18n-theme/SKILL.md) | Manage all user-facing text and the visual theme of a Kotlin Jetpack Compose Android app through Kotlin objects instead of strings.xml - the… | imported | generic | pt-PT | DailyCompany |
| [`android-images-media`](skills/mobile/android-images-media/SKILL.md) | Handle photos in the DailyCompany Android app - Photo Picker and camera capture without storage permissions, copying images to filesDir/images,… | imported | generic | en | DailyCompany |
| [`android-maps-location`](skills/mobile/android-maps-location/SKILL.md) | Add maps, markers, routes and device location to Android apps built with Kotlin and Jetpack Compose - Google Maps Compose (or OpenStreetMap-based… | imported | generic | en | DailyCompany |
| [`android-recurring-events-dates`](skills/mobile/android-recurring-events-dates/SKILL.md) | Model and compute dates, times, time zones and recurring events in Kotlin Android apps using java.time - one-off and repeating events (daily, weekly… | imported | generic | en | DailyCompany |
| [`android-release-security`](skills/mobile/android-release-security/SKILL.md) | Prepare Android apps for release and keep them secure - R8/ProGuard shrinking and keep rules, release signing with a keystore,… | imported | generic | en | DailyCompany |
| [`android-testing`](skills/mobile/android-testing/SKILL.md) | Write and run tests for Kotlin Android apps with Jetpack Compose - JUnit unit tests for ViewModels and repositories, coroutine and Flow testing… | imported | generic | en | DailyCompany |
| [`android-wardrobe-outfits`](skills/mobile/android-wardrobe-outfits/SKILL.md) | Build a digital wardrobe and outfit suggestion feature for the DailyCompany Android app - clothing items with photos and multiple categories, slots… | imported | project-specific | en | DailyCompany |
| [`kotlin-compose-android`](skills/mobile/kotlin-compose-android/SKILL.md) | Build, modify, debug and review native Android apps written in Kotlin with Jetpack Compose (Material 3, ViewModel, StateFlow, Navigation Compose,… | imported | generic | en | DailyCompany |

## C / C++

Pequenos programas nativos e builds.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`c-windows-mingw-build`](skills/c-cpp/c-windows-mingw-build/SKILL.md) | Build a small C program for Windows with MinGW gcc from a PowerShell script, and embed binary files (images, data) into the executable with objcopy. | derived | generic | en | Bk_Query |

## DevOps

Correr software como serviço e operá-lo.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`windows-service-nssm`](skills/devops/windows-service-nssm/SKILL.md) | Run a Node or other long-lived program as an auto-starting Windows service with NSSM, with rotating stdout/stderr logs, plus install, check and… | derived | generic | en | Discord-Easy-Music-Bot |

## Integrações

Pesquisar e ligar APIs de terceiros.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`pesquisar-api-email`](skills/integrations/pesquisar-api-email/SKILL.md) | Pesquisa na web e compara APIs oficiais para criar mailboxes de email reais e permanentes (nunca temporárias) e recomenda a melhor para o AccMaker.… | imported | project-specific | pt-PT | AccMaker |
| [`provider-agentmail`](skills/integrations/provider-agentmail/SKILL.md) | Implementar e manter o fornecedor AgentMail (plano gratis, 3 inboxes) no AccMaker, com listar, criar e apagar inboxes a qualquer momento para trocar… | imported | project-specific | pt-PT | AccMaker |

## Godot

Jogos Godot 4: consola de debug, Steam e multiplayer.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`godot-debug-console`](skills/godot/godot-debug-console/SKILL.md) | Plan and build a reusable in-game command console for any Godot 4 project: Autoload with CanvasLayer UI, command registry and parser, autocomplete… | derived | generic | en | Vivo-Sprint |
| [`godotsteam-lobby-multiplayer`](skills/godot/godotsteam-lobby-multiplayer/SKILL.md) | Add Steam lobbies, friends, invites, voice chat and P2P multiplayer to a Godot 4 game with GodotSteam (GDExtension) and SteamMultiplayerPeer,… | derived | generic | en | Vivo-Sprint |

## Dados e telemetria

Painéis de telemetria e interpretação de dados de jogos.

| Skill | O que faz | Origem | Âmbito | Lang | Fonte |
|---|---|---|---|---|---|
| [`jogos-e-capacidades`](skills/data-telemetry/jogos-e-capacidades/SKILL.md) | Checklist para acrescentar um campo de telemetria, uma capacidade ou um jogo novo ao painel. Usar sempre que se acrescentar algo ao snapshot() de um… | imported | project-specific | pt-PT | AssetoCorsaTelemetry |
