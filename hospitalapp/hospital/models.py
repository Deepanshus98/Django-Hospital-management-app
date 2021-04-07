from django.db import models

class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    special=models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Patient(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField(null=True)
    gender=models.CharField(max_length=10)
    adress=models.CharField(max_length=150)

    def __str__(self):
        return self.name
class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    date1=models.DateField()
    time1=models.TimeField()


    def __str__(self):
        return self.doctor.name+"--"+self.patient.name
# Create your models here.
