from django.shortcuts import render
from django.http import JsonResponse
from .models import PatientDetails
import json
import requests

def details_view(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        age = int(request.POST.get('age'))
        sex = request.POST.get('sex')
        past_medical_history = request.POST.get('history')
        symptom_days = int(request.POST.get('symptomDays'))
        symptoms = request.POST.get('symptoms')

        # Save form data to the database
        patient = PatientDetails(
            name=name,
            age=age,
            sex=sex,
            past_medical_history=past_medical_history,
            symptom_days=symptom_days,
            symptoms=symptoms
        )
        patient.save()

        # Prepare data for the trained model (adjust as needed)
        model_input_data = {
            'name': name,
            'age': age,
            'sex': sex,
            'past_medical_history': past_medical_history,
            'symptom_days': symptom_days,
            'symptoms': symptoms
        }

        # Send data to the trained model (replace 'model_endpoint' with the actual endpoint)
        model_endpoint = 'https://your-trained-model-endpoint'
        response = requests.post(model_endpoint, json=model_input_data)

        # Process the response from the model as needed
        model_output_data = response.json()

        # Combine patient details and model output data
        response_data = {
            'status': 'success',
            'patient_details': {
                'name': name,
                'age': age,
                'sex': sex,
                'past_medical_history': past_medical_history,
                'symptom_days': symptom_days,
                'symptoms': symptoms
            },
            'model_output_data': model_output_data
        }

        # Return a JSON response with the processed data
        return JsonResponse(response_data)

    return render(request, 'symptomsform.html')
