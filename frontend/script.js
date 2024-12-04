// Function to confirm submission of operation scheduling
document.addEventListener("DOMContentLoaded", function() {
    const scheduleForm = document.querySelector('form[action="/schedule"]');
    const addPatientForm = document.querySelector('form[action="/add_patient"]');

    // Confirm before scheduling an operation
    if (scheduleForm) {
        scheduleForm.addEventListener("submit", function(event) {
            const patientId = document.getElementById("patient_id").value;
            const operationType = document.getElementById("operation_type").value;
            const operationDate = document.getElementById("operation_date").value;

            const confirmation = confirm(`Are you sure you want to schedule ${operationType} for Patient ID ${patientId} on ${operationDate}?`);
            if (!confirmation) {
                event.preventDefault(); // Prevent form submission if not confirmed
            }
        });
    }

    // Confirm before adding a new patient
    if (addPatientForm) {
        addPatientForm.addEventListener("submit", function(event) {
            const name = document.getElementById("name").value;
            const age = document.getElementById("age").value;

            const confirmation = confirm(`Are you sure you want to add patient ${name}, Age: ${age}?`);
            if (!confirmation) {
                event.preventDefault(); // Prevent form submission if not confirmed
            }
        });
    }
});
