from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_admin = models.BooleanField('is admin',default=False)
    is_staff = models.BooleanField('is staff',default=False)
    is_student = models.BooleanField('is student',default=False)


Type_choices =(
    ("Principal office","Principal office"),
    ("Department","Department "),
    ("Dean Academics","Dean Academics"),
)

nu_choices =(
    ("Student_file","Student_file"),
    ("Faculty_file","Faculty_file"),
    ("common_file","common_file"),
    ("Admin","Admin"),
)

class file(models.Model):
    name=models.CharField(max_length=100)
    date=models.DateTimeField(default=datetime.now,blank=True)
    source=models.CharField(max_length=100,choices=Type_choices)
    fo=models.CharField(max_length=100,choices=nu_choices)
    files=models.FileField(upload_to='file_folder/',max_length=250,default=None)

class Students(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    Usn=models.CharField(max_length=10,unique=True)
    Email=models.EmailField(max_length=100)
    Sem=models.IntegerField()

class Faculty(models.Model):
    Name=models.CharField(max_length=100,unique=True)
    Ssn=models.CharField(max_length=10,unique=True)
    Email=models.EmailField(max_length=100)


