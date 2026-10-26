---
name: godotsteam-lobby-multiplayer
description: "Add Steam lobbies, friends, invites, voice chat and P2P multiplayer to a Godot 4 game with GodotSteam (GDExtension) and SteamMultiplayerPeer, including host migration and network performance. Use when integrating Steam, creating or joining lobbies, spawning networked players, or when callbacks never fire."
license: MIT
compatibility: opencode
metadata:
  category: godot
  source: ["Vivo-Sprint"]
  origin: derived
  language: en
  scope: generic
---

# GodotSteam lobby + multiplayer (Godot 4)

Condensed from `Vivo-Sprint/guia_godotsteam.md` (the full guide is ~90 KB: read it for lobby passwords, filters, voice and proximity chat). This skill keeps the decisions and the traps.

## Setup

1. Download the **GDExtension** release that matches your Godot 4 version and extract it into the project. The `Steam` singleton is registered by the extension (no Autoload needed for it).
2. App ID: use `480` (Spacewar) for tests. Set it in Project Settings > Steam > Initialization, as an argument to the init call, through `SteamAppId`/`SteamGameId` environment variables in an autoload `_init()`, or with a `steam_appid.txt`. **Remove `steam_appid.txt` from the shipped build.**
3. Put everything Steam in one Autoload (`steamworks.gd`) that calls `Steam.steamInitEx()` and reads `getSteamID()` / `getPersonaName()`.
   - `status` 0 = ok, 1 = other failure, 2 = could not reach Steam (client not running), 3 = Steam client outdated.

## Callbacks

Steam answers asynchronously through signals. Pump them one of three ways: enable **Embed Callbacks** in Project Settings, pass `true` as the second argument to `steamInitEx()`, or call `Steam.run_callbacks()` in `_process()`. That node must **never pause**.

## Networking

- Use **`SteamMultiplayerPeer`** with Godot's high-level multiplayer (RPCs, `MultiplayerSpawner`, `MultiplayerSynchronizer`).
- Host: after the lobby is created, `peer.create_host(0)`, `peer.server_relay = true`, `multiplayer.set_multiplayer_peer(peer)`.
- Client: after joining, `peer.create_client(Steam.getLobbyOwner(lobby_id), 0)`, `server_relay = true`.
- `server_relay = true` routes everything through the server: simpler topology and fewer problems for late joiners.
- The server is always peer id 1. Authority is per node (`set_multiplayer_authority()`).
- Dedicated-server builds of GodotSteam did not support `MultiplayerPeer` at the time of the guide.

## Performance

- `unreliable_ordered` for frequent state (position), `reliable` only for one-off events.
- Lower `MultiplayerSynchronizer.replication_interval` (for example 0.05 s) and **interpolate on the client**.
- Send input state, not resulting positions, when the server owns physics.
- Filter by relevance/distance (`set_visibility_for`) so far-away players are not replicated; this also limits wallhacks.
- A network tick rate of 20-30 Hz is usually enough.

## Checklist

- [ ] Steam client running when testing; `steamInitEx` status checked.
- [ ] Callbacks pumped from a node that never pauses.
- [ ] Host and client both set `server_relay`.
- [ ] `steam_appid.txt` removed from release builds.
- [ ] Two real Steam accounts used for the final multiplayer test.

## Provenance

`Vivo-Sprint/guia_godotsteam.md`. Values and API names are as in the guide; verify them against the installed GodotSteam version.
