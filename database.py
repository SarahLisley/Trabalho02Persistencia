from sqlmodel import SQLModel, create_engine
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não foi encontrada. Verifique o arquivo .env")

# Criar engine do SQLAlchemy
engine = create_engine(DATABASE_URL, echo=True)

def create_db():
    """Função para criar todas as tabelas do banco de dados"""
    SQLModel.metadata.create_all(engine)
