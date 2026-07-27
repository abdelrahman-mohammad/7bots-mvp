# ShipTrack integrations

The customer portal calls the ShipTrack Booking API to create consignments.

The finance system drops a credit hold CSV on a shared mount every morning. A cron job on shiptrack-app-01 loads it into the customer table.

The tracking service writes scan events to the consignment database, and a nightly job copies them to the scan archive bucket.

When a consignment is delivered the Booking API posts an invoice event to the Legacy Invoicing Gateway (INVGW). Nobody has documentation for INVGW and it appears nowhere else in the evidence.
