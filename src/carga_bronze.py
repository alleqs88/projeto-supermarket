import pandas as pd

from conexao import engine


# Caminho do arquivo CSV original
caminho_arquivo = "data/raw/SuperMarket Analysis.csv"

# Leitura do CSV
df = pd.read_csv(caminho_arquivo)

# Renomeando as colunas para os nomes da tabela Bronze
df.columns = [
    "invoice_id",
    "branch",
    "city",
    "customer_type",
    "gender",
    "product_line",
    "unit_price",
    "quantity",
    "tax_5",
    "sales",
    "date",
    "time",
    "payment",
    "cogs",
    "gross_margin_percentage",
    "gross_income",
    "rating"
]

# Inserindo os dados na camada Bronze
df.to_sql(
    name="vendas",
    con=engine,
    schema="bronze",
    if_exists="append",
    index=False
)

print(f"Carga concluída! {len(df)} registros inseridos em bronze.vendas.")