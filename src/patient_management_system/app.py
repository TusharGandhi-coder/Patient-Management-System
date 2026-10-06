from fastapi import FastAPI, HTTPException
from patient_management_system.models import Patient
from patient_management_system.doctor import router as doctor_router

app = FastAPI(title="Patient Management System")
app.include_router(doctor_router)

patients_db: list[Patient] = []
next_patient_id = 1


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Patient Management System API is running"}


@app.get("/patients", response_model=list[Patient])
def get_patients() -> list[Patient]:
    return patients_db


@app.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int) -> Patient:
    for patient in patients_db:
        if patient.id == patient_id:
            return patient
    raise HTTPException(status_code=404, detail="Patient not found")


@app.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, updated_patient: Patient) -> Patient:
    for i, patient in enumerate(patients_db):
        if patient.id == patient_id:
            updated_patient.id = patient_id
            patients_db[i] = updated_patient
            return updated_patient
    raise HTTPException(status_code=404, detail="Patient not found")


@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int) -> dict[str, str]:
    for i, patient in enumerate(patients_db):
        if patient.id == patient_id:
            del patients_db[i]
            return {"message": "Patient deleted"}
    raise HTTPException(status_code=404, detail="Patient not found")


@app.post("/patients", response_model=Patient)
def create_patient(patient: Patient) -> Patient:
    global next_patient_id
    patient.id = next_patient_id
    next_patient_id += 1
    patients_db.append(patient)
    return patient
