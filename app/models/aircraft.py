from pydantic import BaseModel


class Aircraft(BaseModel):
    serial_number: str
    manufacturer: str


class AircraftsId(BaseModel):
    aircrafts_serial_number: list[str] = []


class AircraftsInfo(BaseModel):
    aircrafts: list[Aircraft] = []
