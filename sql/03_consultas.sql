-- Consulta geral da camada Silver
SELECT *
FROM silver.vendas;


-- Formas de pagamento disponíveis
SELECT DISTINCT forma_pagamento
FROM silver.vendas;


-- Vendas realizadas com cartão de crédito
SELECT *
FROM silver.vendas
WHERE forma_pagamento = 'Credit card';


-- Quantidade de vendas realizadas com cartão de crédito
SELECT COUNT(*) AS quantidade_vendas
FROM silver.vendas
WHERE forma_pagamento = 'Credit card';


-- Quantidade de vendas por forma de pagamento
SELECT
    forma_pagamento,
    COUNT(*) AS quantidade_vendas
FROM silver.vendas
GROUP BY forma_pagamento
ORDER BY quantidade_vendas DESC;

-- Faturamento total por filial
SELECT
    filial,
    SUM(valor_total) AS faturamento_total
FROM silver.vendas
GROUP BY filial
ORDER BY faturamento_total DESC;

-- Valor médio das vendas
SELECT
    ROUND(AVG(valor_total), 2) AS valor_medio_vendas
FROM silver.vendas;

-- Maior venda registrada
SELECT
    MAX(valor_total) AS maior_venda
FROM silver.vendas;

-- Detalhes da maior venda registrada
SELECT
    id_venda,
    filial,
    cidade,
    linha_produto,
    valor_total,
    forma_pagamento
FROM silver.vendas
ORDER BY valor_total DESC
LIMIT 1;

-- Quantidade de vendas por filial
SELECT
    filial,
    COUNT(*) AS quantidade_vendas
FROM silver.vendas
GROUP BY filial
ORDER BY quantidade_vendas DESC;

-- Faturamento por linha de produto
SELECT
    linha_produto,
    SUM(valor_total) AS faturamento_total
FROM silver.vendas
GROUP BY linha_produto
ORDER BY faturamento_total DESC;

-- Avaliação média por linha de produto
SELECT
    linha_produto,
    ROUND(AVG(avaliacao), 2) AS avaliacao_media
FROM silver.vendas
GROUP BY linha_produto
ORDER BY avaliacao_media DESC;

-- Quantidade de vendas por dia da semana
SELECT
    TO_CHAR(data_venda, 'Day') AS dia_semana,
    COUNT(*) AS quantidade_vendas
FROM silver.vendas
GROUP BY dia_semana
ORDER BY quantidade_vendas DESC;