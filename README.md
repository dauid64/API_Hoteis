<h1>Documentação da REST API dos Hoteis</h1>

Este documento especifica como utilizar os recursos disponíveis no REST API de Reserva e Comparação de Hotéis, as formas de se realizar uma requisição e suas possíveis respostas.

<h2>1. Consultar Hotéis</h2>
<h3>Requisição</h3>

Requisição para listar todos os hotéis do sistema, podendo opcionalmente receber filtros personalizados via path, de forma que se o cliente não definir nenhum parâmetro de consulta (nenhum filtro), os parâmetros receberão os valores padrão.

<p>⦁	Possíveis parâmetros de consulta</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⦁	cidade ⇒ Filtrar hotéis pela cidade escolhida. Padrão: Nulo </p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⦁	estrelas_min ⇒ Avaliações mínimas de hotéis de 0 a 5. Padrão: 0</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⦁	estrelas_max ⇒ Avaliações máximas de hotéis de 0 a 5. Padrão: 5</p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⦁	diaria_min ⇒ Valor mínimo da diária do hotel de R$ 0 a R$ 10.000,00. Padrão: 0 </p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⦁	diaria_max ⇒ Valor máximo da diária do hotel de R$ 0 a R$ 10.000,00. Padrão: 10000 </p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⦁	limit ⇒ Quantidade máxima de elementos exibidos por página. Padrão: 50 </p>
  <p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⦁	offset ⇒ Quantidade de elementos pular (geralmente múltiplo de limit). Padrão: 0 </p>
