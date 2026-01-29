from pydantic import BaseModel
from typing import Optional


class AppointmentEntities(BaseModel):
    patient_name: Optional[str] = None
    visit_reason: Optional[str] = None
    preferred_doctor: Optional[str] = None
    appointment_date: Optional[str] = None
    appointment_time: Optional[str] = None


class IntentResult(BaseModel):
    intent: str
    entities: AppointmentEntities
