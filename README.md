# Logstash HTTP Poller Pipeline for WebServer Indexer
This repository provides details on configuring a Logstash pipeline using the http_poller input plugin. The pipeline fetches data from an external SOAP API and processes it for further use. The timestamp range for data collection is dynamically adjusted to ensure that the pipeline runs at different times, maintaining continuous log coverage.

## Purpose
This Logstash pipeline is designed to periodically collect access records from a WebServer. It sends a SOAP request to the API and retrieves access logs within a specific time range.

## Requirements
- Elasticsearch Cluster
- Logstash

## Configuration
The pipeline in [pipeline.conf](https://github.com/AndreaBarocco/WebServer-Indexer/blob/main/pipeline.conf) use the http_poller plugin to send an HTTP POST request to the WEBSERVER. The request includes authentication credentials and date filters to retrieve access records.

To update the pDATEFROM and end pDATETO field for the query dynamically, I created the [update_logstash_conf.py](https://github.com/AndreaBarocco/WebServer-Indexer/blob/main/update_logstash_conf.py) python script.

Lastly I configured the execution of the script every n minutes via crontab and the logstash service restart
-  */5 * * * * python3 /esr/server/sman/script/update_logstash_conf.py && sleep 10 && systemctl restart logstash
