FROM --platform=${TARGETPLATFORM:-linux/amd64} python:3.11-alpine as build

ARG TARGETPLATFORM
ARG BUILDPLATFORM

WORKDIR /home/app/

COPY app.py .
COPY listen.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py

EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]