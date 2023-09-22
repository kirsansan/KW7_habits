import pytest
from django.test import Client

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


# @pytest.mark.django_db
# def test_ads_list_view(client, token):
#
#     response = client.get(
#         '/ad/',
#         HTTP_AUTHORIZATION="Bearer " + token
#     )
#
#     assert response.status_code == 200
#     #assert len(response.data['results']) == ads_count
