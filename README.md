# Drag and drop system for diagram

Generate a data with a diagram, created with drag and drop

## Use the app 

## Technologies
    - Flask
    - Vue.js
    - Drag and Drop Component : Easy-Dnd ( https://github.com/rlemaigre/Easy-DnD ) 

## Generality

Launch a python server ( in api folder) :

```bash
$ flask run 
```

Launch a Vue server with yarn or npm in webapp folder:

```bash
npm install
npm run serve
```

install the necessary library

    - pip install flask
    - pip install xlrd
    - pip install turtle

    For Database ( PostreSQL ) 

    - pip install psycopg2 Flask-SQLAlchemy Flask-Migrate
    - pip install flask_script 

## DataBase

    - Install PostGresSQL et create database 
    - change database configuration ( config.py ) 
    - python manage.py db init
    - python manage.py db migrate
    - python manage.py db upgrade

## Docker
Docker-compose up --build

## Algorithm

## Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


