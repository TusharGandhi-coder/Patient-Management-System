from fastapi import APIRouter, HTTPException
from patient_management_system.models import Diagnosis

router = APIRouter()

diagnoses_db: list[Diagnosis] = []
next_diagnosis_id = 1


@router.get("/diagnoses", response_model=list[Diagnosis])
def get_diagnoses() -> list[Diagnosis]:
    return diagnoses_db


@router.get("/diagnoses/{diagnosis_id}", response_model=Diagnosis)
def get_diagnosis(diagnosis_id: int) -> Diagnosis:
    for diagnosis in diagnoses_db:
        if diagnosis.id == diagnosis_id:
            return diagnosis
    raise HTTPException(status_code=404, detail="Diagnosis not found")


@router.put("/diagnoses/{diagnosis_id}", response_model=Diagnosis)
def update_diagnosis(diagnosis_id: int, updated_diagnosis: Diagnosis) -> Diagnosis:
    for i, diagnosis in enumerate(diagnoses_db):
        if diagnosis.id == diagnosis_id:
            updated_diagnosis.id = diagnosis_id
            diagnoses_db[i] = updated_diagnosis
            return updated_diagnosis
    raise HTTPException(status_code=404, detail="Diagnosis not found")


@router.delete("/diagnoses/{diagnosis_id}")
def delete_diagnosis(diagnosis_id: int) -> dict[str, str]:
    for i, diagnosis in enumerate(diagnoses_db):
        if diagnosis.id == diagnosis_id:
            del diagnoses_db[i]
            return {"message": "Diagnosis deleted"}
    raise HTTPException(status_code=404, detail="Diagnosis not found")


@router.post("/diagnoses", response_model=Diagnosis)
def create_diagnosis(diagnosis: Diagnosis) -> Diagnosis:
    global next_diagnosis_id
    diagnosis.id = next_diagnosis_id
    next_diagnosis_id += 1
    diagnoses_db.append(diagnosis)
    return diagnosis
