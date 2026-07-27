from db import connect
from fastapi import FastAPI

app = FastAPI(title="ShipTrack Tracking Service")


@app.get("/consignments/{consignment_id}/tracking")
def read_tracking(consignment_id):
    connection = connect()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT depot_code, scanned_at FROM scan_event WHERE consignment_id = %s",
        (consignment_id,),
    )
    return cursor.fetchall()
