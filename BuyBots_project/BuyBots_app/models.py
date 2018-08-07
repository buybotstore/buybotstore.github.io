from django.db import models
from django.utils import timezone


class Admin(models.Model):
    id_admin = models.AutoField(primary_key=True)


class Developer(models.Model):
    id_developer = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.full_name


class Deal(models.Model):
    id_deal = models.AutoField(primary_key=True)
    id_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)


class Bot(models.Model):
    id_bot = models.AutoField(primary_key=True)
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.full_name


class Purchase(models.Model):
    id_purchase = models.AutoField(primary_key=True)
    id_bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Post(models.Model):
    id_post = models.AutoField(primary_key=True)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Password(models.Model):
    id_password = models.AutoField(primary_key=True)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    client_password = models.CharField(max_length=20)
    developer_password = models.CharField(max_length=20)
