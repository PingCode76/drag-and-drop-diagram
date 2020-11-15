FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano

RUN pip install flask
COPY ./app /app
WORKDIR /app

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
EXPOSE 80
#ENTRYPOINT ["run.py"]
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt



# How de display this application on docker instance ?

# ./start.sh --------------- for create a instance ( or sh ./start.sh)
# sudo docker ps -a -s for --------------- list a instances
# docker run -p 80:80 -d docker-flask.dev -------------- if instance is not running
# visit instance with http://127.0.0.1:80/    # or docker-machine ip

# -------------------------------------------------------------------------------

# HELP FOR DOCKER
# docker system prune
# docker rmi $(docker images -a -q)
# docker stop $(docker ps -a -q)
# docker rm $(docker ps -a -q)
# docker volume prune
