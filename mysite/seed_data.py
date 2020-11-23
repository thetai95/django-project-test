import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django_seed import Seed
from faker import Faker

seeder = Seed.seeder()

from polls.models import Department

seeder.add_entity(Department, 4)

inserted_pks = seeder.execute()
# print(list(inserted_pks.keys()))
a = list(inserted_pks.keys())[0]
print(inserted_pks[a])

