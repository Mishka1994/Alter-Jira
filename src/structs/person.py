from pydantic import BaseModel, ConfigDict


class BasePersonStruct(BaseModel):
    name: str

    model_config = ConfigDict(from_attributes=True)


class CreatePersonStruct(BasePersonStruct):
    pass


class UpdatePersonStruct(BasePersonStruct):
    pass


class PersonStruct(BasePersonStruct):
    id: int
