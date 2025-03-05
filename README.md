# Logstash HTTP Poller Pipeline for WebServer Indexer
This repository provides details on configuring a Logstash pipeline using the http_poller input plugin. The pipeline fetches data from an external SOAP API and processes it for further use. The timestamp range for data collection is dynamically adjusted to ensure that the pipeline runs at different times, maintaining continuous log coverage.

## Purpose
This Logstash pipeline is designed to periodically collect access records from a WebServer. It sends a SOAP request to the API and retrieves access logs within a specific time range.

## Requirements
- Elasticsearch Cluster
- Logstash
