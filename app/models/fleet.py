from pydantic import BaseModel

from .aircraft import Aircraft
from .flight import Flight


class Fleet(BaseModel):
    aircrafts: list[Aircraft] = []
    flights: list[Flight] = []
