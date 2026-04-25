

# conseguir fazer:

--status success
--status failed
--year 2024
--month 3


# todos os lancamentos
uv run python -m app.main

# somente falhas 
uv run python -m app.main --status failed

# somente sucessos em 2022
uv run python -m app.main --status success --year 2022

# falhas em março
uv run python -m app.main --status failed --month 3


# Como verificar pelo banco

docker exec -it spacex_postgres psql -U postgres -d spacex_bot
\dt
SELECT * FROM launches LIMIT 10;

# report em html ou dashboard
# testes automatizados
# github actions
# scheduler diario


# Melhorias

- Expandir para os outros endpoints:
   - rockets
   - capsules