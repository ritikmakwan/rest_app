from django.db import models

# Create your models here.
class Emp(models.Model):
    name=models.CharField(max_length=20)
    sal=models.IntegerField()
    position=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    
class Products(models.Model):
    name=models.CharField(max_length=20)
    price=models.IntegerField()
    category=models.CharField(max_length=20)
    company=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.name
    