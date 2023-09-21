import pytest
from django.test import Client

from users.models import User


@pytest.mark.django_db
class TestUserAuthentication:
    def test_user_create(self):
        """Test user create"""
        client = Client()
        response = client.post(
            '/users/',
            {'email': 'tompson@london.uk', 'password': '12345'},
            content_type='application/json',
        )
        expected_response = {'id': 1, 'email': 'tompson@london.uk', 'last_name': ''}
        assert response.status_code == 201
        #assert response.data == expected_response


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
