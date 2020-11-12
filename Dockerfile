FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt

# How de display this application on docker instance ?

# ./start.sh --------------- for create a instance
# sudo docker ps -a -s for --------------- list a instances
# docker run d79411759b5c -------------- if instance is not running
# visit instance with http://ip-address:56733

# -------------------------------------------------------------------------------

# HELP FOR DOCKER
# docker run -p 5001:5000 -d container-name  ---------- for specify port ( http://localhost:5001 )  
# docker container ls -------- ( or docker image ls ) see containers or images
# docker system prune -------------for clean all instances and images