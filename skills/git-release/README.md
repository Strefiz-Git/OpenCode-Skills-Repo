# Git e release

Commits, pushes, fluxo GitHub, deploy e checklists de release.

> Gerado por `python scripts/build-catalog.py`.

| Skill | Usar quando |
|---|---|
| [`auto-commit-powershell`](auto-commit-powershell/SKILL.md) | Fazer commit do trabalho por conta própria, com mensagem útil, depois de verificar testes, segredos e ficheiros que não devem entrar. Use quando o utilizador pedir para commitar, guardar o trabalho, fazer commit, ou… |
| [`auto-commit-pt`](auto-commit-pt/SKILL.md) | Faz commit automático, seguro e em commits lógicos das alterações do projeto, com mensagens Conventional Commits em PT-PT. Usa ao concluir uma tarefa/fase ou quando o utilizador pedir para fazer commit. |
| [`auto-commit`](auto-commit/SKILL.md) | Make small, frequent, well-described git commits (Conventional Commits), with secrets checking, and understand the auto commit plugin that saves checkpoints. ALWAYS use when you finish a logical unit of work, before… |
| [`auto-push`](auto-push/SKILL.md) | Envia os commits para o GitHub de forma segura (verifica build, faz rebase se necessário, nunca usa force). Usa depois do auto-commit ou quando o utilizador pedir push. |
| [`deploy`](deploy/SKILL.md) | Usa para construir a imagem Docker, correr em produção, configurar variáveis, proxy reverso ou volumes. |
| [`git-auto-commit-push`](git-auto-commit-push/SKILL.md) | Usa para fazer commit e push automáticos no fim de uma unidade de trabalho, com scripts/auto-commit.mjs. Define quando commitar e como escrever a mensagem. |
| [`git-commit-workflow`](git-commit-workflow/SKILL.md) | MANDATORY git workflow for every coding task - inspect repository state before starting, create a branch for experimental, large or risky changes, make small atomic commits with Conventional Commit messages that include… |
| [`git-github`](git-github/SKILL.md) | Fluxo git/GitHub para o port: branches, remote, push, tags e releases. Usar ao iniciar o repo, ao criar branches ou ao preparar uma versão. |
| [`git-workflow`](git-workflow/SKILL.md) | Obrigatória em todos os projectos. Commita automaticamente cada alteração concluída, cria branches para trabalho grande, e mantém o histórico legível — sem perguntar ao utilizador. Usar sempre que uma tarefa fechar um… |
| [`release-checklist`](release-checklist/SKILL.md) | Checklist para publicar uma versão do mod portado (jar, metadados, licença, changelog, tag). Usar quando o port está pronto para release. |
| [`release-github`](release-github/SKILL.md) | Prepara e publica uma release do mod no GitHub (versão, build, tag, jar). Usa apenas quando o utilizador pedir explicitamente para fazer release/publicar uma versão. |
