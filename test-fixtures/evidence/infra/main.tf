resource "aws_instance" "shipdb_primary" {
  instance_type = "m5.large"

  tags = {
    Name = "shipdb-primary"
    Role = "PostgreSQL 12 primary for ShipTrack"
  }
}

resource "aws_instance" "shiptrack_app_01" {
  instance_type = "t3.medium"

  tags = {
    Name = "shiptrack-app-01"
    Role = "nginx fronting booking-service and tracking-service"
  }
}

resource "aws_s3_bucket" "scan_archive" {
  bucket = "vantage-shiptrack-scan-archive"
}
