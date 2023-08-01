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
    
class Footer(models.Model):
    link = models.CharField(max_length=200)
    class1= models.CharField(max_length=200)
    class2= models.CharField(max_length=200)
    class3= models.CharField(max_length=200)
    def __str__(self):
        return self.title