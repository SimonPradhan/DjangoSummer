from django.db import models

# Create your models here
class Blog (models.Model):
    title = models.CharField(max_length=200)
    subheading = models.CharField(max_length=200, default="This is subheading")
    description = models.TextField()

    def __str__(self):
        return self.title

class Contacts(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class User(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    email = models.EmailField()
    phoneNumber = models.IntegerField()

    def __str__(self):
        return self.firstname