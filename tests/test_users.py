from app import schemas
from .database import client, session

def test_root(client):
    res = client.get('/')
    print(res.json().get('message'))
    assert res.json().get('message') == 'Hello World'


def test_create_user(client):
    res = client.post('/users/', json= {"phone_number": "0123", "password": "123"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.phone_number == "0123"
