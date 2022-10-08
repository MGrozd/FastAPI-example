from fastapi import FastAPI

from app.models.aircraft import Aircraft
from app.models.flight import Flight
app = FastAPI()





@app.post("/aircraft/create")
async def create_aircraft(aircraft: Aircraft):
    return aircraft

@app.get("/")
def read_root():
    return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}