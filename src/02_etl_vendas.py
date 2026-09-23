import pandas as pd

from sqlalchemy import text

from conexao import engine


# Lendo os dados da camada Bronze
consulta = """
SELECT *
FROM bronze.vendas;
"""

df = pd.read_sql(consulta, engine)

print(df.head())

print("\nInformações do DataFrame:")
df.info()


# Conversão das colunas numéricas
colunas_numericas = [
    "unit_price",
    "tax_5",
    "sales",
    "cogs",
    "gross_margin_percentage",
    "gross_income",
    "rating"
]

for coluna in colunas_numericas:
    df[coluna] = pd.to_numeric(
        df[coluna],
        errors="coerce"
    )

df["quantity"] = pd.to_numeric(
    df["quantity"],
    errors="coerce"
).astype("Int64")

print("\nTipos após conversão:")
print(df.dtypes)


# Conversão de data e hora
df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

df["time"] = pd.to_datetime(
    df["time"],
    format="%I:%M:%S %p",
    errors="coerce"
).apply(
    lambda valor: valor.time()
    if pd.notna(valor)
    else None
)

print("\nTipos após conversão de data e hora:")
print(df.dtypes)

print("\nValores nulos após as conversões:")
print(df.isnull().sum())


# Renomeando as colunas para o padrão da camada Silver
df = df.rename(columns={
    "invoice_id": "id_venda",
    "branch": "filial",
    "city": "cidade",
    "customer_type": "tipo_cliente",
    "gender": "genero",
    "product_line": "linha_produto",
    "unit_price": "preco_unitario",
    "quantity": "quantidade",
    "tax_5": "imposto",
    "sales": "valor_total",
    "date": "data_venda",
    "time": "hora_venda",
    "payment": "forma_pagamento",
    "cogs": "custo_mercadoria",
    "gross_margin_percentage": "margem_percentual",
    "gross_income": "receita_bruta",
    "rating": "avaliacao"
})

print("\nColunas após renomeação:")
print(df.columns)


# Validação dos valores calculados
df["custo_calculado"] = (
    df["preco_unitario"] * df["quantidade"]
)

df["imposto_calculado"] = (
    df["custo_calculado"] * 0.05
)

print("\nComparação dos valores calculados:")
print(
    df[
        [
            "custo_mercadoria",
            "custo_calculado",
            "imposto",
            "imposto_calculado"
        ]
    ].head()
)


# Verificando diferenças nos cálculos
diferenca_custo = (
    df["custo_mercadoria"] - df["custo_calculado"]
).abs()

diferenca_imposto = (
    df["imposto"] - df["imposto_calculado"]
).abs()

print("\nRegistros com diferença no custo:")
print((diferenca_custo > 0.01).sum())

print("\nRegistros com diferença no imposto:")
print((diferenca_imposto > 0.01).sum())


# Removendo colunas utilizadas apenas para validação
df.drop(
    columns=[
        "custo_calculado",
        "imposto_calculado"
    ],
    inplace=True
)


# Verificando a dimensão final
print("\nDimensão final do DataFrame:")
print(df.shape)


# Verificação de IDs duplicados
ids_duplicados = df["id_venda"].duplicated().sum()

print("\nQuantidade de IDs duplicados:")
print(ids_duplicados)


# Salvando a base tratada
caminho_saida = "data/processed/vendas_tratadas.csv"

df.to_csv(
    caminho_saida,
    index=False
)

print(
    f"\nArquivo tratado salvo em: "
    f"{caminho_saida}"
)


# Limpando os registros existentes da camada Silver
with engine.begin() as conexao:
    conexao.execute(
        text("TRUNCATE TABLE silver.vendas;")
    )


# Carregando os dados tratados na camada Silver
df.to_sql(
    name="vendas",
    con=engine,
    schema="silver",
    if_exists="append",
    index=False
)

print(
    f"\nCarga concluída! "
    f"{len(df)} registros inseridos em silver.vendas."
)