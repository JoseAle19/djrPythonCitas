from enum import unique
from django.db import models

# Create your models here.
class UsersModel(models.Model):
    username = models.CharField(max_length=100, unique= True)
    lastname = models.CharField(max_length=100)
    rol= models.CharField(max_length=100)
    phone= models.CharField(max_length=10, unique= True,)
    email = models.CharField(max_length=100, unique=True, )
    password = models.CharField(max_length=100)




class PatientAppointmentModel(models.Model):
    namePatient = models.CharField(max_length = 100 )
    lastNamePatient = models.CharField(max_length = 100 )
    emailPatient = models.EmailField(max_length = 100 )
    phonePatient = models.CharField(max_length = 10 )
    descriptionPatient = models.TextField()
    dateAppointment = models.DateField()
    appointmentTime = models.TimeField()
    statustAppointment = models.BooleanField()














