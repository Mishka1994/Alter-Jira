from tests.test_api.fixture import data_task, data_person, second_data_task, update_task

from models.person import Person
from models.task import Task


def test_get(client, data_task, data_person, test_db):
    person = Person(**data_person)
    test_db.add(person)
    test_db.commit()
    test_db.refresh(person)

    task = Task(**data_task)
    test_db.add(task)
    test_db.commit()
    test_db.refresh(task)

    response = client.get(f"/tasks/{task.id}")
    assert response.status_code == 200


def test_all(client, data_person, data_task, second_data_task, test_db):
    person = Person(**data_person)
    test_db.add(person)
    test_db.commit()
    test_db.refresh(person)

    task_1 = Task(**data_task)
    task_2 = Task(**second_data_task)
    # test_db.add_all([task_1, task_2])
    test_db.add(task_1)
    test_db.add(task_2)
    test_db.commit()
    test_db.refresh(task_1)
    test_db.refresh(task_2)

    response = client.get("/tasks/")
    assert response.status_code == 200


def test_create(client, test_db, data_person, data_task):
    person = Person(**data_person)
    test_db.add(person)
    test_db.commit()
    test_db.refresh(person)

    response = client.post("/tasks/", json=data_task)
    assert response.status_code == 200


def test_update(client, test_db, data_person, data_task, update_task):
    person = Person(**data_person)
    test_db.add(person)
    test_db.commit()
    test_db.refresh(person)

    task = Task(**data_task)
    test_db.add(task)
    test_db.commit()
    test_db.refresh(task)

    response = client.put(f"/tasks/{task.id}", json=update_task)
    assert response.status_code == 200
    # assert response.json() == {
    #     "id": 1,
    #     "name": "task1",
    #     "description": "very important task",
    #     "person_id": 1,
    #     "status": "done",
    # }


def test_delete(client, test_db, data_person, data_task):
    person = Person(**data_person)
    test_db.add(person)
    test_db.commit()
    test_db.refresh(person)

    task = Task(**data_task)
    test_db.add(task)
    test_db.commit()
    test_db.refresh(task)

    response = client.delete(f"/tasks/{task.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Model instance deleted successfully"}
