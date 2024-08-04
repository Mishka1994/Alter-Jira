from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.db import get_db
from models.person import Person
from services.person import PersonService
from structs.person import PersonStruct, CreatePersonStruct, UpdatePersonStruct

person_router = APIRouter(prefix='/person', tags=['Person'])


@person_router.get('/', response_model=list[PersonStruct])
def all_(db: Session = Depends(get_db)):
    service: PersonService = PersonService(model=Person, struct=PersonStruct, db=db)
    return service.get_all()


@person_router.get('/{person_id}')
def get(person_id: int, db: Session = Depends(get_db)) -> PersonStruct:
    service: PersonService = PersonService(model=Person, struct=PersonStruct, db=db)
    return service.get_by_id(person_id)


@person_router.post('/')
def create(person: CreatePersonStruct, db: Session = Depends(get_db)) -> PersonStruct:
    service: PersonService = PersonService(model=Person, struct=PersonStruct, db=db)
    return service.create(person)


@person_router.put('/{person_id}')
def update(person_id: int, data: UpdatePersonStruct, db: Session = Depends(get_db)) -> PersonStruct:
    service: PersonService = PersonService(model=Person, struct=PersonStruct, db=db)
    return service.update(person_id, data)


@person_router.delete('/{person_id}')
def delete(person_id: int, db: Session = Depends(get_db)):
    service: PersonService = PersonService(model=Person, struct=PersonStruct, db=db)
    return service.delete(person_id)
