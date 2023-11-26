from django.shortcuts import render
from django.http import JsonResponse
from .models import PatientDetails
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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

    return render(request, 'Templates/remedic/symptomsform.html')



batch_feedback_data = []

def feedback_view(request):
    global batch_feedback_data

    if request.method == 'POST':
        try:
            # Retrieve the feedback data from the request
            feedback_data = json.loads(request.body.decode('utf-8'))

            # Extract relevant information from the feedback_data
            edited_data = feedback_data.get('edited_data', {})

            # Append the edited_data to the batch_feedback_data
            batch_feedback_data.append(edited_data)

            # Check if the batch size is reached
            batch_size = 500
            if len(batch_feedback_data) >= batch_size:
                # Send the batch to the model endpoint
                model_endpoint = 'https://your-model-endpoint'
                response = requests.post(model_endpoint, json=batch_feedback_data)

                # Clear the batch_feedback_data after sending
                batch_feedback_data = []

                # Assuming the model update is successful, you can return a success response
                return JsonResponse({'status': 'success'})
            
            # Return a success response indicating that the feedback is recorded
            return JsonResponse({'status': 'success'})

        except Exception as e:
            # Handle exceptions or errors during the feedback processing
            return JsonResponse({'status': 'error', 'message': str(e)})

    # Handle other HTTP methods if needed
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
