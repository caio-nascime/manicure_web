# Backlog — Sistema de Agendamento para Manicure

Ordenado por dependência técnica: cada bloco depende dos anteriores para funcionar.

## 1. Autenticação

- **US01** — Como visitante, quero me cadastrar informando nome, email e senha, para poder solicitar agendamentos como cliente.
- **US02** — Como usuário cadastrado, quero fazer login com email e senha, para acessar minhas funcionalidades autenticadas.

## 2. Gestão do time

- **US03** — Como manicure, quero cadastrar outra manicure no sistema, para que ela também possa gerenciar sua própria agenda.

## 3. Agenda e serviços (manicure)

- **US15** — Como manicure, quero cadastrar, visualizar, editar e remover os dias e horários do meu expediente, para que as clientes só possam solicitar horários em que eu atendo.
- **US16** — Como manicure, quero alterar a duração e o preço de cada combinação de serviço, para manter a tabela de serviços atualizada.

## 4. Solicitação de agendamento

- **US04** — Como cliente, quero selecionar uma manicure específica ao solicitar um agendamento, para escolher com quem quero ser atendida.
- **US05** — Como cliente, quero selecionar a área do atendimento (pé, mão ou pé e mão) e o tipo de acabamento (normal ou gel), para definir o serviço que desejo.
- **US06** — Como cliente, quero solicitar um agendamento em uma data e horário específicos, para reservar meu atendimento.
- **US07** — Como cliente, quero ver o preço final do atendimento antes de enviar a solicitação, para saber quanto vou pagar sem que nenhum pagamento seja processado.

## 5. Gestão de solicitações (manicure)

- **US08** — Como manicure, quero visualizar as solicitações de agendamento pendentes, para decidir quais aceitar.
- **US09** — Como manicure, quero aceitar ou rejeitar uma solicitação, para confirmar ou recusar um atendimento.
- **US10** — Como manicure, quero cancelar um agendamento já aceito, podendo justificar o motivo, para liberar o horário quando necessário.

## 6. Acompanhamento da cliente

- **US11** — Como cliente, quero acompanhar o status dos meus agendamentos, para saber se foram aceitos, recusados, cancelados ou concluídos.

## 7. Gestão de clientes e histórico

- **US12** — Como manicure, quero visualizar todos os clientes cadastrados, para ter uma visão geral da minha base de clientes.
- **US13** — Como manicure, quero marcar um agendamento aceito como concluído, para registrar que o atendimento foi realizado.
- **US14** — Como manicure, quero ver o número total de atendimentos concluídos de cada cliente, para acompanhar o histórico de cada uma.

---

## Backlog de melhorias futuras (fora do MVP)

- Auditoria de atendimentos dos últimos 30 dias (atendidos e cancelados), com filtro de busca
- Dashboard de faturamento do mês + top clientes por quantidade de atendimentos
- Cartão fidelidade: desconto/brinde após X atendimentos
- Fluxo de agendamento "sem preferência de manicure", com estratégia de atribuição automática (ex: primeira disponível, menos ocupada, round-robin)
- Revalidação automática de sobreposição ao aceitar uma solicitação (resolve a limitação LIM01)
- Papel de administrador, responsável por cadastrar novas manicures, visualizar todas as agendas e controlar a tabela de preços (resolve a limitação LIM02)
