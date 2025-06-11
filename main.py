from fastapi import FastAPI
from database import create_db

app = FastAPI()

@app.on_event("startup")
def startup():
    create_db()

@app.get("/")
def root():
    return {"message": "API Transporte Acadêmico - Motorista/Viagem/Frequência"}


from logger import logger