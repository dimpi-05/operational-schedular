from flask import Blueprint, render_template, request, redirect, url_for
from database import db, Patient, Operation

main = Blueprint('main', __name__)

@main.route('/')
def index():
    operations = Operation.query.all()
    return render_template('index.html', operations=operations)

@main.route('/schedule', methods=['POST'])
def schedule_operation():
    patient_id = request.form['patient_id']
    operation_date = request.form['operation_date']
    operation_type = request.form['operation_type']

    new_operation = Operation(patient_id=patient_id, operation_date=operation_date, operation_type=operation_type)
    db.session.add(new_operation)
    db.session.commit()
    return redirect(url_for('main.index'))

# Add more routes for managing patients and operations
