# seed data: command: python seed_data.py
# using package django-seed: https://pypi.org/project/django-seed/
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django_seed import Seed
from faker import Faker
from polls.models import Department

# create instant
seeder = Seed.seeder('ja_JP')
fake = Faker(['ja_JP'])

# seeder 4 Department
seeder.add_entity(Department, 4, {
    'name': (lambda x: fake.name()),
    # 'city': seeder.faker.city(),
    'city': 'HN',
})

# get list id of data
inserted_pks = seeder.execute()
a = list(inserted_pks.keys())[0]
print(inserted_pks[a])
