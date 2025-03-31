FROM python:3.13-slim

WORKDIR /app

COPY ecowitt_relay.py .
COPY run.sh /run.sh

# Install dependencies
RUN apt-get update && apt-get install -y jq && \
    pip install flask requests && \
    chmod +x /run.sh

CMD [ "/run.sh" ]
