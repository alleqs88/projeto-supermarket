
# Dicionário de Dados

Este documento descreve as colunas da base tratada de vendas,
armazenada na camada Silver e no arquivo `vendas_tratadas.csv`.

| Coluna            | Tipo          | Descrição                                      |
| ----------------- | ------------- | ------------------------------------------------ |
| id_venda          | VARCHAR(50)   | Identificador único da venda                    |
| filial            | VARCHAR(10)   | Filial onde a venda foi realizada                |
| cidade            | VARCHAR(100)  | Cidade onde a venda foi realizada                |
| tipo_cliente      | VARCHAR(50)   | Tipo de cliente                                  |
| genero            | VARCHAR(20)   | Gênero informado no cadastro do cliente         |
| linha_produto     | VARCHAR(150)  | Categoria ou linha do produto vendido            |
| preco_unitario    | NUMERIC(10,2) | Preço unitário do produto                      |
| quantidade        | INTEGER       | Quantidade de itens vendidos                     |
| imposto           | NUMERIC(10,2) | Valor do imposto de 5% da venda                  |
| valor_total       | NUMERIC(12,2) | Valor total da venda                             |
| data_venda        | DATE          | Data em que a venda foi realizada                |
| hora_venda        | TIME          | Horário em que a venda foi realizada            |
| forma_pagamento   | VARCHAR(50)   | Forma de pagamento utilizada                     |
| custo_mercadoria  | NUMERIC(12,2) | Custo das mercadorias vendidas                   |
| margem_percentual | NUMERIC(10,2) | Percentual de margem bruta registrado na base    |
| receita_bruta     | NUMERIC(12,2) | Receita bruta registrada na base original        |
| avaliacao         | NUMERIC(4,2)  | Avaliação atribuída à experiência de compra |
