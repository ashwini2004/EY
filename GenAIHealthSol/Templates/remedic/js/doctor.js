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
    document.getElementById('patientName').innerText = response_data.patient_details.name;
    document.getElementById('patientAge').innerText = response_data.patient_details.age;
    document.getElementById('patientSex').innerText = response_data.patient_details.sex;
    document.getElementById('patientHistory').innerText = response_data.patient_details.past_medical_history;
    document.getElementById('symptomDays').innerText = response_data.patient_details.symptom_days;
    document.getElementById('patientSymptoms').innerText = response_data.patient_details.symptoms;

    // Update model output data
    document.getElementById('outputField1').innerText = response_data.model_output_data.outputField1;
    document.getElementById('outputField2').innerText = response_data.model_output_data.outputField2;
    // Update other model output fields similarly
});
