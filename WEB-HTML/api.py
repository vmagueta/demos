import json
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


# Serializador de Saída
class PersonOut(BaseModel):
    id: int
    name: str
    picture: str
    age: int
    email: str
    about: Optional[str] = ""
    is_active: bool


app = FastAPI()

@app.get("/", response_model=list[PersonOut])
async def read_root(is_active: Optional[str] = None):
    if is_active is not None:
        is_active = is_active.lower() == "true"

    return get_pessoas(is_active=is_active)


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



def get_pessoas(is_active=None) -> list[dict[str, any]]:
    with open("data.json") as datafile:
        data = json.loads(datafile.read())

    if is_active is not None:
        return [pessoa for pessoa in data if pessoa["is_active"] == is_active]
    return data
