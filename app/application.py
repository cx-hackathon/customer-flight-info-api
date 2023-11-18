from fastapi import FastAPI
from pydantic import BaseModel
from customer_api.customers import Customer

app = FastAPI()

class Facility(BaseModel):
    name: str
    type: str

facilities = {
    "lhr": [
        Facility(name="Lounge A", type="lounge"),
        Facility(name="Runway 1", type="runway"), 
        Facility(name="Hangar 1", type="hangar")
    ],
    "jfk": [
        Facility(name="Lounge B", type="lounge"),
        Facility(name="Runway 2", type="runway"),
        Facility(name="Hangar 2", type="hangar")
    ]
}

@app.get("/")
async def health_check():
    return {"message": "Customer Info API is running"}


@app.get("/v1/customer/{pid}")
async def customer_flights(pid: str):
    customer = Customer(pid)
    return customer.get_flights()



@app.get("/v1/facilities/{airport}")
def get_facilities(airport: str, type: str):
    return [f for f in facilities[airport] if f.type == type]
