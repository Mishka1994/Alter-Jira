from pydantic import BaseModel, ConfigDict


class BaseTaskStruct(BaseModel):
    name: str
    description: str
    status: str
    person_id: int

    model_config = ConfigDict(from_attributes=True)


class CreateTaskStruct(BaseTaskStruct):
    pass


class UpdateTaskStruct(BaseTaskStruct):
    pass


class TaskStruct(BaseTaskStruct):
    id: int
