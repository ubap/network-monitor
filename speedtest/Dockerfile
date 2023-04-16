# syntax=docker/dockerfile:1

FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install curl -y
RUN curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash
RUN apt-get install speedtest -y
# run speedtest once to accept license and gdpr
RUN speedtest --accept-license --accept-gdpr --progress=no --unit=Mbps --format=json-pretty 

RUN apt-get install python3 python3-pip -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY . .

CMD ["python3", "main.py"]
