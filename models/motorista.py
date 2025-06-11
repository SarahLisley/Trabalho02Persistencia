from sqlmodel import SQLModel, Field
from datetime import date

class Motorista(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    nome_completo: str
    cnh: str
    telefone: str
    data_admissao: date
    status_ativo: bool
