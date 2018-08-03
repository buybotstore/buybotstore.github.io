from django.db import models


class Admin(models.Model):
    pass


class Developer(models.Model):
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)


class Deal(models.Model):
    id_admin = models.ForeignKey()
    id_developer = models.ForeignKey()


class Bot(models.Model):
    id_developer = models.ForeignKey()
    name = models.CharField(max_length=100)
    price = models.DecimalField()
    description = models.TextField(max_length=500)


class Purchase(models.Model):
    id_bot = models.ForeignKey()
    id_client = models.ForeignKey()


class Client(models.Model):
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)




