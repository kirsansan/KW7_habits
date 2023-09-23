import pytest
from django.test import Client
from rest_framework.test import APIClient

# from tests.conftest import token_for_user
from users.models import User


@pytest.mark.django_db
class TestUserCreateAndAuth:
    def test_user_create(self):
        """Test user create"""
        client = Client()
        response = client.post(
            '/users/',
            {'email': 'tompson@london.uk', 'password': '12345'},
            content_type='application/json',
        )
        expected_response = {'id': 1,
                             'last_login': None,
                             'is_superuser': False,
                             'first_name': '',
                             'is_staff': False,
                             'is_active': True,
                             'email': 'tompson@london.uk',
                             'phone': None,
                             'country': None,
                             'avatar': None,
                             'last_name': None,
                             'telegram_username': None,
                             'groups': [],
                             'user_permissions': []}
        assert response.status_code == 201
        response.data.pop('password')       # it doesn't matter
        response.data.pop('date_joined')    # and it to
        assert response.data == expected_response

    def test_get_users(self, client, token):
        response = client.get(
            '/users/',
            HTTP_AUTHORIZATION="Bearer " + token
        )
        assert response.status_code == 200
        assert response.data[0]['email'] == 'testuser@example.com'

    def test_get_users_anonymous(self, client):
        response = client.get(
            '/users/'
        )
        assert response.status_code == 401
        assert response.data['detail'] == 'Учетные данные не были предоставлены.'


@pytest.mark.django_db
class TestUserDetail:

    def test_get_one_user(self, authenticated_user: dict):
        user = authenticated_user.get('user')
        client = authenticated_user.get('client')
        response = client.get(f'/users/{user.pk}/')
        #print(response.data)
        assert response.status_code == 200
        assert response.data['email'] == user.email


@pytest.mark.django_db
def test_factories(random_habit, user):
    print("user:", user)
    print("habit:", random_habit)

