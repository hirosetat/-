from fastapi import FastAPI
import MeCab
from typing import Optional
m_t = MeCab.Tagger('-Ochasen')

text = '機械学習が好きです。'

print(m_t.parse(text))

app = FastAPI()


@app.get("/")
def read_root():
    return m_t.parse(text)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}