# Sistema de Agendamento para Manicure

Projeto de estudo full-stack, sem intenção de deploy imediato: o objetivo é treinar raciocínio lógico, fluxo web ponta a ponta, organização de código em camadas e escrita de testes automatizados, construindo uma aplicação real de agendamento para um salão de manicure.

## Sobre o projeto

O sistema tem dois papéis de usuário: **cliente** e **manicure** 

- A **cliente** se cadastra, escolhe uma manicure específica, seleciona o serviço (área do atendimento e tipo de acabamento) e solicita um horário disponível. O sistema calcula a duração e o preço automaticamente e valida se o serviço cabe no horário escolhido antes de enviar a solicitação.
- A **manicure** define seu próprio expediente, gerencia a fila de solicitações (aceitar, recusar, cancelar), marca atendimentos como concluídos e acompanha o histórico de cada cliente.

O núcleo de complexidade do projeto está no **motor de disponibilidade** (cálculo de horários livres a partir do expediente e dos agendamentos já aceitos) e na **máquina de estados** do agendamento (pendente → aceito/recusado → cancelado/concluído).

A documentação completa do projeto vive em `docs/`:
- `requisitos-funcionais.md` — requisitos, regras de negócio e limitações conhecidas do MVP
- `user-stories.md` — user stories com critérios de aceite, por épico
- `backlog.md` — as stories priorizadas por dependência técnica, mais o backlog de melhorias futuras
- `stack.md` — stack e roadmap resumido
- `roadmap-projeto-manicure.md` — o roadmap detalhado, sprint a sprint
- `decisoes.md` — registro das decisões técnicas tomadas ao longo do projeto, com o motivo

## Stack

| Camada | Tecnologia |
|---|---|
| Backend | Flask |
| Banco de dados | PostgreSQL (via Docker) |
| ORM | SQLAlchemy + Flask-Migrate (Alembic) |
| Autenticação | JWT (PyJWT) + hash de senha (Werkzeug) |
| Frontend | Vue 3 + TypeScript (Vite) |
| Estilização | HTML + CSS |
| Testes | pytest + Flask test client |
| Infraestrutura | Docker Compose |

Arquitetura em camadas no backend: **Router (Blueprints) → Controller → Service → Model**, com as regras de negócio mais densas (motor de disponibilidade, validação de CPF, máquina de estados) isoladas em funções puras, sem dependência de Flask ou banco.

## Estrutura do repositório

```text
manicure/
├── backend/
│   ├── app/
│   │   ├── routes/        → blueprints
│   │   ├── controllers/
│   │   ├── services/
│   │   ├── models/
│   │   ├── domain/        → regras puras (motor de disponibilidade, etc.)
│   │   └── auth/          → decorators de autenticação/autorização
│   ├── migrations/
│   ├── tests/
│   │   ├── unit/
│   │   ├── integration/
│   │   └── e2e/
│   └── requirements.txt
├── frontend/               → Vue 3 + TypeScript (a partir da Sprint 7)
├── docs/                   → requisitos, user stories, backlog, roadmap, decisões
└── docker-compose.yml
```

## Como iniciar

Pré-requisitos: Python 3.10+, Git, Docker e Node.js.

```bash
# clonar o repositório
git clone <url-do-repositorio>
cd manicure/backend

# criar e ativar o ambiente virtual
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# instalar as dependências
pip install -r requirements.txt

# configurar as variáveis de ambiente
cp .env.example .env             # depois, preencha os valores no .env

# rodar a suíte de testes
pytest

# subir a aplicação
flask --app app run --debug
```

A partir da Sprint 2, o banco PostgreSQL sobe com `docker compose up`, e a partir da Sprint 7 o frontend roda separadamente com `npm install` e `npm run dev` dentro de `frontend/`. As instruções desta seção são atualizadas ao final de cada sprint conforme novas dependências entram no projeto.

