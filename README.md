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
  
![image](https://user-images.githubusercontent.com/94979678/203685476-0c738b71-8ef4-4358-a9ef-333eca19d910.png)
 
<h3>Resposta</h3>
<p>Como resposta, obtém-se uma lista de hotéis que se enquadram nos filtros da requisição acima:</p>
 
![image](https://user-images.githubusercontent.com/94979678/203685507-7335b3e9-aba5-4c66-aa80-7c87357fc596.png)
 
<h3>Requisição</h3>
<p>Requisição exemplo de quando o usuário pesquisar por um hotel que não existe.</p>
 
 ![image](https://user-images.githubusercontent.com/94979678/203690400-053a613a-a14d-4f7d-a5bc-05d039e4cab4.png)

<h3>Resposta</h3>
<p>Como resposta, obtém-se uma mensagem de erro, dizendo que o hotel não foi encontrado.</p>

![image](https://user-images.githubusercontent.com/94979678/203690441-46e68ad9-4595-45b6-ab15-f9fbaa6d278b.png)
![image](https://user-images.githubusercontent.com/94979678/203690990-0ff6bd41-5ae3-4a13-bd93-0e575f70540e.png)

<h2>2. Cadastro de Usuário</h2>

<h3>Requisição</h3>
<p>Exemplo de Requisição cadastrar um novo usuário.</p>

![image](https://user-images.githubusercontent.com/94979678/203690596-dda58aac-a761-48d1-8744-7eeadabff393.png)

![image](https://user-images.githubusercontent.com/94979678/203690660-62f224bc-9200-44e5-8e62-4a2b6a5a5ef0.png)

![image](https://user-images.githubusercontent.com/94979678/203690716-ab411b33-645e-44ab-a52e-54fbc01c34d6.png)

<h3>Resposta</h3>
<p>Como resposta, obtém-se uma mensagem de sucesso informado que usuário foi criado, e status code 201 Created (Criado).</p>

![image](https://user-images.githubusercontent.com/94979678/203690863-739ac7a5-357e-4662-8606-2f30b30b8d86.png)
![image](https://user-images.githubusercontent.com/94979678/203690898-756a9b14-d59d-4644-9388-f9e988b3a8cd.png)


 
 



