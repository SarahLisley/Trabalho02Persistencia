from sqlmodel import SQLModel, Field
from datetime import datetime

class RegistroFrequencia(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    viagem_id: int = Field(foreign_key="viagem.id")
    aluno_id: int   # se você quiser FK real, precisa importar e definir Aluno
    data_hora_embarque: datetime
    tipo_registro: str  # Ex: "Embarque" ou "Desembarque"
