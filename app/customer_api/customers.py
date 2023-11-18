import os
import requests
import traceback

from loguru import logger
from dotenv import load_dotenv


class Customer():

    base_url = "https://developers.cathaypacific.com/hackathon-apigw/airport/customers/"
    path_param = "/details"

    parent_dir = os.path.dirname(os.path.dirname(__file__))
    load_dotenv(os.path.join(parent_dir, '.env'))

    api_key = os.getenv("CATHAY_API_KEY")

    headers = {
      'apiKey': api_key
    }

    def __init__(self, pid: str):
        self.pid = pid
        logger.debug(f"Passenger ID: {pid}")


    def get_flights(self):
        url = self.base_url + self.pid + self.path_param
        res = {
            "data": {},
            "success": False,
            "message": ""
        }
        flights = {}
        try:
            response = requests.request("GET", url, headers=self.headers)
            data = response.json()
            logger.debug(f"response: {data}")
            dated_flight = data["dictionaries"]["datedFlight"]
            logger.debug(f"datedFlight: {dated_flight}")
            flights = self.prepare_flights(dated_flight)
            logger.info(f"flights: {flights}")

            # prepare response
            res["data"]["pid"] = self.pid
            res["data"]["flights"] = flights
            res["success"] = True
        except Exception as e:
            res["message"] = "Invalid request"
            self.logger.error('ERROR: get_flights()')
            self.logger.error(e)
            self.logger.error(traceback.format_exc())
        finally:
            return res


    def prepare_flights(self, response: dict):
        flights = {}
        for id, item in response.items():
            flights[id] = {}
            flights[id]["from"] = {}
            flights[id]["to"] = {}
            flights[id]["from"]["at"] = {}
            flights[id]["to"]["at"] = {}
            flights[id]["from"]["airport"] = item["legs"][0]["boardPointIataCode"]
            flights[id]["to"]["airport"] = item["legs"][0]["offPointIataCode"]

            for timing in item["flightPoints"][0]["departure"]["timings"]:
                if timing["qualifier"] == "STD":
                    datetime = timing["value"]
                    date, time = datetime.split("T")
                    flights[id]["from"]["at"]["date"] = date
                    flights[id]["from"]["at"]["time"] = time

            for timing in item["flightPoints"][0]["arrival"]["timings"]:
                if timing["qualifier"] == "STA":
                    datetime = timing["value"]
                    date, time = datetime.split("T")
                    flights[id]["to"]["at"]["date"] = date
                    flights[id]["to"]["at"]["time"] = time

        logger.debug(f"flights: {flights}")

        return flights

# cus = Customer("510892B0000153AC")
# print(cus.get_flights())




        


