FROM python:3.11-slim

WORKDIR /app

COPY ecowitt_relay.py .
COPY run.sh /run.sh

RUN pip install flask requests && chmod a+x /run.sh

CMD [ "/run.sh" ]