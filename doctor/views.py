# doctor_app/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import requests

def doctor_view(request):
    # Make a request to the model app to get the model output data
    model_app_url = 'http://localhost:8000/model-app/get-model-output-data/'  # Adjust the URL
    response = requests.get(model_app_url)

    # Process the response and extract the model output data
    model_output_data = response.json()

    # Pass the model output data to the template for rendering
    return render(request, 'Template/remedic/doctor.html', {'model_output_data': model_output_data})


@csrf_exempt  # Using csrf_exempt for simplicity, consider CSRF protection in a production environment
def doctorfeedback_view(request):
    if request.method == 'POST':
        try:
            feedback_data = json.loads(request.body)
            
            # Process the feedback_data, update your model or perform other actions

            # Example: Print feedback_data
            print("Received feedback from the doctor:", feedback_data)

            return JsonResponse({'status': 'success'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
# views.py in the doctor app
from .models import DoctorFeedback


def db_store(request):
    if request.method == 'POST':
        # Assuming you have received feedback data from the frontend
        patient_name = request.POST.get('patientName')
        age = request.POST.get('patientAge')
        sex = request.POST.get('patientSex')
        past_medical_history = request.POST.get('patientHistory')
        symptom_days = request.POST.get('symptomDays')
        symptoms = request.POST.get('patientSymptoms')
        output_field_1 = request.POST.get('outputField1')
        output_field_2 = request.POST.get('outputField2')
        feedback_text = request.POST.get('feedbackText')  # Assuming you have an input field for feedback

        # Save feedback to the database
        feedback = DoctorFeedback(
            patient_name=patient_name,
            age=age,
            sex=sex,
            past_medical_history=past_medical_history,
            symptom_days=symptom_days,
            symptoms=symptoms,
            output_field_1=output_field_1,
            output_field_2=output_field_2,
            feedback_text=feedback_text
        )
        feedback.save()

        # Redirect or return a response as needed
        return redirect('doctor_dashboard')  # Adjust the URL name

    # Rest of your existing code for rendering the doctor dashboard

