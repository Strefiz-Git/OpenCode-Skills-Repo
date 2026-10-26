---
name: discord-server-template-from-html
description: "Turn a pasted Discord sidebar HTML dump into a server-template JSON for a Discord server-builder bot, and know the limits of what a template can reproduce."
license: MIT
compatibility: opencode
metadata:
  category: discord
  source: ["Discord-server-builder-bot"]
  origin: derived
  language: en
  scope: generic
---

# Discord server template from HTML

## Recipe

1. Save the pasted sidebar HTML as `server-template-<slug>-html.txt` in the bot repo.
2. Run `python convert.py` to generate the template JSON.
3. Read the generated JSON: check category order, channel names and channel types.
4. Tell the user which parts could not be reproduced (see limits).
5. Apply with the bot's `/setup-server` command on a test server first.

## How the converter reads the HTML

- Names come from each item's `aria-label`.
- The **channel type** (text, voice, forum, announcement) comes from the icon's tooltip, not from the name.

## Limits of a template

- A truncated HTML dump produces a truncated template; ask for the full sidebar.
- Private channels lose their lock: permissions are not in the HTML.
- Text and forum channel names are lowercased by Discord.
- Forum channels only accept names that are valid text-channel names.
- Roles, permissions, emojis and messages are not reproducible from a sidebar.

## Checklist

- [ ] Generated JSON reviewed by a human before applying.
- [ ] Test server used first.
- [ ] Limits communicated to the user.

## Provenance

`Discord-server-builder-bot` (`convert.py`, `/setup-server`).
