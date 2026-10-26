---
name: fabric-client-config-modmenu
description: "Add a persistent JSON config and an in-game settings screen to a Fabric mod, exposed through Mod Menu as an optional dependency. Use when a Fabric mod needs user settings, a gear button in Mod Menu, a config file in config/, or when Mod Menu must not be a hard requirement."
license: MIT
compatibility: opencode
metadata:
  category: minecraft
  source: ["RocketWithSpearMod", "ClientHarvestMod", "Minecraft-MultyCore-Mod", "Slime-Chunk-Finder-Helper-Mod"]
  origin: derived
  language: en
  scope: generic
---

# Fabric config + Mod Menu screen

The pattern used in `RocketWithSpearMod`, `ClientHarvestMod`, `Slime-Chunk-Finder-Helper-Mod` and `Minecraft-MultyCore-Mod`.

## 1. Config class (plain object, JSON file)

- One class with **public fields that carry the defaults** (`public boolean enabled = true;`).
- A lazy singleton: `get()` calls `load()` once and caches the instance.
- File: `FabricLoader.getInstance().getConfigDir().toFile()` + `"<modid>.json"`. Serialize with Gson `setPrettyPrinting()`.
- `load()`: if the file exists, parse it; on a read/parse error or a `null` result fall back to `new Config()`. Write the file back (`save()`) so new fields appear after an update.
- `save()`: `mkdirs()` on the parent, write the JSON, swallow `IOException` (a read-only config folder must not crash the game).
- Derived helpers live on the class (`useOffHandPreferred()`), not in the screen.

## 2. Config screen

- A `Screen` subclass that mutates the singleton and calls `save()` on every change (RocketWithSpearMod's `ModConfigScreen`).
- Keep screens in their own package (`config/` or `screen/`) and keep game logic out of them.

## 3. Mod Menu entry point

```java
public class ModMenuIntegration implements ModMenuApi {
    @Override
    public ConfigScreenFactory<?> getModConfigScreenFactory() {
        return ModConfigScreen::new;
    }
}
```

Register it in `fabric.mod.json`, and declare Mod Menu as a **suggestion**, not a dependency:

```json
"entrypoints": { "modmenu": ["com.example.mod.compat.ModMenuIntegration"] },
"suggests":    { "modmenu": "*" }
```

Put the class in a `compat/` package so nothing else in the mod references Mod Menu types: the mod must load when Mod Menu is absent.

## 4. Gradle

```groovy
repositories { maven { name = "TerraformersMC"; url = "https://maven.terraformersmc.com/" } }
dependencies {
    compileOnly  "com.terraformersmc:modmenu:21.0.0"
    localRuntime "com.terraformersmc:modmenu:21.0.0"
}
```

## Hardening ideas (suggestions, not observed in the repos)

- Read/write with an explicit `UTF_8` charset instead of `FileReader`/`FileWriter`.
- Write to a temp file and move it over the real one, so a crash mid-write cannot truncate the config.
- When the existing file fails to parse, rename it to `<modid>.json.bak` before writing defaults.
- Clamp numeric fields after loading (cooldowns, radii, thread counts).
- Server-side mods: a config read **once at startup** is a legitimate choice (MultiCore D-008).

## Checklist

- [ ] Defaults are in the field initialisers; file is created on first run.
- [ ] Bad JSON does not crash the game and does not destroy the old file.
- [ ] Mod loads with Mod Menu removed.
- [ ] `fabric.mod.json` has the `modmenu` entrypoint and a `suggests` entry.

## Provenance

`RocketWithSpearMod/.../config/ModConfig.java`, `compat/ModMenuIntegration.java`, `build.gradle`, `fabric.mod.json`; `ClientHarvestMod/.../AutoPlantConfig.java`; `Minecraft-MultyCore-Mod` decisions D-007 and D-008.
