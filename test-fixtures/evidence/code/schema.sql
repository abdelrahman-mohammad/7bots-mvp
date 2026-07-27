-- ShipTrack consignment database (SHIPDB)

CREATE TABLE customer (
    customer_id  SERIAL PRIMARY KEY,
    name         TEXT NOT NULL,
    credit_hold  BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE consignment (
    consignment_id  SERIAL PRIMARY KEY,
    customer_id     INTEGER NOT NULL REFERENCES customer (customer_id),
    status          TEXT NOT NULL DEFAULT 'booked'
);

CREATE TABLE scan_event (
    scan_event_id   SERIAL PRIMARY KEY,
    consignment_id  INTEGER NOT NULL REFERENCES consignment (consignment_id),
    depot_code      TEXT NOT NULL,
    scanned_at      TIMESTAMP NOT NULL
);
