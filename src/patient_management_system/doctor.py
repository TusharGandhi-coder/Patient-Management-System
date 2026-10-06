from fastapi import APIRouter
from patient_management_system.models import Doctor

router = APIRouter()

doctors_db: list[Doctor] = []
next_doctor_id = 1


@router.get("/doctors", response_model=list[Doctor])
def get_doctors() -> list[Doctor]:
    return doctors_db


@router.post("/doctors", response_model=Doctor)
def create_doctor(doctor: Doctor) -> Doctor:
    global next_doctor_id
    doctor.id = next_doctor_id
    next_doctor_id += 1
    doctors_db.append(doctor)
    return doctor
