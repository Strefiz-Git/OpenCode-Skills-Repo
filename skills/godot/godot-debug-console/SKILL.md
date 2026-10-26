---
name: godot-debug-console
description: "Plan and build a reusable in-game command console for any Godot 4 project: Autoload with CanvasLayer UI, command registry and parser, autocomplete and history, per-scene command cleanup, release-build protection and multiplayer-safe commands. Use when adding a debug console or cheats to a Godot game."
license: MIT
compatibility: opencode
metadata:
  category: godot
  source: ["Vivo-Sprint"]
  origin: derived
  language: en
  scope: generic
---

# Godot debug console

Condensed from `Vivo-Sprint/plano_consola_godot.md`. Goal: copy one `console/` folder between games and only rewrite the game-specific commands.

## Architecture

```
Console (Autoload)
 |- ConsoleUI (CanvasLayer, high layer)
 |    |- Panel, RichTextLabel (output), LineEdit (input)
 |- CommandRegistry (name -> Callable / Command resource)
 |- CommandParser (text -> name + args, respects "quotes")
```

```
res://addons/console/
  console.gd  console_ui.tscn  command.gd
  commands/base_commands.gd   # /help /clear /quit /echo
  commands/debug_commands.gd  # game-specific: /god /tp /give /fps
```

## Rules

1. **Register `console_ui.tscn` as an Autoload** (named `Console`). A console that lives inside `Main.tscn` disappears on every scene change.
2. Any script registers commands with `Console.register_command(...)`; the console never edits per scene code.
3. A scene script that registers a command **must unregister it in `_exit_tree()`** (`Console.unregister_command("give")`), otherwise the registry keeps a Callable to a freed object.
4. Parse `/command arg1 "arg with spaces"` with a small tokenizer that honours quotes.
5. `/help` lists commands from the registry, never from a hard-coded list.
6. If opening the console pauses the game, set `process_mode = PROCESS_MODE_ALWAYS` and reset `paused = false` on scene transitions.
7. Plan each command on a card first: name, arguments, affected system, validations.

## Release protection

- Register dangerous commands only if `OS.is_debug_build()`, or
- gate them with a `console_enabled` flag, or
- require `/unlock <password>` before cheats work.

## Multiplayer (GodotSteam)

World-changing commands (spawn, give, set) run only when `multiplayer.is_server()` and propagate by `@rpc("authority", "call_local")`. Local cosmetic commands (`/fps`, `/clear`) need no RPC. A `/whoami` command printing `multiplayer.get_unique_id()` helps debug sessions.

## Implementation order

1. UI scene. 2. Autoload with toggle key. 3. Parser. 4. Register/execute. 5. `/help /clear /echo /quit`. 6. History (up/down). 7. Autocomplete (Tab). 8. Game commands. 9. Release protection. 10. Multiplayer adaptation.

## Checklist

- [ ] `toggle_console` action in the Input Map, tested on the real keyboard layout.
- [ ] Works in at least two different scenes without duplicating.
- [ ] Closed console does not swallow input (`mouse_filter`, `visible`).
- [ ] Sensitive commands protected in release builds.

## Provenance

`Vivo-Sprint/plano_consola_godot.md` (written as a generic plan reusable in UniCooking).
