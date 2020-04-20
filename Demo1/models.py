from django.db import models

# Create your models here.
class Demo(models.Model):

    bookname=models.CharField(max_length=15)
    bookauthor=models.CharField(max_length=20)
    bookprice=models.IntegerField()
