from django.db import models
from faker import Faker

# Create your models here.
class Group(models.Model) :
    name = models.CharField(max_length=50 , null=False)\



    @staticmethod
    def generate_group(count):
        faker = Faker()
        for _ in range(count):
            st = Group(
                name=faker.name_name(),

            )

            st.save()
