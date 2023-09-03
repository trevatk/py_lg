"""Test the HTTP server"""
from fastapi.testclient import TestClient

from src.http_server import app

client = TestClient(app)


def test_health():
    """Test the health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
