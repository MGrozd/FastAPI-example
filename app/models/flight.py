from datetime import datetime
from pydantic import BaseModel
from .aircraft import Aircraft


class Flight(BaseModel):
    departure_airport: str
    arrival_airport: str
    departure_datetime: datetime
    arrival_datetime: datetime
    assigned_aircraft: Aircraft