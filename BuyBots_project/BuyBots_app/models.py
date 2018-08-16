from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Admin(models.Model):
    pass


class Developer(models.Model):
    full_name = models.CharField(max_length=100)
    en_full_name= models.CharField(max_length=100)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.en_full_name


class Deal(models.Model):
    id_admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Bot(models.Model):
    id_developer = models.ForeignKey(Developer, on_delete=models.CASCADE, null=True)
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    en_name= models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    description = models.TextField(max_length=500)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    id_bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    id_client = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField()


class Comment(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_bot = models.ForeignKey(Bot, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    comment = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class Response(models.Model):
    id_comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
     
 
