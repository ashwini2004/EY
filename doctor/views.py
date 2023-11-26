# doctor_app/views.py

from django.shortcuts import render
import requests

def doctor_view(request):
    # Make a request to the model app to get the model output data
    model_app_url = 'http://localhost:8000/model-app/get-model-output-data/'  # Adjust the URL
    response = requests.get(model_app_url)

    # Process the response and extract the model output data
    model_output_data = response.json()

    # Pass the model output data to the template for rendering
    return render(request, 'doctor_app/doctor_template.html', {'model_output_data': model_output_data})
