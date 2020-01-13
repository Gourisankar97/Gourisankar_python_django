from django.db import models


class Api(models.Model):
    Fname = models.CharField(max_length=20)
    Mname = models.CharField(max_length=20)
    Lname = models.CharField(max_length=20)
    age = models.CharField(max_length=5)
    Gender = models.CharField(max_length=5)
    phone_no = models.CharField(max_length=10)
    Qualification = models.CharField(max_length=100)
    R_o_v = models.CharField(max_length=100)

