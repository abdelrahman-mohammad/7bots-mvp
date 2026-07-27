from db import connect
from fastapi import FastAPI, HTTPException

app = FastAPI(title="ShipTrack Booking Service")


@app.post("/consignments")
def create_consignment(customer_id):
    connection = connect()
    cursor = connection.cursor()

    cursor.execute("SELECT credit_hold FROM customer WHERE customer_id = %s", (customer_id,))
    if cursor.fetchone()[0]:
        raise HTTPException(status_code=409, detail="customer is on credit hold")

    cursor.execute(
        "INSERT INTO consignment (customer_id) VALUES (%s) RETURNING consignment_id",
        (customer_id,),
    )
    connection.commit()
    return {"consignment_id": cursor.fetchone()[0], "status": "booked"}
