"""Tests for API"""


def test_api_health(client):
    response = client.get("/health")
    assert response.status_code == 200
