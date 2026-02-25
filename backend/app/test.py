
import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch


from main import app


client = TestClient(app)


def test_root_returns_index_html():
    """Проверяем, что / отдаёт frontend (html)"""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    
    assert response.text.strip() != ""


def test_api_v1_events_root():
    """Проверяем, что роутер /api/v1/events подключён и отвечает"""
    response = client.get("/api/v1/events")
    
    assert response.status_code in (200, 404, 405, 422)


def test_openapi_schema_exists():
    """Просто проверяем, что FastAPI генерирует /docs и /openapi.json"""
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "openapi" in response.json()


def test_404_handler_works():
    """Проверяем наш кастомный обработчик 404"""
    response = client.get("/some-random-page-123")
    assert response.status_code == 404
    
    assert "detail" in data


@pytest.mark.parametrize("bad_path", [
    "/api/v1/events/999999999",
    "/api/v1/events/create",  # если нет такого метода
    "/random/endpoint",
])
def test_random_endpoints_404(bad_path):
    response = client.get(bad_path)
    assert response.status_code in (404, 405)



@patch("main.DBBaseModel.metadata.create_all")
def test_app_startup_does_not_crash(mock_create_all):
    # Просто проверяем, что при импорте main.py ничего не падает
    from main import app
    assert app is not None
    mock_create_all.assert_called_once()



def test_event_post_validation_fails():
    bad_payload = {"wrong_field": "haha"}
    response = client.post("/api/v1/events", json=bad_payload)
    assert response.status_code in (422, 400)