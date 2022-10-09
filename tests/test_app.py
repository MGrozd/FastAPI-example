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

