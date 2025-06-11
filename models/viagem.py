from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import date, datetime

class Viagem(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    data_viagem: date
    hora_partida: datetime
    status: str
    vagas_ocupadas: int
    motorista_id: int = Field(foreign_key="motorista.id")
    veiculo_id: Optional[int] = None  # ainda não modelamos veiculo
    rota_id: Optional[int] = None     # ainda não modelamos rota
