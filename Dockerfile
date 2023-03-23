LABEL maintainer="Matheus Feu Soares de Assis - matheusfeu@gmail.com"
LABEL desc="Dockerfile for Python Flask API"

FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt /app

RUN pip install mysqlclient==2.1.1
RUN python -m pip install --uprade pip
RUN pip install -r requirements.txt

COPY . /app

CMD ["python", "app.py"]
