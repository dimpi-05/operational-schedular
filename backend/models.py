from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

db = SQLAlchemy()

class Patient(db.Model):
    __tablename__ = 'patients'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    medical_history = db.Column(db.Text)
    operations = db.relationship('Operation', backref='patient', lazy=True)

    def __repr__(self):
        return f'<Patient {self.name}>'

class Operation(db.Model):
    __tablename__ = 'operations'

    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    operation_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    operation_type = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Scheduled')

    def __repr__(self):
        return f'<Operation {self.operation_type} for Patient ID {self.patient_id}>'
