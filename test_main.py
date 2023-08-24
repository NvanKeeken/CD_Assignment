import pytest

from main import app


@pytest.fixture
def client():
    client = app.test_client()
    return client


def test_home(client):
    response = client.get("/home")
    assert response.status_code == 302
    assert response.location == "/"


def test_index(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"<title>Index</title>" in response.data


def test_about(client):
    response = client.get("/about")
    assert response.status_code == 200
    assert b"<title>About</title>" in response.data
    
# from main import index, requirements

# def test_index():
#     assert index() == "Welcome, to my final winc assignment: CD! I hope it will work, yes!"

# def test_requirments():
#     assert requirements() == "The requirments are: build a continuous deployment using Git Actions"



