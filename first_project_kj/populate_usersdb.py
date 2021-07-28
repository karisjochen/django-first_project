
import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project_kj.settings')

import django
django.setup()
import random
from users_app.models import Users
from faker import Faker

fakegen = Faker()
def add_user(N=5):
    for n in range(N):
        first = fakegen.name().split()[0]
        last = fakegen.name().split()[1]
        e = fakegen.email()
        # this returns an object so have to use [0] for the tuple unpacking
        user = Users.objects.get_or_create(fname=first, lname=last, email=e)[0]
        user.save() # is this line necessary?
    


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    add_user(20)
    print('Populating Complete')
