import pytest
import requests

# CRUD
BASE_URL = 'SUA_URL_AQUI'
tasks = []

def test_create_task():
    new_task_data = {
        "title": "Nova tarefa",
        "description": "Descrição da nova tarefa"
    }
    response = requests.post(f"{BASE_URL}/tasks", json=new_task_data)
    assert response.status_code == 200

    response_json = response.json()

    assert "message" in response_json
    assert "id" in response_json
    tasks.append(response_json['id'])