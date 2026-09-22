# Stack do Projeto — Sistema de Agendamento para Manicure

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Flask |
| Banco de dados | PostgreSQL (via Docker) |
| ORM | SQLAlchemy |
| Frontend | Vue 3 + TypeScript |
| Estilização | HTML + CSS |
| Testes | pytest + Flask test client |

## Papéis de usuário

- **Cliente**
- **Manicure** (único papel administrativo — sem papel separado de admin/dona do estabelecimento)

## Roadmap

1. Modelagem do banco (models + migrations) e autenticação, já em PostgreSQL via Docker
2. CRUD de `Service` e `WorkingHours` — validar cada endpoint isoladamente (Postman/Insomnia/Swagger) antes de qualquer tela
3. Motor de disponibilidade (camada de Service) — testado isolado via API, antes de existir tela
4. Endpoints de solicitação e aceitar/recusar/cancelar, com a máquina de estados definida nas Regras de Negócio
5. Frontend em Vue 3, começando pelas telas mais simples (login/cadastro) antes das telas com mais estado (seleção de horário + serviço)
6. Landing page estática, apenas para apresentar o salão e atrair clientes (por último)

## Testes

Objetivo adicional do projeto: treinar produção de testes (motivado por uma responsabilidade equivalente em um projeto em grupo).

- **Unitários** (pytest) — funções puras sem I/O: motor de disponibilidade, cálculo de duração/preço (RN02)
- **Integração** — Service + Model juntos contra um banco real (ex: criação de agendamento respeitando RN01)
- **Ponta a ponta (E2E)** — via Flask test client, chamando os endpoints e conferindo status code + resposta
- Cada Regra de Negócio (RN01-RN15) deve gerar ao menos um teste de caminho feliz e um de caminho de falha
- Banco de teste deve ser separado do banco de desenvolvimento (ex: serviço `db_test` no mesmo Docker Compose), para não corromper dados usados manualmente durante o desenvolvimento
- Testes de cada parte devem ser escritos junto com a implementação daquela parte no roadmap, não deixados para uma fase final

## Observações

- Projeto de estudo, sem intenção original de deploy — mas a possibilidade de produção futura passou a ser considerada, o que motivou adotar PostgreSQL desde já em vez de SQLite.
- Postgres + Docker e Vue 3 foram escolhidos deliberadamente como desafio extra de aprendizado, sem pressa de prazo — o projeto pode levar meses.
- Vue 3 será usado desde a primeira tela (não como migração posterior de um frontend em TypeScript vanilla).
- Recomendação mantida: validar cada endpoint do backend isoladamente antes de consumi-lo em um componente Vue, para isolar se um problema está na API ou na camada de reatividade do frontend.
- Caso a produção real venha a se concretizar, pontos ainda não cobertos pelo escopo atual incluem: proteção contra condição de corrida em escritas concorrentes, segurança adicional (CSRF, rate limiting, HTTPS), conformidade com a LGPD, servidor de produção (Gunicorn/uWSGI + Nginx).
