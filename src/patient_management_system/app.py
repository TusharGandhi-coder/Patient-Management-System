from fastapi import FastAPI
from patient_management_system.models import Patient

app = FastAPI(title="Patient Management System")

patients_db: list[Patient] = []
next_patient_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Patient Management System API is running"}


@app.get("/patients", response_model=list[Patient])
def get_patients() -> list[Patient]:
    return patients_db


@app.post("/patients", response_model=Patient)
def create_patient(patient: Patient) -> Patient:
    global next_patient_id
    patient.id = next_patient_id
    next_patient_id += 1
    patients_db.append(patient)
    return patient
