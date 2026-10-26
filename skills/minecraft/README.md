# Minecraft

Mods Fabric: setup, mixins, portar entre versões, rede, HUD, builds, performance.

> Gerado por `python scripts/build-catalog.py`.

| Skill | Usar quando |
|---|---|
| [`api-verification`](api-verification/SKILL.md) | Confirmar nomes reais de classes, métodos e assinaturas da versão destino antes de os usar. Usar sempre que um nome é duvidoso, em renames e quando o compilador dá erros de símbolo. |
| [`benchmark-optimization`](benchmark-optimization/SKILL.md) | Método para medir e otimizar o desempenho das explosões (microbenchmarks, spark in-game, métricas do mod, regras de hot loop sem alocações) e decidir entre WAVEFRONT, RAY_CACHE e VANILLA com dados. Usa ao otimizar, ao… |
| [`build-and-test`](build-and-test/SKILL.md) | Compilar, correr o cliente e validar o mod, registando resultados. Usar depois de cada grupo de alterações e antes de commits importantes. |
| [`crash-debugging`](crash-debugging/SKILL.md) | Diagnosticar crashes e erros de arranque lendo crash reports, latest.log e stack traces. Usar quando o jogo crasha, o mod não carrega ou há exceções. |
| [`dependency-check`](dependency-check/SKILL.md) | Verificar se as dependências (Fabric API, ModMenu, libs, outros mods) existem para a versão destino e decidir alternativas. Usar na fase 2 ou quando uma lib falha. |
| [`fabric-client-config-modmenu`](fabric-client-config-modmenu/SKILL.md) | Add a persistent JSON config and an in-game settings screen to a Fabric mod, exposed through Mod Menu as an optional dependency. Use when a Fabric mod needs user settings, a gear button in Mod Menu, a config file in… |
| [`fabric-hud-overlay`](fabric-hud-overlay/SKILL.md) | Render a HUD element or world overlay in a Fabric client mod for Minecraft 26.x, register a keybinding, and read vanilla debug flags (such as F3+G chunk borders) through public API instead of a mixin. Use for HUDs,… |
| [`fabric-known-good-baseline`](fabric-known-good-baseline/SKILL.md) | Reuse a known-good Fabric build baseline (Minecraft 26.3, Loom, Gradle wrapper, Java 25, Fabric API, Mod Menu versions) taken from a sibling mod that already compiles. |
| [`fabric-loom-setup`](fabric-loom-setup/SKILL.md) | Configurar Gradle, Fabric Loom, versões e fabric.mod.json para a versão destino do Minecraft. Usar na fase de setup e quando o build falha por versões. |
| [`fabric-mod-setup`](fabric-mod-setup/SKILL.md) | Monta o esqueleto do mod Fabric server-side (fase F0 do progresso.md) - Gradle/Loom, fabric.mod.json, mixins.json, wrapper e arranque do runServer, sem Fabric API. Usa quando o projeto ainda não tem build ou quando for… |
| [`fabric-optional-server-payload`](fabric-optional-server-payload/SKILL.md) | Design a Fabric client mod that works on vanilla servers and only uses a custom network payload when the server also has the mod. Use when adding C2S or S2C packets, CustomPacketPayload records, PayloadTypeRegistry,… |
| [`gradle-build-verify`](gradle-build-verify/SKILL.md) | Compila, testa e valida o mod com Gradle (build, compileJava, test, runServer), interpreta erros comuns de Loom/Mixin/Java 25 e localiza o jar final. Usa antes de commits/pushes de código e ao diagnosticar falhas de… |
| [`input-and-lwjgl`](input-and-lwjgl/SKILL.md) | Migrar teclado, rato, scroll, atalhos e janela quando o backend de input mudou (GLFW, SDL ou eventos novos). Usar em keybindings e envio de input para componentes embebidos. |
| [`mc-port-workflow`](mc-port-workflow/SKILL.md) | Roteiro completo para portar um mod de Minecraft para outra versão. Usar no início do port e sempre que precisares de decidir o próximo passo. |
| [`minecraft-server-parallelism`](minecraft-server-parallelism/SKILL.md) | Plan or review a Minecraft server mod that spreads work across threads (worker pools, regionised ticking, offloading chunk IO, light or pathfinding) while keeping legacy mods safe. |
| [`mixin-explosion`](mixin-explosion/SKILL.md) | Regras para escrever e manter os mixins do mod (ServerExplosionMixin em calculateExplodedPositions e CommandsMixin para /optimizedtnt sem Fabric API), incluindo fallback para o vanilla e confirmação de nomes Mojmap com… |
| [`mixin-migration`](mixin-migration/SKILL.md) | Migrar mixins, accessors e invokers para a versão destino. Usar quando há erros de mixin no arranque ou ao tocar em classes do Minecraft. |
| [`mixin-stale-static-state-fix`](mixin-stale-static-state-fix/SKILL.md) | Fix crashes in a third-party Minecraft mod caused by static state that survives leaving a world (NullPointerException when Minecraft.player becomes null) with a tiny companion mixin on Minecraft.tick, built per loader. |
| [`neoforge-kotlin-mod-setup`](neoforge-kotlin-mod-setup/SKILL.md) | Set up a NeoForge 1.21.1 mod written in Kotlin with KotlinForForge: clone the official skeleton, configure gradle.properties, build.gradle.kts and neoforge.mods.toml, write the main class on the Kotlin mod bus, and run… |
| [`render-gui-migration`](render-gui-migration/SKILL.md) | Migrar render (mundo 3D) e GUI entre versões do Minecraft quando o pipeline de render mudou. Usar em ecrãs, HUD, render de entidades/blocos e texturas dinâmicas. |
| [`unit-testing-parity`](unit-testing-parity/SKILL.md) | Estratégia de testes do mod - núcleo do algoritmo em Java puro testável com JUnit 5, comparação de paridade wavefront vs raios vanilla, cenários de explosão e validação in-game com /optimizedtnt compare (sem Fabric… |
| [`wavefront-algorithm`](wavefront-algorithm/SKILL.md) | Especificação e guia de implementação do algoritmo wavefront (Dijkstra por blocos com bucket queue) que substitui os 1352 raios do vanilla, incluindo custos, paridade e pontos a verificar no bytecode. Usa ao implementar… |
