FROM python:3.7-alpine

WORKDIR /code

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

#RUN pip install psycopg2

#RUN apt install libpq-dev python3-dev

#RUN pip install psycopg2-binary

#pipenv run pip install psycopg2

#RUN pipenv run pip install psycopg2-binary



RUN pip install -r requirements.txt

EXPOSE 5000

COPY . .

CMD ["flask", "run"]