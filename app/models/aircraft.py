from pydantic import BaseModel


class Aircraft(BaseModel):
    serial_number: str
    manufacturer: str


