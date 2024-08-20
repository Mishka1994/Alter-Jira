from tests.test_api.fixture import update_person, second_data_person, data_person
from models.person import Person


def test_get(client, test_db, data_person):
    person = Person(**data_person)
    test_db.add(person)
    test_db.commit()
    test_db.refresh(person)

    response = client.get(f"/persons/{person.id}")
    assert response.status_code == 200
    # assert response.json()["id"] == 1
    # assert response.json()["name"] == "Test_person1"


def test_all(client, test_db, data_person, second_data_person):
    person = Person(**data_person)
    person_2 = Person(**second_data_person)

    test_db.add_all([person, person_2])
    test_db.commit()

    response = client.get("/persons")
    assert response.status_code == 200
    # assert response.json() == [{"id": person.id, "name": f"{person.name}"},
    #                            {"id": person_2.id, "name": f"{person_2.name}"}]


def test_create(client, test_db, data_person):
    response = client.post("/persons/", json=data_person)
    assert response.status_code == 200
    # assert response.json()["id"] == 1
    # assert response.json()["name"] == "Test_person1"


def test_update(client, test_db, data_person, update_person):
    person = Person(**data_person)
    test_db.add(person)
    test_db.commit()
    test_db.refresh(person)

    response = client.put(f"/persons/{person.id}", json=update_person)
    assert response.status_code == 200
    # assert response.json()["name"] == "Update_Test_person1"


def test_delete(client, test_db, data_person):
    person = Person(**data_person)
    test_db.add(person)
    test_db.commit()
    test_db.refresh(person)

    response = client.delete(f"/persons/{person.id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Model instance deleted successfully"}
