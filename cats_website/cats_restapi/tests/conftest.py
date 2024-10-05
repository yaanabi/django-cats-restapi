import pytest
from django.contrib.auth.models import User 
from rest_framework_simplejwt.tokens import AccessToken


@pytest.fixture(autouse=True)
def load_test_data(db):
    """Load test data from 'data_populate.yaml' into the database."""
    from django.core.management import call_command
    call_command('loaddata', 'data_populate')

@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()

@pytest.fixture
def create_user(db) -> User:
    def make_user(**kwargs):
        return User.objects.create_user(**kwargs)
    return make_user

@pytest.fixture
def get_jwt_access_token(create_user) -> AccessToken:
    user = create_user(username='test_user', password='test_password')
    access_token = AccessToken.for_user(user)
    return access_token

