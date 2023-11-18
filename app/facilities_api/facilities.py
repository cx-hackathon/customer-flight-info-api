from sqlmodel import Field, SQLModel, create_engine, Session, select
from loguru import logger

from .db_model import *


class AirportFacilities():

    def __init__(self, airport: str):
        self.airport = airport
        logger.debug(f"Airport code: {airport}")


    def get_ids_by_type(self, type: str):
        logger.debug(type)
        with Session(engine) as session:
            query = select(Facilities).where(Facilities.airport_code == self.airport).where(Facilities.facility_type == type)
            logger.debug(f"query {query}")
            facs = session.exec(query).all()
            logger.debug(f"fac id: {facs}")

        ids = []
        for fac in facs:
            ids.append(fac.facility_id)

        return ids


    def get_name_by_id(self, id: int):
        with Session(engine) as session:
            query = select(Facilities).where(Facilities.facility_id == id)
            facs = session.exec(query).all()

        return facs[0].facility_name


    def get_opening_hours(self, id: int):
        res = {
            "Monday": {},
            "Tuesday": {},
            "Wednesday": {},
            "Thursday": {},
            "Friday": {},
            "Saturday": {},
            "Sunday": {},
            "Holidays": []
        }
        with Session(engine) as session:
            weekdays_query = select(Opening_hours).where(Opening_hours.facility_id == id)
            holidays_query = select(Holidays).where(Holidays.facility_id == id)
            weekdays = session.exec(weekdays_query).all()
            holidays = session.exec(holidays_query).all()

        for day in weekdays:
            res[day.day_of_week]["from"] = day.open_time
            res[day.day_of_week]["to"] = day.close_time

        for day in holidays:
            holiday_hour = {
                "date": "",
                "from": "",
                "to": ""
            }
            holiday_hour["date"] = day.holiday_date
            holiday_hour["from"] = day.open_time
            holiday_hour["to"] = day.close_time
            res["Holidays"].append(holiday_hour)

        return res


    def get_gate_info(self, id: int):
        with Session(engine) as session:
            query = select(Gates).where(Gates.facility_id == id)
            gates = session.exec(query).all()
            gate = gates[0]
        logger.debug(gates)

        res = {}
        res['facility_id'] = id
        res['gate_id'] = gate.gate_id
        res['gate_number'] = gate.gate_number

        return res
        

