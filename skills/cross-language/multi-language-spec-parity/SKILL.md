---
name: multi-language-spec-parity
description: "Implement the same format or algorithm in several languages or stacks (C#, Java, Kotlin, Python, web) and keep them byte-identical using one written spec, shared test vectors from a reference implementation, and an independent decoder as referee."
license: MIT
compatibility: opencode
metadata:
  category: cross-language
  source: ["QrCodeGenerator"]
  origin: derived
  language: en
  scope: generic
---

# Multi-language spec parity

## Rule: one spec, N clients

```
docs/<SPEC>.md          # the written truth
spec/vectors.json       # shared test vectors
spec/generate-vectors.py
<stack>/                # one folder per implementation
```

## Workflow

1. Fix the **spec** first.
2. Regenerate the vectors from the reference implementation.
3. Propagate to the other stacks (suggested order: Java -> mobile -> C# -> Python -> Go).
4. Run every stack's tests against the same vectors.

Never hand-edit generated files; change the generator.

## Tests

- **Level 1, structural**: output matches the vectors byte for byte.
- **Level 2, decode**: an independent reader (ZXing for QR/barcodes) decodes what each implementation produced.
- Validate against official examples where the standard publishes them.

## Practical rules

- Keep a table of commands per stack in the README.
- Pin toolchains (Java, Gradle, Python versions).
- Every bug gets a regression vector before it is fixed.

## Checklist

- [ ] Spec changed before code.
- [ ] Vectors regenerated and committed.
- [ ] All stacks green on the same vectors.
- [ ] Independent decoder used at least once.

## Provenance

`QrCodeGenerator` (5 stacks, 1107 tests).
