from fastapi import APIRouter
from sqlmodel import Session, select
from typing import List
from models.registro_frequencia import RegistroFrequencia
from database import get_session

router = APIRouter(prefix="/frequencias")

@router.post("/", response_model=RegistroFrequencia)
def criar_registro(registro: RegistroFrequencia, session: Session = get_session()):
    session.add(registro)
    session.commit()
    session.refresh(registro)
    return registro

@router.get("/", response_model=List[RegistroFrequencia])
def listar_registros(session: Session = get_session()):
    return session.exec(select(RegistroFrequencia)).all()
