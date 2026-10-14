from pydantic import BaseModel, Field


class Patient(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0, lt=150)
    gender: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)
    address: str = Field(..., min_length=1)
    symptoms: list[str] = Field(default_factory=list)


class Doctor(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    specialization: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)


class Diagnosis(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    diagnosis: str = Field(..., min_length=1)
    notes: str = Field(default="")


class Prescription(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    diagnosis_id: int
    medication_name: str = Field(..., min_length=1)
    dosage: str = Field(..., min_length=1)
    frequency: str = Field(..., min_length=1)
    duration: str = Field(..., min_length=1)
    instructions: str = Field(default="")
