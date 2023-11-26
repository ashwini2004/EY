# models.py in the doctor app
from django.db import models

class DoctorFeedback(models.Model):
    patient_name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    past_medical_history = models.TextField()
    symptom_days = models.IntegerField()
    symptoms = models.TextField()
    output_field_1 = models.CharField(max_length=255)  # Replace with the actual type you need
    output_field_2 = models.CharField(max_length=255)  # Replace with the actual type you need
    feedback_text = models.TextField()

    def __str__(self):
        return f"Feedback for {self.patient_name}"
