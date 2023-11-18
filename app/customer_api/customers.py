import os
import requests
import traceback

from loguru import logger
from dotenv import load_dotenv

parent_dir = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(parent_dir, '.env'))

api_key = os.getenv("CATHAY_API_KEY")


url = "https://developers.cathaypacific.com/hackathon-apigw/airport/customers/510892B000014EBB/details"

payload = {}
headers = {
  'apiKey': 'V6lY3PSPozs1RAokZYrjWeGdTxMTg91o',
  'Cookie': '_abck=6A635EB9F44F1A25ADBAD3DE76BBEC0C~-1~YAAQRSTDFzxqf9yLAQAAy3PD4QpTiY6GW/nQ24Y60p6IbnOeI5b2glrVgrZLfAQbVtCwMKqwuEpEj/EK7m87KoagQHMLx1658geHLELw/ck+TmqaeFPb6jHePggkD+VsM7RnlyEJ9FLoRX3ns5aW9QGHPA90IkFj12O/b6As3hsmb4OnRcdJmUiVXcDhYYscgVibzoPMhPhVOrntrqVZl4v6MqCT9MDQfM5XCEDJz0La/rAk4aYq3gX1ohC/GjiSaTEpM65gN9Vxu5YGzpPetJGz8pV6KFa8DtsFEI1uXZi79eycEjnVsZT9qHuwrun5L4mcX/kvHn1kb7wUVR3mhhGF/GS86yFeCsfwcde/7jf7ovl7dhEiQphl2zusT+RU~-1~-1~-1; bm_sz=FE694917132A9A42386400E98EA35D24~YAAQRSTDFz1qf9yLAQAAy3PD4RXvLyouwuNVqUKJvCIrXTcoTwMC1gSzFs0+aK9S2BYe75uB2ZH0SQRfDLNxkVzR2iLJ6AJlF/Ie/3hsBOiW3KC5gwcv2vZeblz4i/EiEw2S5GsPEqnj7rPwjYZJX5R7NizlikIxI829aRVkk8UReJswAhj1wE+FU3HTsWkrbiy5q5uRmHT4UKg6l3V2HM00tHke7mf5QQzc1J7WHdppAwEh3Wnuhzf8E2IdWVa62rEC8JwteUGlCoHEQcQdNjn2cGbJv/Drc1EFmksCriK3uLabQqf6idOd~3617862~3425845; 8bac6ca36dd7fb6e1a5df804509d965c=35d212e43c5133effb9e250a30b93d43; 91d1e5aa2d49f01a98ca619ad658207a=818868ad03ecc9ede57945664b7d842a'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.json())

print(api_key)


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
        url = base_url + self.pid + path_param
        res = {
            "data": {},
            "success": False,
            "message": ""
        }
        try:
            response = requests.request("GET", url, headers=headers)
            data = response.json()
        except Exception as e:
            res["message"] = "Invalid request"
            self.logger.error('ERROR: get_flights()')
            self.logger.error(e)
            self.logger.error(self.traceback.format_exc())
        finally:
            return res

        


