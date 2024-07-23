from fastapi import APIRouter

person_router = APIRouter(prefix='/person', tags=['Person'])


@person_router.get('/')
def all_():
    return {'Hello': 'World'}


@person_router.get('/{person_id}')
def get(person_id: int):
    return {'person_id': person_id}


@person_router.post('/')
def create():
    return {'hello': 'world'}


@person_router.put('/{person_id}')
def update(person_id: int):
    return {'person_id': person_id}


@person_router.delete('/{person_id}')
def delete(person_id: int):
    return {'person_id': person_id}
