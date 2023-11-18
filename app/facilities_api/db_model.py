import os

from sqlmodel import Field, SQLModel, create_engine
from datetime import date, time
from dotenv import load_dotenv


parent_dir = os.path.dirname(os.path.dirname(__file__))
load_dotenv(os.path.join(parent_dir, '.env'))

db_url = os.getenv("DB_URL")
db_password = os.getenv("DB_PASSWORD")
user = "postgres"
db_name = "airport_facilities"

postgres_url = f"postgresql://{user}:{db_password}@{db_url}:5432/{db_name}"

engine = create_engine(postgres_url)

SQLModel.metadata.create_all(engine)


class Airports(SQLModel, table=True):
    airport_code: str = Field(default=None, primary_key=True)
    airport_name: str


class Facilities(SQLModel, table=True):
    facility_id: int = Field(default=None, primary_key=True)
    airport_code: str 
    facility_name: str
    facility_type: str


class Opening_hours(SQLModel, table=True):
    facility_id: int = Field(default=None, primary_key=True)
    day_of_week: str = Field(default=None, primary_key=True)
    open_time: str
    close_time: str


class Holidays(SQLModel, table=True):
    holiday_date: date = Field(default=None, primary_key=True) 
    facility_id: int = Field(default=None, primary_key=True)
    open_time: time
    close_time: time


class Gates(SQLModel, table=True):
    gate_id: int = Field(default=None, primary_key=True)
    airport_code: str
    gate_number: str
    facility_id: int



