from fastapi.testclient import TestClient
from fastapi import status
import sys
import os
sys.path.append(os.path.dirname(__file__) + '/..')

from main import app


client = TestClient(app)

def test_app_health():
    response = client.get('/healthy')
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'status': 'healthy'}

def test_get_request():
    response = client.get('/word-frequency?article=Pet%20door&depth=0')
    assert response.status_code == 200
    assert 'dog' in response.text

def test_post_request():
    data = {
        "article": "Pet door",
        "depth": 0,
        "ignore_list": [
            "string"
        ],
        "percentile": 0
    }
    response = client.post('/keywords', json=data)
    assert response.status_code == 200
    assert 'dog' in response.text
