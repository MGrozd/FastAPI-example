from datetime import datetime

from fastapi import FastAPI, Header, HTTPException

from app.models.aircraft import Aircraft, AircraftsId, AircraftsInfo
from app.models.flight import Flight, FlightsId, FlightsInfo

secret_token = "coneofsilence"

db = {
    '1': Aircraft(serial_number='1', manufacturer='Boing'),
    '2': Aircraft(serial_number='2', manufacturer='Airbus')
}

flight_db = {
    '1': Flight(
        flight_number='1',
        departure_airport_code='LDZA',
        arrival_airport_code='LDOS',
        departure_datetime='2023-10-09 08:00',
        arrival_datetime='2023-10-09 09:00',
        assigned_aircraft=Aircraft(serial_number='1', manufacturer='Boing')),
    '2': Flight(
        flight_number='2',
        departure_airport_code='LDOS',
        arrival_airport_code='LDZA',
        departure_datetime='2023-10-09 10:00',
        arrival_datetime='2023-10-09 11:00',
        assigned_aircraft=None)
}

app = FastAPI()
# TODO: add to db


def check_token(token: str):
    if token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")


@app.put("/api/aircraft/create_one")
async def create_one_aircraft(aircraft: Aircraft, x_token: str = Header()):
    check_token(x_token)
    if aircraft.serial_number in db:
        raise HTTPException(status_code=400, detail="Item already exists")


@app.put("/api/aircraft/create")
async def create_aircraft(aircrafts_info: AircraftsInfo, x_token: str = Header()):
    check_token(x_token)
    for aircraft in aircrafts_info.aircrafts:
        if aircraft.serial_number not in db:
            db[aircraft.serial_number] = aircraft


@app.get("/api/aircraft/{serial_number}")
async def read_aircraft_info(serial_number: str, x_token: str = Header()):
    check_token(x_token)
    if serial_number in db:
        return db[serial_number]
    else:
        raise HTTPException(status_code=404, detail=f'Aircraft {serial_number} does not exists!')


@app.post("/api/aircraft/read", response_model=AircraftsInfo)
async def aircrafts_info(aircrafts_id: AircraftsId, x_token: str = Header()):
    check_token(x_token)
    aircrafts_info = AircraftsInfo()
    aircrafts_info_list = []
    for aircraft_serial_number in aircrafts_id.aircrafts_serial_number:
        if aircraft_serial_number in db:
            aircrafts_info_list.append(db[aircraft_serial_number])
    aircrafts_info.aircrafts = aircrafts_info_list
    return aircrafts_info


@app.patch("/api/aircraft/update", response_model=AircraftsInfo)
async def update_aircraft(aircrafts_info: AircraftsInfo, x_token: str = Header()):
    check_token(x_token)
    aircrafts_info_list = []
    for aircraft in aircrafts_info.aircrafts:
        if aircraft.serial_number in db:
            db[aircraft.serial_number] = aircraft
            aircrafts_info_list.append(aircraft)
    aircrafts_info.aircrafts = aircrafts_info_list
    return aircrafts_info


@app.delete('/api/aircraft/delete')
async def delete_aircraft(aircrafts_id: AircraftsId, x_token: str = Header()):
    check_token(x_token)
    for aircraft_serial_number in aircrafts_id.aircrafts_serial_number:
        if aircraft_serial_number in db:
            del db[aircraft_serial_number]
    return db


@app.put('/api/flight/create')
async def create_flight(flights_info: FlightsInfo, x_token: str = Header()):
    check_token(x_token)
    for flight in flights_info.flights:
        flight_departure_datetime = datetime.strptime(flight.departure_datetime, "%Y-%m-%d %H:%M")
        if (flight.flight_number not in flight_db) and (flight_departure_datetime > datetime.now()):
            flight_db[flight.flight_number] = flight


@app.post("/api/flight/read", response_model=FlightsInfo)
async def flights_info(flights_id: FlightsId, x_token: str = Header()):
    check_token(x_token)
    flights_info = FlightsInfo()
    flights_info_list = []
    for flight_number in flights_id.flights_number:
        if flight_number in flight_db:
            flights_info_list.append(flight_db[flight_number])
    flights_info.flights = flights_info_list
    return flights_info

@app.patch('/api/flight/update', response_model=FlightsInfo)
async def update_flight(flights_info: FlightsInfo, x_token: str = Header()):
    check_token(x_token)
    flights_info_list = []
    for flight in flights_info.flights:
        if flight.flight_number in flight_db:
            flight_db[flight.flight_number] = flight
            flights_info_list.append(flight)
    flights_info.flights = flights_info_list
    return flights_info

@app.delete('/api/flight/delete')
async def delete_flight(flights_id: FlightsId, x_token: str = Header()):
    check_token(x_token)
    for flight_number in flights_id.flights_number:
        if flight_number in flight_db:
            del flight_db[flight_number]
    return flight_db

