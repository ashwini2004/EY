from django.shortcuts import render
from doctor.models import DoctorFeedback


def index(request):
    return render(request, 'index.html')

def generate_reports(request):
    # Retrieve doctor feedback data from the database
    feedback_data = DoctorFeedback.objects.all()

    # Process the feedback data or perform any additional logic as needed
    # ...

    # Pass the processed data to the template for rendering
    return render(request, 'user_app/reports.html', {'feedback_data': feedback_data})
