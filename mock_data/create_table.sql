CREATE TABLE airports (
  airport_code VARCHAR(3) PRIMARY KEY,
  airport_name TEXT NOT NULL
);

CREATE TABLE facilities (
  facility_id SERIAL PRIMARY KEY,
  airport_code VARCHAR(3) NOT NULL REFERENCES airports(airport_code),
  facility_name TEXT NOT NULL,
  facility_type VARCHAR(20) NOT NULL CHECK (facility_type IN ('restaurant', 'gate', 'toilet', 'lounge', 'other'))
);

CREATE TABLE opening_hours (
  facility_id INTEGER NOT NULL REFERENCES facilities(facility_id),
  day_of_week VARCHAR(10) NOT NULL CHECK (day_of_week IN ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')),
  open_time TIME,
  close_time TIME,
  PRIMARY KEY (facility_id, day_of_week)
);

CREATE TABLE holidays (
  holiday_date DATE NOT NULL,
  facility_id INTEGER NOT NULL REFERENCES facilities(facility_id),
  open_time TIME,
  close_time TIME,
  PRIMARY KEY (holiday_date, facility_id)
);

CREATE TABLE gates (
  gate_id SERIAL PRIMARY KEY,
  airport_code VARCHAR(3) NOT NULL REFERENCES airports(airport_code),
  gate_number VARCHAR(10) NOT NULL,
  facility_id INTEGER NOT NULL REFERENCES facilities(facility_id) UNIQUE
);
