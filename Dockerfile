FROM python:3.10

WORKDIR /usr/src/app
COPY . .

COPY requirements.txt /usr/src/app/
RUN pip install -r requirements.txt