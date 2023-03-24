FROM python:3.11

WORKDIR /flask-app

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
