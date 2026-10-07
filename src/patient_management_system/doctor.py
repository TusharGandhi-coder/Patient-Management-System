from fastapi import APIRouter, HTTPException
from patient_management_system.models import Doctor

router = APIRouter()

doctors_db: list[Doctor] = []
next_doctor_id = 1


@router.get("/doctors", response_model=list[Doctor])
def get_doctors() -> list[Doctor]:
    return doctors_db


@router.get("/doctors/{doctor_id}", response_model=Doctor)
def get_doctor(doctor_id: int) -> Doctor:
    for doctor in doctors_db:
        if doctor.id == doctor_id:
            return doctor
    raise HTTPException(status_code=404, detail="Doctor not found")


@router.put("/doctors/{doctor_id}", response_model=Doctor)
def update_doctor(doctor_id: int, updated_doctor: Doctor) -> Doctor:
    for i, doctor in enumerate(doctors_db):
        if doctor.id == doctor_id:
            updated_doctor.id = doctor_id
            doctors_db[i] = updated_doctor
            return updated_doctor
    raise HTTPException(status_code=404, detail="Doctor not found")


@router.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int) -> dict[str, str]:
    for i, doctor in enumerate(doctors_db):
        if doctor.id == doctor_id:
            del doctors_db[i]
            return {"message": "Doctor deleted"}
    raise HTTPException(status_code=404, detail="Doctor not found")


@router.post("/doctors", response_model=Doctor)
def create_doctor(doctor: Doctor) -> Doctor:
    global next_doctor_id
    doctor.id = next_doctor_id
    next_doctor_id += 1
    doctors_db.append(doctor)
    return doctor
