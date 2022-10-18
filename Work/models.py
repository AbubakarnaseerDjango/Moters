from audioop import reverse
import email
from unicodedata import name
from django.db import models

# Create your models here.

class Contact(models.Model):
    name  = models.CharField(max_length = 30)
    email = models.EmailField(max_length=20 , null = True)
    subject = models.CharField(max_length=40)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name

class Catagry(models.Model):
    naam = models.CharField(max_length=40)

    def __str__(self) -> str:
        return self.naam

class Product(models.Model):
    image = models.ImageField(upload_to='images' , null = True , blank = True)
    description = models.TextField(max_length = 100)
    price = models.DecimalField(max_digits = 10, decimal_places=2  )
    catagry = models.ForeignKey(Catagry, on_delete=models.CASCADE,default=True,null=False )

    def __str__(self):
     
       return "pkr "+str(self.price)

    



class CustomerServices(models.Model):
    name = models.CharField(max_length=10)
    details = models.TextField(max_length= 500)

    def __str__(self) :
        return self.name