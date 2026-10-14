from fastapi import APIRouter, HTTPException
from patient_management_system.models import Prescription

router = APIRouter()

prescriptions_db: list[Prescription] = []
next_prescription_id = 1


@router.get("/prescriptions", response_model=list[Prescription])
def get_prescriptions() -> list[Prescription]:
    return prescriptions_db


@router.get("/prescriptions/{prescription_id}", response_model=Prescription)
def get_prescription(prescription_id: int) -> Prescription:
    for prescription in prescriptions_db:
        if prescription.id == prescription_id:
            return prescription
    raise HTTPException(status_code=404, detail="Prescription not found")


@router.put("/prescriptions/{prescription_id}", response_model=Prescription)
def update_prescription(prescription_id: int, updated_prescription: Prescription) -> Prescription:
    for i, prescription in enumerate(prescriptions_db):
        if prescription.id == prescription_id:
            updated_prescription.id = prescription_id
            prescriptions_db[i] = updated_prescription
            return updated_prescription
    raise HTTPException(status_code=404, detail="Prescription not found")


@router.delete("/prescriptions/{prescription_id}")
def delete_prescription(prescription_id: int) -> dict[str, str]:
    for i, prescription in enumerate(prescriptions_db):
        if prescription.id == prescription_id:
            del prescriptions_db[i]
            return {"message": "Prescription deleted"}
    raise HTTPException(status_code=404, detail="Prescription not found")


@router.post("/prescriptions", response_model=Prescription)
def create_prescription(prescription: Prescription) -> Prescription:
    global next_prescription_id
    prescription.id = next_prescription_id
    next_prescription_id += 1
    prescriptions_db.append(prescription)
    return prescription
