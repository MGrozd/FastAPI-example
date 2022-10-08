from fastapi import FastAPI, Header, HTTPException

from app.models.fleet import Fleet
from app.models.aircraft import Aircraft

secret_token = "coneofsilence"

db = {
    "1": {"serial_number": "1", "manufacturer": "Boing"}
}
AIRCRAFTS = 'aircraft'

app = FastAPI()

"""
@app.put("/api/aircraft/create")
async def create_aircraft(fleet: Fleet, x_token: str = Header()):
    if x_token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    for aircraft in fleet[AIRCRAFTS]:
        if aircraft.serial_number in db:
            raise HTTPException(status_code=400, detail="Item already exists")
    with open('test.txt', 'a') as file:
        file.write(aircraft.serial_number + aircraft.manufacturer)
"""

@app.put("/api/aircraft/create")
async def create_aircraft(aircraft: Aircraft, x_token: str = Header()):
    if x_token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if aircraft.serial_number in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    # TODO: add to db


@app.get("/api/aircraft/{serial_number}")
async def read_aircraft_info(serial_number: str, x_token: str = Header()):
    if x_token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if serial_number in db:
        return db[serial_number]
    else:
        raise HTTPException(status_code=404, detail=f'Aircraft {serial_number} does not exists!')


@app.patch("/api/aircraft/update", response_model=Aircraft)
async def update_aircraft(aircraft: Aircraft, x_token: str = Header()):
    if x_token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if aircraft.serial_number not in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    db[aircraft.serial_number] = aircraft
    return aircraft

@app.delete("/api/aircraft/delete")
async def update_aircraft(aircraft: Aircraft, x_token: str = Header()):
    if x_token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")
    if aircraft.serial_number not in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    del db[aircraft.serial_number]
    return db

