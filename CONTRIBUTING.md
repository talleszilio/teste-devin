# Contributing Guide

## Branch Strategy

- `main` - Branch de produção (deploy automático)
- `develop` - Branch de desenvolvimento (staging)
- `feature/*` - Branches para novas funcionalidades
- `bugfix/*` - Branches para correções de bugs
- `hotfix/*` - Branches para correções urgentes em produção

## Workflow

1. Crie um branch a partir de `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/nova-funcionalidade
   ```

2. Faça suas alterações e commit:
   ```bash
   git add .
   git commit -m "feat: descrição da funcionalidade"
   ```

3. Push para o GitHub:
   ```bash
   git push origin feature/nova-funcionalidade
   ```

4. Crie um Pull Request para `develop`

5. Após aprovação, faça merge

6. Para deploy em produção, faça merge de `develop` para `main`

## Commit Message Convention

- `feat:` Nova funcionalidade
- `fix:` Correção de bug
- `docs:` Alteração na documentação
- `style:` Formatação, missing semicolons, etc
- `refactor:` Refatoração de código
- `test:` Adicionando testes
- `chore:` Atualização de build, etc

## Pull Request Process

1. Mantenha PRs pequenos e focados
2. Descreva claramente o que foi alterado
3. Referencie issues relacionadas
4. Adicione screenshots se for uma alteração visual
5. Aguarde review e aprovação antes do merge