FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
# or FROM python:3.6.1-alpine

RUN apk --update add bash nano

RUN pip install flask
RUN pip install pipreqs

COPY ./requirements.txt /app/requirements.txt
#COPY requirements.txt requirements.txt

#RUN sh start.sh
WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
#COPY . .    

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

EXPOSE 5000

CMD ["python","app.py"]
#ENTRYPOINT ["app.py"]

#HOW to generate requirements.txt ?
# pip install pipreqs
# pipreqs /chemin/vers/votre/projet or just "pipreqs" in current folder
# install with pip install -r requirements.txt

# try to : https://medium.com/@tasnuva2606/dockerize-flask-app-4998a378a6aa
