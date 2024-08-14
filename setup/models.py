from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass


class Company(models.Model):
    company_name = models.CharField(max_length=30)
    since_year = models.IntegerField()
    slogan = models.CharField(max_length=60)
    vision = models.TextField(max_length=400)

    def __str__(self):
        return self.company_name
