from django.db import models

# Create your models here.
class teachers(models.Model) :
    first_name = models.CharField(max_length=50 , null=False)
    last_name = models.CharField(max_length=80 , null=False)
    age = models.IntegerField(default=42)