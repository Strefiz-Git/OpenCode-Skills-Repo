---
name: discord-music-bot-architecture
description: "Structure a Discord music bot in TypeScript with discord.js v14 and @discordjs/voice: per-guild player manager, queue, extractors with fallback, slash and prefix commands, button panels, i18n locale files, persisted state, and running as a Windows service."
license: MIT
compatibility: opencode
metadata:
  category: discord
  source: ["Discord-Easy-Music-Bot"]
  origin: derived
  language: en
  scope: generic
---

# Discord music bot architecture

## Stack

discord.js 14, @discordjs/voice, @discordjs/opus, ffmpeg-static, play-dl, Prisma + SQLite.

## Layout

```
src/
  index.ts  client.ts  config.ts
  events/          # ready, interactionCreate, messageCreate, voiceStateUpdate
  commands/        # one file per command (slash + prefix share the same handler)
  music/
    PlayerManager.ts   # one player per guild (singleton map)
    Queue.ts  Track.ts  resolver.ts
    extractors/        # one file per source
  utils/               # LangManager (i18n), logger, embeds
locales/               # one JSON per language
prisma/schema.prisma
```

## Rules

- **Command contract**: each command exports `data`, `execute` and (optionally) a prefix alias, so slash and prefix behave identically.
- **One player per guild**: `PlayerManager.get(guildId)` creates on demand and destroys on disconnect.
- **Resolver -> extractor**: `resolver.ts` classifies the input (URL, search text, playlist) and picks an extractor.
- **Fallback chain**: if an extractor fails, log the reason and try the next; never silently swallow.
- **Button panels**: encode intent in `customId` as `action:guildId[:arg]` and parse it in one place.
- **i18n**: all user-facing text goes through `LangManager`; no literals in commands.
- **Persistence**: save the queue and settings with Prisma (see `prisma-sqlite-bot-state`); restore on `ready`.
- **Resilience**: handle voice disconnects, reconnect with backoff, and keep one failing track from killing the queue.
- **Deploy**: run as a Windows service (see `windows-service-nssm`).

## Checklist

- [ ] No command contains user-facing literals.
- [ ] Extractor failures are logged with the source and reason.
- [ ] Queue survives a restart.
- [ ] Secrets are in `.env`.

## Provenance

`Discord-Easy-Music-Bot` (34 commands, 9 languages, Prisma + SQLite, NSSM service).
