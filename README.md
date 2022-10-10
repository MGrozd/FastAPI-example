# Documentation
## Command for running server
    uvicorn main:app --reload
## Command for running Tests
    pytest
## API info
    http://127.0.0.1:8000/docs#/
## Database info
- Database is in memory and it is represented like python dict with names **db** and **flight_db**
- Databes in memory is very efficient for this type of case
- It can be implemented saving on disk for data backup similar like **dbm** database
## Security info
- Basic level of security implemented with token
## Web framework info
- FastAPI is designed for creating and using REST API with standard OpenAPI