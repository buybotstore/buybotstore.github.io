from django.db import models


class Admin(models.Model):
    pass
    #id_admin = models.ForeignKey(primary_key=True, on_delete=models.CASCADE)


class Developer(models.Model):
    #id_developer = models.ForeignKey(primary_key=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)


class Deal(models.Model):
    id_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    date = models.DateField()


class Bot(models.Model):
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField()
    description = models.TextField(max_length=500)


class Purchase(models.Model):
    id_bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()


class Client(models.Model):
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)




