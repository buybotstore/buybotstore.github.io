from django.db import models
from django.utils import timezone

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
    price = models.DecimalField(max_digits=10,decimal_places=3)
    description = models.TextField(max_length=500)





class Client(models.Model):
    full_name = models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)


class Purchase(models.Model):
    id_bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date = models.DateField()

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title