---
name: crash-debugging
description: "Diagnosticar crashes e erros de arranque lendo crash reports, latest.log e stack traces. Usar quando o jogo crasha, o mod não carrega ou há exceções."
license: AGPL-3.0-only
compatibility: opencode
metadata:
  category: minecraft
  source: ["ScreenMine"]
  source-commit: "fa7f977"
  original-name: "crash-debugging"
  source-path: ".opencode/skills/crash-debugging"
  origin: imported
  language: pt-PT
  scope: generic
---

# Debug de crashes

## Onde ver
- `run/crash-reports/crash-*.txt` e `run/logs/latest.log`.
- No terminal do `runClient`.

## Método
1. Lê a **primeira** exceção relevante (a causa), não a última (o efeito). Procura `Caused by:`.
2. Identifica a camada: arranque do loader · mixin · registo · render · input · thread errada.
3. Localiza no stack trace a **primeira linha do teu pacote**.
4. Formula uma hipótese e testa com a menor alteração possível.

## Padrões comuns
- `NoSuchMethodError`/`NoSuchFieldError`/`ClassNotFoundException`: nome/assinatura errada → `api-verification`.
- `MixinApplyError`/`InvalidInjectionException` → `mixin-migration`.
- `IllegalStateException` ligada a render/GL: chamada fora da thread de render ou fora do momento certo do frame.
- `UnsatisfiedLinkError`: nativos em falta/incompatíveis (bibliotecas externas) → `dependency-check`.
- Nada acontece, sem erro: evento não registado / entrypoint em falta no `fabric.mod.json`.

## Regras
- Não "silencies" exceções com try/catch vazio para fazer o erro desaparecer.
- Regista a causa-raiz e a solução em `progresso.md` ("Descobertas").
