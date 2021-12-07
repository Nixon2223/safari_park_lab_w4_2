DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS staff;

CREATE TABLE staff (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255),
  start_date DATE,
  department VARCHAR(255),
  performance INT
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255),
    staff_id INT REFERENCES staff(id)
);