# Requisitos Funcionais — Sistema de Agendamento para Manicure

## Cliente

- **RF01** — O sistema deve permitir que um novo usuário se cadastre.
- **RF02** — O sistema deve permitir que um usuário faça login.
- **RF03** — O sistema deve permitir que o cliente solicite um agendamento (data e horário).
- **RF04** — O sistema deve permitir que a cliente selecione a área do atendimento (pé, mão ou pé e mão) e o tipo de acabamento (esmaltação normal ou gel) ao solicitar um agendamento.
- **RF05** — O sistema deve permitir que a cliente selecione uma manicure específica ao solicitar um agendamento (seleção obrigatória).
- **RF06** — O sistema deve exibir o preço final do atendimento à cliente antes do envio da solicitação, sem processar pagamento.
- **RF07** — O sistema deve permitir que a cliente acompanhe o status de seus agendamentos (pendente, agendado/aceito, recusado, cancelado ou concluído).

## Manicure

- **RF08** — O sistema deve permitir que uma manicure cadastre novas manicures no sistema.
- **RF09** — O sistema deve permitir que uma manicure visualize as solicitações de agendamento.
- **RF10** — O sistema deve permitir que uma manicure aceite ou rejeite um agendamento.
- **RF11** — O sistema deve permitir que uma manicure cancele um agendamento (será possível adicionar uma mensagem justificando o cancelamento).
- **RF12** — O sistema deve permitir que uma manicure visualize todos os clientes cadastrados.
- **RF13** — O sistema deve permitir que a manicure marque um agendamento aceito como concluído.
- **RF14** — O sistema deve exibir, para a manicure, o número total de atendimentos concluídos de cada cliente.
- **RF15** — O sistema deve permitir que a manicure cadastre, visualize, edite e remova os dias e horários do seu expediente de atendimento.
- **RF16** — O sistema deve permitir que a manicure altere a duração e o preço de cada combinação de serviço (área × acabamento).

## Regras de Negócio

- **RN01** — Vinculada ao RF03: o sistema não deve permitir a criação de um agendamento cujo intervalo de horário sobreponha um agendamento já aceito para a mesma manicure.
- **RN02** — Vinculada ao RF04 e RF16: a duração e o preço do atendimento são determinados pela combinação específica entre área e tipo de acabamento selecionados (não por soma nem fórmula entre os dois fatores).
- **RN03** — Vinculada ao RF03 e RN01: o sistema não deve permitir o envio da solicitação se a duração do serviço (RF04) não couber no intervalo de horário disponível.
- **RN04** — Vinculada ao RF13: um agendamento só pode ser marcado como concluído se estiver no status "aceito".
- **RN05** — Vinculada ao RF14: o número de atendimentos de um cliente deve refletir sempre o estado atual dos agendamentos concluídos, sem depender de um valor armazenado separadamente.
- **RN06** — Vinculada ao RF13: um agendamento marcado como concluído é definitivo e não pode retornar a um status anterior.
- **RN07** — Vinculada ao RF11: ao cancelar um agendamento, o intervalo de horário correspondente deve voltar a ficar disponível para novas solicitações.
- **RN08** — Vinculada ao RF02: em caso de falha no login, o sistema não deve revelar qual campo (email ou senha) está incorreto.
- **RN09** — Vinculada ao RF09, RF10, RF11, RF13 e RF15: a manicure só pode visualizar e agir sobre a própria agenda, as próprias solicitações e o próprio expediente.
- **RN10** — Vinculada ao RF03: os horários de início oferecidos à cliente seguem intervalos de 15 minutos.
- **RN11** — Vinculada ao RF01 e RF08: o cadastro público cria exclusivamente contas de cliente; contas de manicure só são criadas por uma manicure autenticada ou pelo bootstrap inicial do sistema (script de código que popula o banco, sem inserção manual).
- **RN12** — Vinculada ao RF03 e RF15: só podem ser solicitados horários dentro do expediente da manicure escolhida.
- **RN13** — Vinculada ao RF11 e RF07: a justificativa de cancelamento é opcional; quando informada, fica visível para a cliente.
- **RN14** — Vinculada ao RF06 e RF16: o preço exibido à cliente no momento da solicitação é registrado no agendamento e é o que vale para o pagamento; alterações posteriores na tabela de preços não afetam agendamentos já solicitados.
- **RN15** — Vinculada ao RF16: a tabela de duração e preço é única para o salão (não há preço por manicure), e qualquer manicure pode alterá-la.

## Limitações conhecidas do MVP

- **LIM01** — Vinculada ao RF10 e RN01: ao aceitar uma solicitação, o sistema não revalida se ela se sobrepõe a outra solicitação aceita no mesmo horário. Duas solicitações pendentes podem existir para o mesmo horário; no MVP, a manicure resolve manualmente (aceita a primeira e recusa a segunda). A revalidação automática fica para uma versão futura.
- **LIM02** — Vinculada ao RF16 e RN15: qualquer manicure pode alterar a tabela de preços do salão. É uma limitação de segurança consciente; o controle passará a um papel de administrador em uma versão futura.
