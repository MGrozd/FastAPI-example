from fastapi import FastAPI, Header, HTTPException

from app.models.aircraft import Aircraft, AircraftsId, AircraftsInfo

secret_token = "coneofsilence"

db = {
    '1': Aircraft(serial_number='1', manufacturer='Boing'),
    '2': Aircraft(serial_number='2', manufacturer='Airbus')
}

AIRCRAFTS = 'aircraft'
AIRCRAFTS_SERIAL_NUMBER = 'aircrafts_serial_number'

app = FastAPI()


def check_token(token: str):
    if token != secret_token:
        raise HTTPException(status_code=400, detail="Invalid X-Token header")


@app.put("/api/aircraft/create_one")
async def create_one_aircraft(aircraft: Aircraft, x_token: str = Header()):
    check_token(x_token)
    if aircraft.serial_number in db:
        raise HTTPException(status_code=400, detail="Item already exists")
    # TODO: add to db


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
    with open('update.txt', 'a') as f:
        f.write(str(db))
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
