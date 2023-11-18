from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from customer_api.customers import Customer

app = FastAPI()

# allow CORS setting
origins = [
    '*',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# security setting
# https://geekflare.com/http-header-implementation/https://geekflare.com/http-header-implementation/
HEADERS = {
    # CORS setting
    "Access-Control-Allow-Credentials": "true",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "*",
    "Access-Control-Allow-Headers": "*",
    # security setting
    "X-Frame-Options": "SAMEORIGIN",
    "X-Content-Type-Options": "nosniff",
    "X-XSS-Protection": "1; mode=block",
    "Strict-Transport-Security": "max-age=31536000; includeSubDomains",
    # enforcement of Certificate Transparency for 24 hours
    "Expect-CT": "max-age=86400, enforce",
    "Content-Security-Policy": "default-src https:"
}


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
