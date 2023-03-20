import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','event_management_application.settings')
import django
django.setup()
from event_management_application.models import *

from faker import Faker
fakegen = Faker()
import random

fake_name = ['jash','milan','malay','vikram','vijeet']

def populate():
    for entry in range():
        emp = Employee.objects.get_or_create(first_name=random.choice(fake_name))[0]

        emp.save()

if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate()
    print('Populating Complete')

    