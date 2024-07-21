from typing import Union

from fastapi import FastAPI

from config.settings import AppSettings

app = FastAPI(**AppSettings().model_dump())


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None):
    return {'item_id': item_id, 'q': q}
