import os
from app import app

def test_home(monkeypatch):
    monkeypatch.setenv("YOUR_NAME", "Darren")

    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert b"Hello Darren" in response.data
