FROM ubuntu:20.04
WORKDIR /app
RUN apt update
ENV DEBIAN_FRONTEND="noninteractive" TZ="Europe/Zagreb"
RUN apt -y install neo4j-client postgresql python3 python3-pip libpq-dev
COPY . .
RUN  pip3 install -r requirements.txt

EXPOSE 8000
CMD ["sh", "start_development_server.sh"]