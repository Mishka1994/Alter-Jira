from models.person import Person
from structs.person import PersonStruct, CreatePersonStruct, UpdatePersonStruct


class PersonService:
    @classmethod
    def get_person_by_id(cls, person_id: int, db) -> PersonStruct:
        query = db.query(Person).filter(Person.id == person_id).first()
        data = PersonStruct.model_validate(query)
        return data

    @classmethod
    def get_all_person(cls, db) -> list[PersonStruct]:
        query = db.query(Person).all()
        data = [PersonStruct.model_validate(el) for el in query]
        return data

    @classmethod
    def create_person(cls, data: CreatePersonStruct, db) -> PersonStruct:
        person = Person(**data.model_dump())
        db.add(person)
        db.commit()
        db.refresh(person)
        return PersonStruct.model_validate(person)

    @classmethod
    def update_person(cls, person_id: int, data: UpdatePersonStruct, db) -> PersonStruct:
        person = db.query(Person).filter(Person.id == person_id).first()
        for key, value in data.dict.items():
            setattr(person, key, value)
        db.commit()
        db.refresh(person)
        return PersonStruct.model_validate(person)

    @classmethod
    def delete_person(cls, person_id: int, db):
        db.query(Person).filter(Person.id == person_id).delete()
        db.commit()
        return {'message': 'Person deleted successfully'}
