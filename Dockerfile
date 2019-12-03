FROM python:3.8

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY janisbot4 janisbot4/
COPY conf conf/
COPY main.py main.py

RUN ln -s /run/secrets/janisbot.conf /app/conf/janisbot.conf
