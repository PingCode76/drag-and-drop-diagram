FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL "/static"
ENV STATIC_PATH "/var/www/app/static"
#COPY ./requirements.txt /var/www/requirements.txt
#RUN pip install -r /var/www/requirements.txt

# launch this on docker console
# sudo bash start.sh --------------- for create a instance
# sudo docker ps for --------------- list a instances
# visit instance with http://ip-address:56733