from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.status

class Patient(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name

class Doctor(models.Model):
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=100, null=True)
    doj = models.DateField(null=True)
    dob = models.DateField(null=True)
    image = models.FileField(null=True)

    def __str__(self):
        return self.user.first_name

class Type(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

class Disease(models.Model):
    name = models.CharField(max_length=100, null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    symptom = models.TextField(null=True)

    def __str__(self):
        return self.name+" "+self.type.name

class Feedback(models.Model):
    user = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    messages = models.TextField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return self.user.user.username

class Searched_Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True)
    disease = models.CharField(max_length=100, null=True)
    symptom = models.CharField(max_length=1000,null=True)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    date1 = models.DateTimeField(null=True)

    def __str__(self):
        return self.user.user.username+" "+self.doctor.user.username

class Searched_symptom2(models.Model):
    idso = models.CharField(max_length=1000, null=True)
    name = models.CharField(max_length=1000, null=True)
    name1 = models.CharField(max_length=1000, null=True)
    name2 = models.CharField(max_length=1000, null=True)
    num = models.IntegerField(null=True)

    def __str__(self):
        return self.idso