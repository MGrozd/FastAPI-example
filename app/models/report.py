from pydantic import BaseModel


class AircraftReport(BaseModel):
    aircraft_id: str = ''
    average_flight_time_in_minutes: int = 0


class AirportReport(BaseModel):
    departure_airport_code: str = ''
    number_of_flights: int = 0
    aircrafts: list[AircraftReport] = []


class FlightsReport(BaseModel):
    departure_airport_list: list[AirportReport] = []

