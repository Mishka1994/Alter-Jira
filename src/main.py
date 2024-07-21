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


@app.on_event('startup')
async def startup_event():
    from config.db import engine, Base
    from models.task import Task  # noqa
    from models.person import Person # noqa
    Base.metadata.create_all(bind=engine)

