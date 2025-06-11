from sqlmodel import SQLModel, create_engine, Session
from dotenv import load_dotenv
import os
from dotenv import load_dotenv

load_dotenv()  # carrega o .env na raiz do projeto

DATABASE_URL = os.getenv("DATABASE_URL")

from sqlmodel import create_engine

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    return Session(engine)

def create_db():
    from models import motorista, viagem, registro_frequencia  # importa todos os modelos
    SQLModel.metadata.create_all(engine)
