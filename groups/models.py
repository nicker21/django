import random

from django.db import models
from faker import Faker

# Create your models here.
class Group(models.Model) :
    name = models.CharField(max_length=50 , null=False)\

    def __str__(self):
        return f'{self.name}, {self.id}'

    @staticmethod
    def generate_group(count):
        faker = Faker()
        for _ in range(count):
            st = Group(
                name=random.choice(['Python', 'PHP', 'JS']),
            )

            st.save()
