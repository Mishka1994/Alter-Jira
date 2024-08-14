class TestTasks:
    def test_get(self, client):
        response = client.get('/tasks/1')
        assert response.status_code == 200
        assert response.json() == {
            'description': 'very important task',
            'id': 1,
            'person_id': 1,
            'status': 'todo',
            'name': 'task1'
        }
