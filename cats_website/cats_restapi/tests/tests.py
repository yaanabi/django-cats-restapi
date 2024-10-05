import pytest 
from django.urls import reverse


def test_user_unauthorized_get_breeds(api_client):
    response = api_client.get('/breeds/')
    assert response.status_code == 401

def test_user_unauthorized_get_cats(api_client):
    response = api_client.get('/cats/')
    assert response.status_code == 401

def test_user_unauthorized_get_cat(api_client):
    response = api_client.get('/cats/1/')
    assert response.status_code == 401

def test_user_unauthorized_create_cat(api_client):
    response = api_client.post('/cats/', data={'name': 'test'})
    assert response.status_code == 401

def test_user_unauthorized_delete_cat(api_client):
    response = api_client.delete('/cats/1/')
    assert response.status_code == 401

def test_user_unauthorized_update_cat(api_client):
    response = api_client.patch('/cats/1/', data={'name': 'test'})
    assert response.status_code == 401

def test_user_get_breeds(api_client, get_jwt_access_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(get_jwt_access_token))
    response = api_client.get('/breeds/')
    assert response.status_code == 200
    assert len(response.data) == 3

def test_user_create_cat(api_client, get_jwt_access_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(get_jwt_access_token))
    response = api_client.post('/cats/', data={'name': 'testcat', 'breed': 'Brittish', 'age': 2, 'color': 'red', 'description': 'test description'})
    assert response.status_code == 201
    assert response.data['name'] == 'testcat'
    assert response.data['breed'] == 'Brittish'
    assert response.data['age'] == 2
    assert response.data['color'] == 'red'
    assert response.data['description'] == 'test description'
    assert response.data['owner'] == 'test_user'

def test_user_update_cat(api_client, get_jwt_access_token):
    api_client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(get_jwt_access_token))
    response = api_client.patch('/cats/1/', data={'name': 'testcat', 'breed': 'Brittish', 'age': 2, 'color': 'red', 'description': 'test description'})
    assert response.status_code == 200

def test_user_get_cats(api_client, get_jwt_access_token):
    pass

def test_user_get_cats_by_breed(api_client, get_jwt_access_token):
    pass

def test_user_delete_cat(api_client, get_jwt_access_token):
    pass

def test_user_get_cat(api_client, get_jwt_access_token):
    pass

def test_user_rate_cat(api_client, get_jwt_access_token):
    pass

def test_user_rate_the_same_cat_twice(api_client, get_jwt_access_token):
    pass

def test_user_get_ratings(api_client, get_jwt_access_token):
    pass

