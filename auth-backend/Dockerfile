FROM python:3.8.1-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./auth-backend/requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY ./auth-backend /app

EXPOSE 5000

ENV FLASK_APP=autoapp.py

CMD ["gunicorn", "-b", ":5000", "autoapp:app"]