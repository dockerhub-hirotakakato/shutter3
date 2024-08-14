FROM alpine:latest

WORKDIR /opt/shutter3

RUN apk add --no-cache curl py3-evdev

COPY main.py .

CMD [ "python", "main.py" ]
