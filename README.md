
# Análise de Vendas de Supermercado

Projeto desenvolvido para realizar a análise de dados de vendas de um supermercado, utilizando Python, Pandas, PostgreSQL e SQL.

O projeto aplica conceitos de extração, transformação e análise de dados, utilizando uma arquitetura inspirada no modelo Medallion, com as camadas Bronze, Silver e Gold.

## Objetivo do Projeto

O objetivo deste projeto é aplicar conceitos de análise de dados em uma base de vendas de supermercado, passando pelas etapas de leitura, armazenamento, tratamento e análise dos dados.

A partir dos dados tratados, foram realizadas consultas SQL, análises estatísticas com Pandas e visualizações gráficas para identificar informações relevantes sobre faturamento, quantidade de vendas, linhas de produtos, formas de pagamento e comportamento das vendas ao longo da semana.

## Tecnologias Utilizadas

- Python
- Pandas
- PostgreSQL
- SQL
- SQLAlchemy
- psycopg2
- python-dotenv
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git e GitHub
- VS Code
- DBeaver

## Estrutura do Projeto

```text
projeto_supermarket/
│
├── data/
│   ├── raw/
│   │   ├── SuperMarket Analysis.csv
│   │   └── vendas_exportadas_sql.csv
│   ├── processed/
│   │   └── vendas_tratadas.csv
│   └── dicionario_dados.md
│
├── notebooks/
│   └── analise_vendas.ipynb
│
├── resultados/
│   ├── avaliacao_produtos.png
│   ├── faturamento_filial.png
│   ├── faturamento_produto.png
│   ├── quantidade_vendas_filial.png
│   ├── vendas_dia_semana.png
│   └── vendas_pagamentos.png
│
├── sql/
│   ├── 01_criar_banco.sql
│   ├── 02_criar_tabelas.sql
│   └── 03_consultas.sql
│
├── src/
│   ├── 01_leitura_dados.py
│   ├── 02_etl_vendas.py
│   ├── 03_estatistica.py
│   ├── carga_bronze.py
│   └── conexao.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Como Executar o Projeto

### 1. Instalar as dependências

Com o terminal aberto na pasta raiz do projeto, execute:

```bash
pip install -r requirements.txt
```

Esse comando instalará as bibliotecas Python necessárias para a execução do projeto.

### 2. Configurar o PostgreSQL

No PostgreSQL, execute primeiro o arquivo:

```text
sql/01_criar_banco.sql
```

Esse script cria o banco de dados `supermercado_db`.

Depois, conecte-se ao banco `supermercado_db` e execute:

```text
sql/02_criar_tabelas.sql
```

Esse script cria os schemas `bronze`, `silver` e `gold`, além das tabelas utilizadas no projeto.

### 3. Configurar as variáveis de ambiente

Na raiz do projeto, crie um arquivo chamado `.env` com as configurações de acesso ao PostgreSQL:

```env
DB_USUARIO=postgres
DB_SENHA=sua_senha
DB_HOST=localhost
DB_PORTA=5432
DB_BANCO=supermercado_db
```

Substitua `sua_senha` pela senha configurada no seu PostgreSQL.

O arquivo `.env` está incluído no `.gitignore` para evitar que informações de acesso ao banco de dados sejam enviadas ao repositório.

### 4. Executar o pipeline de dados

Com o banco de dados configurado e o arquivo `.env` criado, execute os scripts a partir da pasta raiz do projeto.

Primeiro, verifique a leitura e a estrutura dos dados originais:

```bash
python src/01_leitura_dados.py
```

Depois, carregue os dados originais na camada Bronze:

```bash
python src/carga_bronze.py
```

Em seguida, execute o processo de ETL para tratar os dados, gerar o arquivo `vendas_tratadas.csv` e carregar os registros na camada Silver:

```bash
python src/02_etl_vendas.py
```

Por fim, execute as análises estatísticas:

```bash
python src/03_estatistica.py
```

## Consultas e Exportação SQL

As consultas SQL utilizadas nas análises estão disponíveis em:

```text
sql/03_consultas.sql
```

Os dados consultados no PostgreSQL também foram exportados para CSV e estão disponíveis em:

```text
data/raw/vendas_exportadas_sql.csv
```

## Notebook de Análise

A análise exploratória e as visualizações gráficas estão disponíveis no notebook:

```text
notebooks/analise_vendas.ipynb
```

Os gráficos gerados durante as análises estão armazenados na pasta:

```text
resultados/
```

## Principais Resultados

A análise dos dados permitiu identificar alguns resultados importantes:

- A filial **Giza** apresentou o maior faturamento, com aproximadamente **R$ 110.568,71**.
- A filial **Alex** apresentou a maior quantidade de vendas, totalizando **340 vendas**.
- A linha de produtos **Food and beverages** apresentou o maior faturamento, com aproximadamente **R$ 56.144,84**.
- **Food and beverages** também apresentou a maior média de avaliação, com aproximadamente **7,11**.
- A forma de pagamento mais utilizada foi **Ewallet**, com **345 vendas**.
- O valor médio das vendas foi de aproximadamente **R$ 322,97**.
- A maior venda registrada foi de **R$ 1.042,65**.
- **Sábado** foi o dia da semana com a maior quantidade de vendas, totalizando **164 vendas**.

## Arquitetura dos Dados

O projeto utiliza uma arquitetura inspirada no modelo Medallion, organizando os dados em diferentes camadas:

- **Bronze:** armazena os dados originais importados do arquivo CSV, preservando sua estrutura inicial.
- **Silver:** contém os dados após o processo de tratamento, conversão de tipos e validação realizado com Python e Pandas.
- **Gold:** representa a etapa de análise dos dados tratados, com métricas, estatísticas e visualizações armazenadas na pasta `resultados/`.

Essa organização permite separar os dados brutos dos dados tratados e das informações utilizadas nas análises.

## Dicionário de Dados

A descrição das colunas, tipos de dados e informações da base tratada está disponível em:

```text
data/dicionario_dados.md
```

## Conclusão

O desenvolvimento deste projeto permitiu aplicar, de forma prática, diferentes etapas de um processo de análise de dados, desde a leitura e o armazenamento dos dados originais até o tratamento, análise estatística e criação de visualizações.

A utilização de Python, Pandas, SQL e PostgreSQL possibilitou organizar e analisar os dados de vendas, enquanto o Git e o GitHub foram utilizados para o controle de versão e documentação da evolução do projeto.
