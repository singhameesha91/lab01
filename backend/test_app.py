from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_message():
    response = client.get("/message")
    assert response.status_code == 200
