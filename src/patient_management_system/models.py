from pydantic import BaseModel, Field


class Patient(BaseModel):
    id: int
    name: str = Field(..., min_length=1)
    age: int = Field(..., gt=0, lt=150)
    gender: str = Field(..., min_length=1)
    phone: str = Field(..., min_length=1)
    address: str = Field(..., min_length=1)
    symptoms: list[str] = Field(default_factory=list)
