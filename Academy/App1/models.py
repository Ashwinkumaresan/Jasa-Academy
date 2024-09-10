from django.db import models

# Create your models here.
class FormModel(models.Model):
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Email=models.EmailField()
    City=models.CharField(max_length=100)
    State=models.CharField(max_length=100)
    Zip=models.CharField(max_length=100)
    competition=models.CharField(max_length=100)
    File=models.FileField()

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"

class DonateModel(models.Model):
    Name=models.CharField(max_length=26)
    Date=models.DateField(auto_now_add=True)
    Amount=models.IntegerField()

    def __str__(self):
        return f"{self.Name}-{self.Amount}"
    
class UserDetailModel(models.Model):
    Name=models.EmailField(max_length=26)
    Password=models.CharField(max_length=50)