---
name: prisma-sqlite-bot-state
description: "Model per-guild or per-user state for a Node/TypeScript bot with Prisma and SQLite: settings, a persisted queue, liked items, upserts and cascade deletes."
license: MIT
compatibility: opencode
metadata:
  category: database
  source: ["Discord-Easy-Music-Bot"]
  origin: derived
  language: en
  scope: generic
---

# Prisma + SQLite bot state

## Schema shape

```prisma
model Guild {
  id          String       @id
  language    String       @default("en")
  queue       QueueTrack[]
}

model QueueTrack {
  id       Int    @id @default(autoincrement())
  guildId  String
  position Int
  url      String
  title    String
  guild    Guild  @relation(fields: [guildId], references: [id], onDelete: Cascade)
}

model LikedTrack {
  id      Int    @id @default(autoincrement())
  userId  String
  url     String
  title   String
  @@unique([userId, url])
}
```

## Rules

- **Upsert on first write**: `prisma.guild.upsert(...)` so a guild row always exists before its children.
- **Cascade deletes** so removing a guild removes its queue.
- npm scripts: `prisma:generate`, `prisma:push`, `start`.
- SQLite file paths are **relative to the schema file**.
- Back up `database.db` before schema changes.
- One `PrismaClient` per process.
- Save the queue on change and restore it on the `ready` event.

## Checklist

- [ ] `prisma generate` and `prisma db push` run clean on a fresh clone.
- [ ] Unique constraints prevent duplicate liked items.
- [ ] Restart restores the queue.

## Provenance

`Discord-Easy-Music-Bot`.
