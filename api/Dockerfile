FROM python:3.7-alpine

WORKDIR /code

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install psycopg2-binary


RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

RUN chmod +x manage.py
RUN python manage.py db init; exit 0
RUN python manage.py db migrate ; exit 0
#RUN python manage.py db upgrade ; exit 0

CMD ["flask", "run"]

