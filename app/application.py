from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from customer_api.customers import Customer
from facilities_api.facilities import AirportFacilities



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


@app.get("/")
async def health_check():
    return {"message": "Customer Info API is running"}


@app.get("/v1/customer/{pid}")
async def customer_flights(pid: str):
    customer = Customer(pid)
    return customer.get_flights()



@app.get("/v1/facilities/{airport}")
def get_facilities(airport: str, type: str):
    res = {
        "data": [],
        "success": False,
        "message": ""
    }

    info = AirportFacilities(airport)
    facility_ids = info.get_ids_by_type(type)
    logger.debug(f"facility_id: {facility_ids}")
    
    if type == "gate":
        for id in facility_ids:
            gate_info = info.get_gate_info(id)
            res["data"].append(gate_info)
        res["success"] = True
        return res

    for id in facility_ids:
        data = {
            "facility_id": id,
            "name": "",
            "opening_hour": ""
        }
        data["name"] = info.get_name_by_id(id)
        data["opening_hour"] = info.get_opening_hours(id)
        res["data"].append(data)
    
    res["success"] = True

    return res
        

        



