# 🚀 SpaceX Bot

Automação em Python que consome a API pública da SpaceX, sincroniza dados no banco, gera relatórios e executa testes automatizados.

---

# ✨ O que o projeto faz

- Consulta dados reais da API da SpaceX
- Salva lançamentos no PostgreSQL
- Filtra lançamentos por status, ano e mês
- Gera relatório HTML 
- Testes automatizados
- CI/CD com GitHub Actions

---

# 🧠 Stack

- Python
- Typer (CLI)
- PostgreSQL
- Pandas
- Plotly
- Pytest
- Playwright
- GitHub Actions
- Docker

---
# 📁 Estrutura

```text
spacex-bot
├── app/
|   ├── cli/
|   ├── clients/
|   ├── core/
|   ├── models/
|   ├── repositories/
|   ├── services/
|   └── main.py
├── tests/
├── reports/
```
---

# ▶️ Como rodar

## Instalar dependências
```bash
pip install -r requirements.txt
```
## Sincronizar banco
```bash
sync
docker compose up -d
run python -m app.main sync

```
## Pegar todos os lançamentos
```bash
uv run python -m app.main run
```

## Pegar lançamentos com sucesso em ano e mês especifico
```bash
uv run python -m app.main run --status success --month 9 --year 2020
```

## 🧪 Testes automatizados
```bash
uv run pytest -v
```
