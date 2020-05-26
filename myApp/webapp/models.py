from django.db import models

class Employee(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    mobileNumber=models.CharField(max_length=10)

    def __str__(self):
        return self.firstname
    
