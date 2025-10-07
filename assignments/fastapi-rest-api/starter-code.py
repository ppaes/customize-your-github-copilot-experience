# Código inicial para a tarefa de FastAPI

# Para começar, instale o FastAPI e o Uvicorn:
# pip install fastapi uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Estrutura de dados em memória
items = []

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# Implemente os endpoints conforme solicitado no README.md
