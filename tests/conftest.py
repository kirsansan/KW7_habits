import pytest
from pytest_factoryboy import register

from tests.factories import UserFactory

# Factories

register(UserFactory)


@pytest.fixture()
@pytest.mark.django_db
def token(client, django_user_model):
    email = "testuser@example.com"
    password = "12345"
    last_name = "testuser"
    telegram_username = "11122233344"

    django_user_model.objects.create_user(
        email=email, password=password, last_name=last_name, telegram_username=telegram_username
    )

    response = client.post(
        "/user/token/",
        {"email": email, "password": password},
        format='json'
    )

    return response.data["access"]

# import pytest
# from model_bakery import baker
# from rest_framework.test import APIClient
#
#
# @pytest.fixture
# def user():
#     user = baker.make_recipe('users.user')
#     user.set_password("password123")
#     return user
#
#
# @pytest.fixture
# def client():
#     client = APIClient()
#     return client


# @pytest.fixture(autouse=True)
# def reset_db_before_test():
#     # Вызывает db.reset_db() перед каждым тестом
#     db.reset_db()
