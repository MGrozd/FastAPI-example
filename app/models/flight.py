from datetime import datetime
from pydantic import BaseModel
from .aircraft import Aircraft


class Flight(BaseModel):
    flight_number: str  # unique number of flight
    departure_airport_code: str
    arrival_airport_code: str
    departure_datetime: str
    arrival_datetime: str
    assigned_aircraft: Aircraft = None


class FlightsId(BaseModel):
    flights_number: list[str] = []


class FlightsInfo(BaseModel):
    flights: list[Flight] = []

