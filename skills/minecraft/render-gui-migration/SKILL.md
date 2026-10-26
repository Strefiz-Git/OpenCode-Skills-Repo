---
name: render-gui-migration
description: "Migrar render (mundo 3D) e GUI entre versões do Minecraft quando o pipeline de render mudou. Usar em ecrãs, HUD, render de entidades/blocos e texturas dinâmicas."
license: AGPL-3.0-only
compatibility: opencode
metadata:
  category: minecraft
  source: ["ScreenMine"]
  source-commit: "fa7f977"
  original-name: "render-gui-migration"
  source-path: ".opencode/skills/render-gui-migration"
  origin: imported
  language: pt-PT
  scope: generic
---

# Render e GUI

## Princípios
- O render é normalmente **a parte mais arriscada**. Faz um **spike** primeiro (ex.: quad no mundo com cor sólida; um ecrã GUI vazio) antes de migrar o resto.
- Não assumas que o pipeline antigo (`RenderLayer`, `VertexConsumer`, `MatrixStack`) existe igual. Lê as classes reais (ver `api-verification`).

## GUI
- Identifica o que mudou: método de desenho do ecrã (`render` vs extração de estado), tipos de eventos de input (parâmetros soltos vs records), `setScreen`, texto/formatação, widgets.
- Migra **um ecrã simples** primeiro; usa-o como molde para os restantes.
- Mantém a lógica de negócio separada do desenho para facilitar a migração.

## Render no mundo
- Ponto de entrada: evento de render do mundo da Fabric API (confirma qual existe na versão).
- Para texturas dinâmicas (vídeo, browser, canvas): confirma como registar/atualizar uma textura e como a ligar a um pipeline/estado de render.
- Verifica: culling, profundidade, blending, luz (unlit vs lit), ordem de desenho.

## Verificações
- Resolução e proporção corretas; sem espelhamento; sem z-fighting.
- Funciona com e sem shaders (se relevante).
- Sem *leaks* de texturas (liberta quando o objeto é removido).

## Se não for possível
Regista em `progresso.md`, propõe alternativa (ex.: só GUI/overlay) e pergunta ao utilizador antes de cortar funcionalidade.
