# Contribuir

## Adicionar uma skill

1. `python scripts/new-skill.py <categoria> <nome> "<descrição>"`.
2. Preenche o `SKILL.md`: quando usar, passos, armadilhas, checklist, proveniência.
3. `python scripts/validate.py` (tem de dar OK) e `python scripts/build-catalog.py`.
4. Commit em Conventional Commits, em português (PT-PT): `feat(skills): adicionar <nome>`.

## Regras

- Reutilizar antes de escrever: se já existe uma skill parecida, melhora-a em vez de duplicar.
- `description` diz **quando** usar (gatilhos concretos), não só o que faz.
- Skills importadas: não alterar o corpo; correções vão para o repo de origem e reimportam-se.
- Sem segredos, sem `{{placeholders}}` esquecidos, sem `TODO` que não esteja num `TODO.md`.
- Ficheiros em UTF-8 **sem BOM** e fins de linha LF.
- Prefixos de commit em inglês (`feat`, `fix`, `docs`, `chore`, `refactor`); o resto em PT-PT. Um commit por unidade lógica; nunca misturar refatoração com mudança de comportamento.
