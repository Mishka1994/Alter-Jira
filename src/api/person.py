from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.db import get_db
from services.person import PersonService
from structs.person import PersonStruct, CreatePersonStruct, UpdatePersonStruct

person_router = APIRouter(prefix='/person', tags=['Person'])


@person_router.get('/', response_model=list[PersonStruct])
def all_(db: Session = Depends(get_db)):
    return PersonService.get_all_person(db)


@person_router.get('/{person_id}')
def get(person_id: int, db: Session = Depends(get_db)) -> PersonStruct:
    return PersonService.get_person_by_id(person_id, db)


@person_router.post('/')
def create(person: CreatePersonStruct, db: Session = Depends(get_db)) -> PersonStruct:
    return PersonService.create_person(person, db)


@person_router.put('/{person_id}')
def update(person_id: int, data: UpdatePersonStruct, db: Session = Depends(get_db)) -> PersonStruct:
    return PersonService.update_person(person_id, data, db)


@person_router.delete('/{person_id}')
def delete(person_id: int, db: Session = Depends(get_db)):
    return PersonService.delete_person(person_id, db)
