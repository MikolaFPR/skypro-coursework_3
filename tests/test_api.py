import pytest
from main import app
import json

data = "data/posts.json"


def test_api_posts():
    response = app.test_client().get("/api/posts")

    assert response.status_code == 200, 'Возвращается неверный код'
    assert type(data) == str, 'Должен возвращаться строку'


def test_api_current_post():
    response = app.test_client().get('/api/posts/1')

    assert response.status_code == 200, 'Возвращается неверный код'

