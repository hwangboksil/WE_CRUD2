from os import name
from django.db import models
from django.db.models.fields import EmailField

# Create your models here.


class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=300)
    age = models.IntegerField()  # 값이없어서 비워두면된다.

    class Meta:
        db_table = 'owners'


class Dog(models.Model):
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'dogs'
