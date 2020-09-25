<<<<<<< HEAD
## PopulateDummyDatabase
The purpose is to implement Django application with User and ActivityPeriod models, write
a custom management command to populate the database with some dummy data.and design an 
API to serve that data in json format.

To get it done in a nice way you'll need a combination of Factory Boy, Faker and custom management commands.

### Factory Boy
Factory Boy allows you to create templates for producing valid objects and Faker generates fake data
```bash
pip install factory_boy
```
1) When you install Factory Boy, you also get Faker.
2) Faker is a Python package that generates fake data for you.
It's useful in all the cases when you need to use some dummy data for testing,
population of database during development, etc

For Example:
For  given Model User
```python
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=32)
```
You can define a Factory as follows:

```python
import factory  
import factory.django

class UserFactory(factory.django.DjangoModelFactory):  
    class Meta:
        model = User

    name = factory.Faker('name')
    address = factory.Faker('address')
    phone_number = factory.Faker('phone_number')
```
Then, you can create fake users by calling UserFactory.create().

### custom management command 
Django management commands are Django’s own way of writing command-line interfaces.
The manage.py utilitiy is used to register and run these commands.
we can write our own management commands like in my application,
I am creating it for populating dummy dada for user and its activity.

```python
from django.core.management.base import BaseCommand

# import UserFactory here


class Command(BaseCommand):
    help = 'Seeds the database.'

    def add_arguments(self, parser):
        parser.add_argument('--users',
            default=200,
            type=int,
            help='The number of fake users to create.')

    def handle(self, *args, **options):
        for _ in range(options['users']):
            UserFactory.create()
```

please refere - https://docs.djangoproject.com/en/3.0/howto/custom-management-commands/

### Usage
```bash
$ git clone https://github.com/rohinizade27/PopulateDummyDatabase.git

# In a virtualenv
$ pip install -r requirements.txt

$ python manage.py migrate

$ python manage.py populatedata 100

$ python manage.py runserver
```
=======
# PopulateDummyUserData
>>>>>>> 1f5d4f11f83a969c1287ad6be03355d14e8a1b72
