FROM python:3.8

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src src/
COPY conf conf/

RUN ln -s /run/secrets/janisbot.conf /app/conf/janisbot.conf
