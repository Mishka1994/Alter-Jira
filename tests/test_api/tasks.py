import pytest

from models.person import Person
from models.task import Task


@pytest.fixture
def data_task():
    return {
        'description': 'very important task',
        'id': 1,
        'person_id': 1,
        'status': 'todo',
        'name': 'task1'
    }


@pytest.fixture
def data_person():
    return {
        'name': 'Test_person1'
    }

class TestTasks:
    def test_get(self, client, data_task, data_person, test_db):
        person = Person(**data_person)
        test_db.add(person)
        test_db.commit()
        test_db.refresh(person)
        task = Task(**data_task)
        test_db.add(task)
        test_db.commit()

        response = client.get('/tasks/1')
        assert response.status_code == 200
        assert response.json() == {
            'description': 'very important task',
            'id': 1,
            'person_id': 1,
            'status': 'todo',
            'name': 'task1'
        }
