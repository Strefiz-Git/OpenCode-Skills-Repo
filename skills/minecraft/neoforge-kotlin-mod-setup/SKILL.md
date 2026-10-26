---
name: neoforge-kotlin-mod-setup
description: "Set up a NeoForge 1.21.1 mod written in Kotlin with KotlinForForge: clone the official skeleton, configure gradle.properties, build.gradle.kts and neoforge.mods.toml, write the main class on the Kotlin mod bus, and run or build it. Use when starting a NeoForge Kotlin mod or when a Kotlin mod does not load."
license: MIT
compatibility: opencode
metadata:
  category: minecraft
  source: ["NeoForge-Mods-Repo"]
  origin: derived
  language: en
  scope: generic
---

# NeoForge + Kotlin mod setup

## Pinned versions (from the guide; re-check before reusing)

| Item | Value |
|---|---|
| Minecraft | 1.21.1 |
| NeoForge | 21.1.172 |
| KotlinForForge | 6.0.0 |
| Kotlin | 2.2.20 |
| JDK | 21 (JDK 25 is not compatible with NeoForge 1.21.1) |
| `modLoader` in the toml | `"kotlinforforge"` |
| Mod bus | `thedarkcolour.kotlinforforge.neoforge.forge.MOD_BUS` |

## Steps

1. **JDK 21** (Temurin or Corretto), installed from IntelliJ: File > Project Structure > SDKs > Download JDK.
2. **Do not use the IntelliJ "New Project" wizard.** Clone the skeleton:
   ```bash
   git clone --branch 1.21.10-neoforge https://github.com/thedarkcolour/KotlinModdingSkeleton.git my-mod
   ```
3. Open `build.gradle.kts` with **Open as Project** and wait for Gradle to sync.
4. `gradle.properties`: `minecraft_version`, `neoforge_version`, `mod_id`, `mod_name`, `mod_version`, `mod_group`, `org.gradle.jvmargs=-Xmx3G`, `org.gradle.daemon=false`.
5. `build.gradle.kts`: plugins `kotlin("jvm")` and `net.neoforged.gradle.userdev`, Java toolchain 21, the Kotlin for Forge maven repository, dependencies `net.neoforged:neoforge` and `thedarkcolour:kotlinforforge-neoforge`, and `runs` for `client` and `server` (`--nogui`).
6. `src/main/resources/META-INF/neoforge.mods.toml`: `modLoader = "kotlinforforge"`, `loaderVersion = "[6.0,)"`, a `[[mods]]` block and three `[[dependencies.<modid>]]` blocks (`neoforge`, `minecraft`, `kotlinforforge`).
7. Main class:
   ```kotlin
   @Mod("mymod")
   class MyMod(modContainer: ModContainer) {
       init {
           val bus: IEventBus = MOD_BUS
           bus.addListener(::onCommonSetup)
           bus.addListener(::onClientSetup)
       }
       private fun onCommonSetup(event: FMLCommonSetupEvent) {}
       private fun onClientSetup(event: FMLClientSetupEvent) {}
   }
   ```
8. Run: `./gradlew genIntellijRuns`, `./gradlew runClient`, `./gradlew runServer`. Build the jar with `./gradlew build` (output in `build/libs/`).

## Pitfalls

- `modLoader = "javafml"` makes the mod silently not load; it must be `"kotlinforforge"`.
- Using Forge's `FMLJavaModLoadingContext` instead of the Kotlin `MOD_BUS` does not work here.
- A JDK newer than 21 fails the Gradle setup.

## Checklist

- [ ] `runClient` shows the mod's "loaded" log line.
- [ ] `build` produces a jar in `build/libs/`.
- [ ] `LICENSE` present (the guide recommends MIT).

## Provenance

`NeoForge-Mods-Repo/guia-mod-neoforge-kotlin.md` (steps and versions are as written there).
