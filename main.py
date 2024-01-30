from typing import Union
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class WorkItem(BaseModel):
  pass

@app.get("/")
def read_root():
  return {"Hello":"World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str,None] = None):
  return {"item_id": item_id, "q":q}

@app.post("/items/{item}")
def write_item(item_id: int, q: Union[str, None] = None):
  pass
