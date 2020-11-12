FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
EXPOSE 80
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt

# How de display this application on docker instance ?

# ./start.sh --------------- for create a instance
# sudo docker ps -a -s for --------------- list a instances
# docker run -p 80:50 -d docker-flask.dev -------------- if instance is not running
# visit instance with http://192.168.99.106:80/    #docker-machine config for have ip  ( or http://localhost:80 )

# -------------------------------------------------------------------------------

# HELP FOR DOCKER
# docker run -p 5001:5000 -d container-name  ---------- for specify port ( http://localhost:80 )  
# docker container ls -------- ( or docker image ls ) see containers or images
# docker system prune -------------for clean all instances and images
# docker rmi $(docker images -a -q)
# docker stop $(docker ps -a -q)
# docker rm $(docker ps -a -q)
# docker volume prune

#trying without port

# for machine
# create test machine : docker-machine create --driver virtualbox docker
# port forwarding in virtualBox