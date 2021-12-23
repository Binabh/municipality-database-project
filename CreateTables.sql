CREATE TABLE Wards(
    ward_id INTEGER UNIQUE PRIMARY KEY,
    ward_name VARCHAR(70),
    location_lat FLOAT(6),
    location_lon FLOAT(6)
);

CREATE TABLE Households(
    house_id INTEGER UNIQUE,
    ward_id INTEGER,
    owner_name VARCHAR(70),
    house_code VARCHAR(70),
    location_lat FLOAT(6),
    location_lon FLOAT(6),
    PRIMARY KEY (house_id),
    FOREIGN KEY (ward_id) REFERENCES Wards(ward_id)
);