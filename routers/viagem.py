from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session, select
from typing import List
from datetime import date
from models.viagem import Viagem
from database import get_session

router = APIRouter(prefix="/viagens")

@router.post("/", response_model=Viagem)
def criar_viagem(viagem: Viagem, session: Session = get_session()):
    session.add(viagem)
    session.commit()
    session.refresh(viagem)
    return viagem

@router.get("/", response_model=List[Viagem])
def listar_viagens(
    page: int = 1, limit: int = 10,
    data: Optional[date] = None,
    status: Optional[str] = None,
    session: Session = get_session()\):
    query = select(Viagem)
    if data:
        query = query.where(Viagem.data_viagem == data)
    if status:
        query = query.where(Viagem.status == status)
    offset = (page - 1) * limit
    return session.exec(query.offset(offset).limit(limit)).all()