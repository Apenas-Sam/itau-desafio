import pytest

from fastapi.testclient import TestClient

from src.app import app
# from src.sql.conn import session
from src.router.models import Resume,Search


client = TestClient(app)

resume_assert = Resume(
    url="https://pt.wikipedia.org/wiki/LinkedIn",
    char_amount=1000,
    resume="",
)

search_assert = Search(
    url="https://pt.wikipedia.org/wiki/LinkedIn"
)

def test_create_resume():
    resume_data = {
        "url": "https://pt.wikipedia.org/wiki/LinkedIn",
        "char_amount": 1000,
    }
    response = client.post("/resume", json=resume_data)
    assert response.status_code == 200

def test_search_resume():
    resume_data = {
        "url": "https://pt.wikipedia.org/wiki/LinkedIn",
        "char_amount": 1000,
    }
    response = client.post("/resume", json=resume_data)
    assert response.status_code == 200


def test_search_consult():
    consult_data = {
        "url": "https://pt.wikipedia.org/wiki/LinkedIn",
    }
    response = client.post("/consult", json=consult_data)
    assert response.status_code == 200