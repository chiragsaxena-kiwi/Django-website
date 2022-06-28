from django.db import models

class Signup(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)

    def __str__(self):
        return self.username
class qur(models.Model):
    uid = models.CharField(max_length=40,default=0)
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=100) 
    subject = models.CharField(max_length=40,default=0)   
    message = models.CharField(max_length=40,default=0)        