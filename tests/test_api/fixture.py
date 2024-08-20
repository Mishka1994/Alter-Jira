import pytest


@pytest.fixture
def update_person():
    return {"name": "Update_Test_person1"}


@pytest.fixture
def data_task():
    return {
        "description": "very important task",
        "person_id": 1,
        "status": "todo",
        "name": "task1",
    }


@pytest.fixture
def update_task():
    return {
        "name": "task1",
        "description": "very important task",
        "person_id": 1,
        "status": "done",
    }


@pytest.fixture
def second_data_task():
    return {
        "description": "not important task",
        "person_id": 1,
        "status": "done",
        "name": "task2",
    }


@pytest.fixture
def data_person():
    return {"name": "Test_person1"}


@pytest.fixture
def second_data_person():
    return {"name": "Test_person2"}
