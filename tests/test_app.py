from datetime import datetime
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_create_one_aircraft():
    response = client.put(
        "/api/aircraft/create_one",
        headers={"X-Token": "coneofsilence"},
        json={"serial_number": "0", "manufacturer": "Boing"},
    )
    assert response.status_code == 200


def test_create_aircraft():
    response = client.put(
        "/api/aircraft/create",
        headers={"X-Token": "coneofsilence"},
        json={"aircrafts": [{"serial_number": "3", "manufacturer": "Boing"},
                            {"serial_number": "4", "manufacturer": "Airbus"}]}
    )
    assert response.status_code == 200


def test_read_aircraft():
    response = client.get("/api/aircraft/1", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "serial_number": "1",
        "manufacturer": "Boing",
    }

def test_read_aircrafts_info():
    response = client.post(
        "/api/aircraft/read",
        headers={"X-Token": "coneofsilence"},
        json={"aircrafts_serial_number": ["1", "2"]}
    )
    assert response.status_code == 200
    assert response.json() == {"aircrafts": [
        {"serial_number": "1", "manufacturer": "Boing"},
        {"serial_number": "2", "manufacturer": "Airbus"}]
    }

def test_update_aircraft():
    response = client.patch(
        "/api/aircraft/update",
        headers={"X-Token": "coneofsilence"},
        json={'aircrafts': [{"serial_number": "1", "manufacturer": "Lockheed Martin"}]}
    )
    assert response.status_code == 200
    assert response.json() == {
        'aircrafts': [{'manufacturer': 'Lockheed Martin', 'serial_number': '1'}]
    }

def test_delete_aircraft():
    response = client.delete(
        "/api/aircraft/delete",
        headers={"X-Token": "coneofsilence"},
        json={"aircrafts_serial_number": ["1", "2"]}
    )
    assert response.status_code == 200
    assert response.json() == {
        '3': {'manufacturer': 'Boing', 'serial_number': '3'},
        '4': {'manufacturer': 'Airbus', 'serial_number': '4'}
    }


def test_create_flight():
    response = client.put(
        '/api/flight/create',
        headers={"X-Token": "coneofsilence"},
        json={
            "flights": [
                {
                    "flight_number": "1",
                    "departure_airport_code": "LDZA",
                    "arrival_airport_code": "LDOS",
                    "departure_datetime": datetime(2023, 10, 9, 8, 0, 0, 0).strftime("%Y-%m-%d %H:%M"),
                    "arrival_datetime": datetime(2023, 10, 9, 9, 0, 0, 0).strftime("%Y-%m-%d %H:%M"),
                    "assigned_aircraft": {"serial_number": "1", "manufacturer": "Boing"}
                },
                {
                    "flight_number": "2",
                    "departure_airport_code": "LDOS",
                    "arrival_airport_code": "LDZA",
                    "departure_datetime": datetime(2023, 10, 9, 10, 0, 0).strftime("%Y-%m-%d %H:%M"),
                    "arrival_datetime": datetime(2023, 10, 9, 11, 0, 0).strftime("%Y-%m-%d %H:%M"),
                }
            ]
        }
    )
    assert response.status_code == 200

def test_read_flights_info():
    response = client.post(
        "/api/flight/read",
        headers={"X-Token": "coneofsilence"},
        json={"flights_number": ["1", "2"]}
    )
    assert response.status_code == 200
    assert response.json() == {
        'flights': [
            {
                'arrival_airport_code': 'LDOS',
                'arrival_datetime': '2023-10-09 09:00',
                'assigned_aircraft': {'manufacturer': 'Boing', 'serial_number': '1'},
                'departure_airport_code': 'LDZA',
                'departure_datetime': '2023-10-09 08:00',
                'flight_number': '1'
            },
            {
                'arrival_airport_code': 'LDZA',
                'arrival_datetime': '2023-10-09 11:00',
                'assigned_aircraft': None,
                'departure_airport_code': 'LDOS',
                'departure_datetime': '2023-10-09 10:00',
                'flight_number': '2'
            }
        ]
    }

def test_update_flight():
    response = client.patch(
        '/api/flight/update',
        headers={"X-Token": "coneofsilence"},
        json={
            'flights': [
                {
                    'arrival_airport_code': 'LDZA',
                    'arrival_datetime': '2023-10-09 11:00',
                    'assigned_aircraft': {'manufacturer': 'Boing', 'serial_number': '1'},
                    'departure_airport_code': 'LDOS',
                    'departure_datetime': '2023-10-09 10:00',
                    'flight_number': '2'
                }
            ]
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        'flights': [
            {
                'arrival_airport_code': 'LDZA',
                'arrival_datetime': '2023-10-09 11:00',
                'assigned_aircraft': {'manufacturer': 'Boing', 'serial_number': '1'},
                'departure_airport_code': 'LDOS',
                'departure_datetime': '2023-10-09 10:00',
                'flight_number': '2'
            }
        ]
    }

def test_delete_flight():
    response = client.delete(
        "/api/flight/delete",
        headers={"X-Token": "coneofsilence"},
        json={"flights_number": ["1"]}
    )
    assert response.status_code == 200
    assert response.json() == {
        '2': {
            'arrival_airport_code': 'LDZA',
            'arrival_datetime': '2023-10-09 11:00',
            'assigned_aircraft': {'manufacturer': 'Boing', 'serial_number': '1'},
            'departure_airport_code': 'LDOS',
            'departure_datetime': '2023-10-09 10:00',
            'flight_number': '2'
        }
    }
