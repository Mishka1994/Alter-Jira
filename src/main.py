from typing import Union

from fastapi import FastAPI

from api.person import person_router
from api.task import task_router
from config.settings import AppSettings

app = FastAPI(**AppSettings().model_dump())

app.include_router(person_router)
app.include_router(task_router)

@app.on_event('startup')
async def startup_event():
    from config.db import engine, Base
    from models.task import Task  # noqa
    from models.person import Person # noqa
    Base.metadata.create_all(bind=engine)

