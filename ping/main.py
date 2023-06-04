from ping3 import ping
from influxdb import InfluxDBClient
import datetime
import time
import schedule

client = InfluxDBClient(host="db", port="8086", username="admin", database="defaultdb")

hosts = [
    "8.8.8.8",
    "wp.pl",
    "192.168.1.1",
    "192.168.88.1"
]


def job(host):
    timestamp = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc).isoformat()
    ping_ms = ping(host, unit="ms", timeout=4)
    signal = "ping_ms"
    if ping_ms is None:
        signal = "timeout"
        ping_ms = 1
    if ping_ms is False:
        signal = "cannot_resolve"
        ping_ms = 1

    if ping_ms > 4000:
        ping_ms = 4000

    json_body = [
        {
            "measurement": signal,
            "tags": {
                "host": host,
            },
            "time": timestamp,
            "fields": {
                "value": ping_ms
            }
        }
    ]
    client.write_points(json_body)


for host in hosts:
    schedule.every(1).second.do(job, host=host)

while True:
    schedule.run_pending()
    time.sleep(0.1)