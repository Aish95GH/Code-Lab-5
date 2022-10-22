FROM python
RUN pip install flask

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

ENV API_HOST=${API_HOST}
ENV API_PORT=${API_PORT}
ENV CONSUMER_PORT=${CONSUMER_PORT}
VOLUME [ "/app" ]
WORKDIR /app
EXPOSE ${CONSUMER_PORT}
