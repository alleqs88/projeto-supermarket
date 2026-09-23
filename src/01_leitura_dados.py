import pandas as pd


caminho_arquivo = "data/raw/SuperMarket Analysis.csv"

df = pd.read_csv(caminho_arquivo)

print(df.head())

print("\nInformações do DataFrame:")
df.info()

print("\nDimensão do DataFrame:")
print(df.shape)

print("\nQuantidade de valores nulos:")
print(df.isnull().sum())

print("\nQuantidade de linhas duplicadas:")
print(df.duplicated().sum())