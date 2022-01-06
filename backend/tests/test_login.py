import pytest
from app.main import app
from app.main import UserInput
from fastapi import HTTPException
from fastapi.testclient import TestClient

client = TestClient(app)


def test_login():
    response = client.post(
        "/login", data={"username": "henrikpoelse@stud.kea.dk", "password": "123456"}
    )
    assert response.status_code == 200

    response = client.post(
        "/login", data={"username": "wrong_username", "password": "wrong_password"}
    )
    assert response.status_code == 400

    response = client.post(
        "/login",
        data={"username": "henrikpoelse@stud.kea.dk", "password": "wrong_password"},
    )
    assert response.status_code == 400


def test_input():
    assert UserInput(username="henrikpoelse@stud.kea.dk")
    assert UserInput(username="henrikpoelse@stud.kea.dk", password=123456)
    assert UserInput(password=123456)

    with pytest.raises(HTTPException):
        assert UserInput(username="21")

    with pytest.raises(HTTPException):
        assert UserInput(
            username="thisusernameissuperlongonpurposeandwillraiseahttpexception"
        )

    with pytest.raises(HTTPException):
        assert UserInput(password="")

    with pytest.raises(HTTPException):
        assert UserInput(password="superlongpasswordtotestlengthofpasswordandstuff")
