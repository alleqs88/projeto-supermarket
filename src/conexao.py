import os

from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

engine = create_engine(
    f"postgresql+psycopg2://"
    f"{os.getenv('DB_USUARIO')}:{os.getenv('DB_SENHA')}"
    f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORTA')}"
    f"/{os.getenv('DB_BANCO')}"
)

try:
    with engine.connect():
        print("Conexão com PostgreSQL realizada com sucesso!")

except Exception as erro:
    print(f"Erro ao conectar: {erro}")