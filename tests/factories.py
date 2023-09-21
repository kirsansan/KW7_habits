import factory


from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker('email')
    phone = factory.Faker('phone')
    country = factory.Faker('country')
    last_name = factory.Faker('last_name')
    password = factory.Faker('password')
    telegram_username = factory.Faker('telegram_username')

if __name__ == '__main__':
    t = UserFactory()
    print(t)