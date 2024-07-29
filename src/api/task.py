from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.db import get_db
from services.task import TaskService
from structs.task import CreateTaskStruct, TaskStruct, UpdateTaskStruct

task_router = APIRouter(prefix='/task', tags=['Task'])


@task_router.get('/')
def all_(db: Session = Depends(get_db)) -> list[TaskStruct]:
    return TaskService.get_all_tasks(db)


@task_router.get('/{task_ud}')
def get(task_id: int, db: Session = Depends(get_db)) -> TaskStruct:
    return TaskService.get_task_by_id(task_id, db)


@task_router.post('/')
def create(task: CreateTaskStruct, db: Session = Depends(get_db)) -> TaskStruct:
    return TaskService.create_task(task, db)


@task_router.put('/{task_id}')
def update(task: int, data: UpdateTaskStruct, db: Session = Depends(get_db)) -> TaskStruct:
    return TaskService.update_task(task, data, db)


@task_router.delete('/{task_id}')
def delete(task: int, db: Session = Depends(get_db)):
    return TaskService.delete_task(task, db)
