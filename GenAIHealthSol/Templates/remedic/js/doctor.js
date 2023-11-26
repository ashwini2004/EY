document.addEventListener("DOMContentLoaded", function() {
    const response_data = {
        'status': 'success',
        'patient_details': {
            'name': 'John Doe',
            'age': 30,
            'sex': 'Male',
            'past_medical_history': 'None',
            'symptom_days': 5,
            'symptoms': 'Fever, Headache'
        },
        'model_output_data': {
            'outputField1': 'Value 1',
            'outputField2': 'Value 2'
            // Add more fields as needed
        }
    };

    // Update patient details
    updateEditableField('patientName', response_data.patient_details.name);
    updateEditableField('patientAge', response_data.patient_details.age);
    updateEditableField('patientSex', response_data.patient_details.sex);
    updateEditableField('patientHistory', response_data.patient_details.past_medical_history);
    updateEditableField('symptomDays', response_data.patient_details.symptom_days);
    updateEditableField('patientSymptoms', response_data.patient_details.symptoms);

    // Update model output data
    updateEditableField('outputField1', response_data.model_output_data.outputField1);
    updateEditableField('outputField2', response_data.model_output_data.outputField2);
    // Update other model output fields similarly

    function updateEditableField(id, value) {
        const element = document.getElementById(id);
        element.innerText = value;
        element.contentEditable = true;  // Make the field editable
        element.addEventListener('blur', function() {
            // Save the edited content to your server (you need to implement this part)
            const editedValue = element.innerText;
            console.log(`Field ${id} edited: ${editedValue}`);
            // Send the edited content to your server for further processing
        });
    }

    const submitBtn = document.getElementById('submitBtn');
    submitBtn.addEventListener('click', function() {
        // Collect the edited data
        const editedData = {
            patient_details: {
                name: document.getElementById('patientName').innerText,
                age: document.getElementById('patientAge').innerText,
                sex: document.getElementById('patientSex').innerText,
                past_medical_history: document.getElementById('patientHistory').innerText,
                symptom_days: document.getElementById('symptomDays').innerText,
                symptoms: document.getElementById('patientSymptoms').innerText,
            },
            model_output_data: {
                outputField1: document.getElementById('outputField1').innerText,
                outputField2: document.getElementById('outputField2').innerText,
                // Add more fields as needed
            }
        };

        // Send the edited data to the feedback endpoint
        fetch('/doctor/feedback/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),  // Ensure to include CSRF token
            },
            body: JSON.stringify({ edited_data: editedData }),
        })
        .then(response => response.json())
        .then(data => {
            // Handle the feedback response as needed
            console.log('Feedback submitted successfully:', data);
        })
        .catch(error => {
            console.error('Error submitting feedback:', error);
        });
    });

    // Function to get CSRF token from cookies
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Search for the csrf token
                if (cookie.startsWith(name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});
