# User Stories — Sistema de Agendamento para Manicure

## Épico: Autenticação

**US01** — Como visitante, quero me cadastrar informando nome completo, email, celular, senha, confirmação de senha, apelido (opcional) e instagram (opcional), para poder solicitar agendamentos como cliente.

Critérios de aceite:
- Dado um email ainda não cadastrado, quando envio os dados válidos, então minha conta é criada e recebo confirmação (201)
- Dado um email já cadastrado, quando tento me cadastrar novamente, então recebo erro de conflito (409), sem criar duplicata
- Dado que a senha é enviada, quando armazenada, então nunca é salva em texto puro (sempre com hash)
- Dado que a senha e a confirmação de senha são diferentes, quando envio o cadastro, então recebo erro de validação e a conta não é criada
- Dado um celular fora do formato esperado, quando envio o cadastro, então recebo erro de validação
- Dado que não informei apelido nem instagram, quando envio o cadastro, então a conta é criada normalmente (campos opcionais)
- Dado qualquer cadastro feito pela tela pública, quando a conta é criada, então ela é sempre do tipo cliente, mesmo que a requisição tente informar outro papel (RN11)
- As validações são feitas por lógica da própria aplicação, sem consulta a serviços externos

**US02** — Como usuário cadastrado, quero fazer login com email e senha, para acessar minhas funcionalidades autenticadas.

Critérios de aceite:
- Dado um email e senha corretos, quando envio a requisição de login, então recebo um token JWT válido
- Dado um email ou senha incorretos, quando tento logar, então recebo erro de autenticação (401), sem revelar qual campo está errado

---

## Épico: Gestão do time

**US03** — Como manicure, quero cadastrar outra manicure no sistema informando nome completo, cpf, email, data de nascimento, senha e confirmação de senha, para que ela também possa gerenciar sua própria agenda.

Critérios de aceite:
- Dado que estou autenticada como manicure, quando cadastro uma nova manicure, então ela passa a existir com login próprio
- Dado que estou autenticada como cliente, quando tento cadastrar uma nova manicure, então recebo erro de autorização (403 — o sistema sabe quem sou, mas não tenho permissão)
- Dado que não estou autenticada, quando tento cadastrar uma nova manicure, então recebo erro de autenticação (401 — o sistema não sabe quem está fazendo a requisição)
- Dado um CPF com dígitos verificadores inválidos, quando envio o cadastro, então recebo erro de validação (validação por algoritmo, sem consulta externa)
- Dado um CPF ou email já cadastrados, quando envio o cadastro, então recebo erro de conflito (409), sem criar duplicata
- Dado uma data de nascimento futura, quando envio o cadastro, então recebo erro de validação
- Dado que a senha e a confirmação de senha são diferentes, quando envio o cadastro, então recebo erro de validação
- A primeira manicure do sistema é criada por bootstrap: um script de código que popula o banco, sem inserção manual pelo DBeaver (RN11)

---

## Épico: Agenda e serviços (manicure)

**US15** — Como manicure, quero cadastrar, visualizar, editar e remover os dias e horários do meu expediente, para que as clientes só possam solicitar horários em que eu atendo.

Critérios de aceite:
- Dado que estou autenticada como manicure, quando defino o horário de início e de fim de um dia da semana, então esse dia passa a fazer parte do meu expediente
- Dado um horário de início igual ou posterior ao horário de fim, quando tento salvar, então recebo erro de validação
- Dado um dia da semana que já tem expediente cadastrado, quando tento cadastrar outro para o mesmo dia, então a ação é bloqueada (um expediente por dia da semana)
- Dado um dia removido do meu expediente, quando uma cliente consulta os horários desse dia, então nenhum horário é oferecido (RN12)
- Dado que estou autenticada como manicure, quando tento alterar o expediente de outra manicure, então a ação é bloqueada (RN09)

**US16** — Como manicure, quero alterar a duração e o preço de cada combinação de serviço, para manter a tabela de serviços atualizada.

Critérios de aceite:
- Dado uma combinação existente de área e acabamento, quando altero sua duração ou seu preço, então os novos valores passam a valer para as próximas solicitações (RN02)
- Dado agendamentos já solicitados, quando altero o preço de um serviço, então o preço registrado nesses agendamentos não muda (RN14)
- Dado que sou qualquer manicure autenticada, quando altero um preço, então a alteração vale para todo o salão (RN15, LIM02)
- Dado uma duração menor ou igual a zero ou um preço negativo, quando tento salvar, então recebo erro de validação
- Dado que estou autenticada como cliente, quando tento alterar um serviço, então recebo erro de autorização (403)

---

## Épico: Solicitação de agendamento

**US04** — Como cliente, quero selecionar uma manicure específica ao solicitar um agendamento, para escolher com quem quero ser atendida.

Critérios de aceite:
- Dado que existem manicures cadastradas, quando solicito um agendamento, então devo obrigatoriamente escolher uma delas
- Dado que nenhuma manicure foi selecionada, quando tento enviar a solicitação, então ela é rejeitada

**US05** — Como cliente, quero selecionar a área do atendimento (pé, mão ou pé e mão) e o tipo de acabamento (normal ou gel), para definir o serviço que desejo.

Critérios de aceite:
- Dado que escolhi uma área e um acabamento, quando ambos são válidos, então o sistema identifica a combinação correspondente de duração e preço (RN02)
- Dado que a combinação de área e acabamento não existe, quando tento prosseguir, então recebo um erro

**US06** — Como cliente, quero solicitar um agendamento em uma data e horário específicos, para reservar meu atendimento.

Critérios de aceite:
- Dado um horário livre na agenda da manicure escolhida, quando envio a solicitação, então ela é registrada com status "pendente"
- Dado um horário que já sobrepõe um agendamento aceito da mesma manicure, quando tento solicitar, então a solicitação é rejeitada (RN01)
- Dado que a duração do serviço escolhido não cabe no intervalo disponível, quando tento solicitar, então recebo um alerta e a solicitação não é enviada (RN03)
- Dado o expediente da manicure escolhida, quando consulto os horários disponíveis, então os horários de início são oferecidos em intervalos de 15 minutos (RN10)
- Dado um horário fora do expediente da manicure, quando tento solicitar, então a solicitação é rejeitada (RN12)
- Dado uma data ou horário no passado, quando tento solicitar, então a solicitação é rejeitada

**US07** — Como cliente, quero ver o preço final do atendimento antes de enviar a solicitação, para saber quanto vou pagar sem que nenhum pagamento seja processado.

Critérios de aceite:
- Dado que selecionei manicure, área e acabamento, quando o preço é calculado, então ele é exibido antes do botão de envio
- Dado que o preço foi exibido, quando a solicitação é enviada, então nenhuma cobrança ou processamento de pagamento ocorre
- Dado que solicitei um agendamento pelo preço X, quando a tabela de preços é alterada depois para Y, então meu agendamento continua registrado com o preço X (RN14)

---

## Épico: Gestão de solicitações (manicure)

**US08** — Como manicure, quero visualizar as solicitações de agendamento pendentes, para decidir quais aceitar.

Critérios de aceite:
- Dado que existem solicitações pendentes, quando acesso a lista, então elas aparecem ordenadas por ordem de envio
- Dado que existem solicitações para outras manicures, quando acesso a lista, então vejo apenas as solicitações da minha agenda (RN09)

**US09** — Como manicure, quero aceitar ou rejeitar uma solicitação, para confirmar ou recusar um atendimento.

Critérios de aceite:
- Dado uma solicitação pendente, quando eu a aceito, então seu status muda para "aceito" e o horário fica reservado
- Dado uma solicitação pendente, quando eu a rejeito, então seu status muda para "rejeitado" e o horário permanece livre
- Dado uma solicitação que já não está mais pendente, quando tento aceitar ou rejeitar, então a ação é bloqueada
- Dado uma solicitação da agenda de outra manicure, quando tento aceitá-la ou rejeitá-la, então a ação é bloqueada (RN09)
- Limitação do MVP (LIM01): ao aceitar, o sistema não revalida sobreposição com outra solicitação já aceita; havendo duas pendentes no mesmo horário, a manicure aceita a primeira e recusa a segunda

**US10** — Como manicure, quero cancelar um agendamento já aceito, podendo justificar o motivo, para liberar o horário quando necessário.

Critérios de aceite:
- Dado um agendamento aceito, quando eu o cancelo, então posso incluir uma mensagem de justificativa, que é opcional (RN13)
- Dado um agendamento aceito, quando eu o cancelo sem justificativa, então o cancelamento é realizado normalmente
- Dado um agendamento da agenda de outra manicure, quando tento cancelá-lo, então a ação é bloqueada (RN09)
- Dado um agendamento cancelado, quando verifico a agenda, então o horário correspondente volta a aparecer como disponível (RN07)

---

## Épico: Acompanhamento da cliente

**US11** — Como cliente, quero acompanhar o status dos meus agendamentos, para saber se estão pendentes, agendados (aceitos), recusados, cancelados ou concluídos.

Critérios de aceite:
- Dado que tenho agendamentos solicitados, quando acesso minha área, então vejo o status atual de cada um
- Dado que um agendamento muda de status, quando consulto novamente, então o status exibido está atualizado
- Dado um agendamento cancelado com justificativa, quando consulto meus agendamentos, então vejo a justificativa informada pela manicure (RN13)
- Dado que existem agendamentos de outras clientes, quando consulto meus agendamentos, então vejo apenas os meus

---

## Épico: Gestão de clientes e histórico

**US12** — Como manicure, quero visualizar todos os clientes cadastrados, para ter uma visão geral da minha base de clientes.

Critérios de aceite:
- Dado que existem clientes cadastrados, quando acesso a lista, então todos aparecem, independentemente de terem agendamentos ativos

**US13** — Como manicure, quero marcar um agendamento aceito como concluído, para registrar que o atendimento foi realizado.

Critérios de aceite:
- Dado um agendamento com status "aceito", quando o marco como concluído, então seu status muda para "concluído" (RN04)
- Dado um agendamento que não está com status "aceito", quando tento concluí-lo, então a ação é bloqueada (RN04)
- Dado um agendamento já concluído, quando tento alterá-lo, então a alteração é bloqueada (RN06)
- Dado um agendamento da agenda de outra manicure, quando tento concluí-lo, então a ação é bloqueada (RN09)

**US14** — Como manicure, quero ver o número total de atendimentos concluídos de cada cliente, para acompanhar o histórico de cada uma.

Critérios de aceite:
- Dado uma cliente com atendimentos concluídos, quando consulto seu histórico, então vejo a contagem atual, calculada a partir dos agendamentos concluídos (RN05)
- Dado que um novo agendamento é concluído, quando consulto o histórico novamente, então a contagem já reflete essa mudança, sem necessidade de nenhuma ação manual de atualização
