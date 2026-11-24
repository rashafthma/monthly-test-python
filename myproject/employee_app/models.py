from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=10)
    department=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)
    salary=models.IntegerField()
    profile_image=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
    