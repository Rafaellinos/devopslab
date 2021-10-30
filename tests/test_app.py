# -*- coding: utf-8 -*-
from app import app
import pytest


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.mark.app_test
def test_app_raiz(client):
    res = client.get("/")
    assert res.data.decode('utf-8') == "Laboratório Pipeline DevOps" and res.status_code == 200


@pytest.mark.app_test
def test_app_soma(client):
    soma = client.get("/soma")
    assert soma.data.decode('utf-8') == "Sua soma de 10+10=20" and soma.status_code == 200
