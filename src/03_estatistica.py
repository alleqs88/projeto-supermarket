import pandas as pd


# Leitura da base tratada
caminho_arquivo = "data/processed/vendas_tratadas.csv"

df = pd.read_csv(caminho_arquivo)

print(df.head())


# Estatísticas gerais das vendas
media_vendas = df["valor_total"].mean()
print(f"\nValor médio das vendas: {media_vendas:.2f}")

maior_venda = df["valor_total"].max()
print(f"Maior valor de venda foi: {maior_venda:.2f}")

menor_valor = df["valor_total"].min()
print(f"Menor valor de venda foi: {menor_valor:.2f}")

faturamento_total = df["valor_total"].sum()
print(f"Faturamento total: {faturamento_total:.2f}")

quantidade_vendas = len(df)
print(f"Quantidade total de vendas: {quantidade_vendas}")

desvio_padrao = df["valor_total"].std()
print(f"Desvio padrão das vendas: {desvio_padrao:.2f}")

mediana_vendas = df["valor_total"].median()
print(f"Mediana das vendas: {mediana_vendas:.2f}")


# Estatísticas descritivas
print("\nEstatísticas descritivas de valor_total:")
print(df["valor_total"].describe())

print("\nEstatísticas descritivas das colunas numéricas:")
print(df.describe())


# Quantidade de vendas por forma de pagamento
vendas_pagamento = df["forma_pagamento"].value_counts()

print("\nQuantidade de vendas por forma de pagamento:")
print(vendas_pagamento)


# Quantidade de vendas por filial
vendas_filial = df["filial"].value_counts()

print("\nQuantidade de vendas por filial:")
print(vendas_filial)


# Faturamento por filial
faturamento_filial = (
    df.groupby("filial")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFaturamento por filial:")
print(faturamento_filial)

# Avaliação média por linha de produto
avaliacao_produto = (
    df.groupby("linha_produto")["avaliacao"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAvaliação média por linha de produto:")
print(avaliacao_produto)

# Faturamento por linha de produto
faturamento_produto = (
    df.groupby("linha_produto")["valor_total"]
    .sum()
    .sort_values(ascending=False)
)

print("\nFaturamento por linha de produto:")
print(faturamento_produto)

# Quantidade de vendas por dia da semana
df["data_venda"] = pd.to_datetime(df["data_venda"])

df["dia_semana"] = df["data_venda"].dt.day_name()

vendas_dia_semana = df["dia_semana"].value_counts()

print("\nQuantidade de vendas por dia da semana:")
print(vendas_dia_semana)
