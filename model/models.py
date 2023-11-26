from django.db import models

class PatientDetails(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    past_medical_history = models.TextField()
    symptom_days = models.IntegerField()
    symptoms = models.TextField()
