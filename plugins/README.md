# Plugins

Plugins do OpenCode (API V2, https://opencode.ai/v2/docs/build/plugins) copiados do `Repo-Template`. Copia para `.opencode/plugins/`.

| Ficheiro | O que faz |
|---|---|
| `auto-commit.js` | Rede de segurança: quando a sessão fica inativa e há alterações, faz um commit `chore(wip): checkpoint`. Ligado por omissão se existir um repositório git. Nunca comita ficheiros sensíveis e cancela se o diff tiver um padrão de segredo. |
| `autopilot.js` | Experimental: mantém o agente a trabalhar durante um orçamento de tempo (`/autopilot [min]`). Só atua enquanto `.opencode/autopilot.state` existe com `active=1`. Parar com `/autopilot-stop`, um ficheiro `STOP` na raiz, ou Esc/erro. |
| `autocommit.example.json` | Configuração de exemplo; copiar para `.opencode/autocommit.json`. |

Os plugins usam scripts do kit (`templates/project-kit/scripts/autocommit.sh`, `autopilot.sh`). A versão v1 antiga dos plugins não foi encontrada nos repos atuais e não está incluída.
