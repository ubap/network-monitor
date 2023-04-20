cd database
docker build --tag network-monitor/database:latest .

cd ..
cd speedtest
docker build --tag network-monitor/speedtest:latest .
