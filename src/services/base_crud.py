from fastapi import HTTPException


class BaseCRUD:
    def __init__(self, model, struct, db):
        self._model = model
        self._struct = struct
        self._db = db

    def get_by_id(self, id_: int):
        queue = self._db.query(self._model).filter(self._model.id == id_).first()
        if not queue:
            raise HTTPException(status_code=404, detail='Not found')
        return self._struct.model_validate(queue)

    def get_all(self):
        queue = self._db.query(self._model).all()
        return [self._struct.model_validate(el) for el in queue]

    def create(self, data):
        model = self._model(**data.model_dump())
        self._db.add(model)
        self._db.commit()
        self._db.refresh(model)
        return self._struct.model_validate(model)

    def update(self, id_: int, data):
        model = self._db.query(self._model).filter(self._model.id == id_).first()
        if not model:
            raise HTTPException(status_code=404, detail='Not found')
        for key, value in data.dict().items():
            setattr(model, key, value)
        self._db.commit()
        self._db.refresh(model)
        return self._struct.model_validate(model)

    def delete(self, id_: int):
        self._db.query(self._model).filter(self._model.id == id_).delete()
        self._db.commit()
        return {'message': 'Model instance deleted successfully'}
