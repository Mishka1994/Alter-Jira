from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.db import get_db
from models.task import Task
from services.task import TaskService
from structs.task import CreateTaskStruct, TaskStruct, UpdateTaskStruct

task_router = APIRouter(prefix="/tasks", tags=["Task"])


@task_router.get("/")
def all_(db: Session = Depends(get_db)) -> list[TaskStruct]:
    service: TaskService = TaskService(model=Task, struct=TaskStruct, db=db)
    return service.get_all()


@task_router.get("/{task_id}")
def get(task_id: int, db: Session = Depends(get_db)) -> TaskStruct:
    service: TaskService = TaskService(model=Task, struct=TaskStruct, db=db)
    return service.get_by_id(task_id)


@task_router.post("/")
def create(task: CreateTaskStruct, db: Session = Depends(get_db)) -> TaskStruct:
    service: TaskService = TaskService(model=Task, struct=TaskStruct, db=db)
    return service.create(task)


@task_router.put("/{task_id}")
def update(
    task_id: int, data: UpdateTaskStruct, db: Session = Depends(get_db)
) -> TaskStruct:
    service: TaskService = TaskService(model=Task, struct=TaskStruct, db=db)
    return service.update(task_id, data)


@task_router.delete("/{task_id}")
def delete(task_id: int, db: Session = Depends(get_db)):
    service: TaskService = TaskService(model=Task, struct=TaskStruct, db=db)
    return service.delete(task_id)
