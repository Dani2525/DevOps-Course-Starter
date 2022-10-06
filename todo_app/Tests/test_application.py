import os
import pytest
import requests
from todo_app import app
from dotenv import load_dotenv, find_dotenv
import mongomock

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    with mongomock.patch(servers=(('fakemongo.com', 27017),)):
        test_app = app.create_app()
        with test_app.test_client() as client:
            yield client


def test_index_page_with_no_items(client):
    response = client.get("/")
    assert response.status_code == 200
    assert 'item1' not in response.data.decode()
    assert 'item2' not in response.data.decode()
    assert 'item3' not in response.data.decode()

def test_index_page_with_todo_items()
