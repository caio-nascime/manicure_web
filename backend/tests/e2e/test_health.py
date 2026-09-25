import pytest

def test_health_check_return_200(create_client):

    response = create_client.get("/health_check")

    assert response.status_code == 200
    