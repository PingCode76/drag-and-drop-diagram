# Drag and drop system for diagram

Generate a data with a diagram, created with drag and drop

## Use the app 

## Technologies
    - Flask
    - Vue.js
    - Drag and Drop Component : https://github.com/SortableJS/Vue.Draggable 

## Generality

Launch a python server:

    flask run (in api folder) 

Launch a Vue server with yarn or npm in webapp folder:

    npm install
    npm run serve

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

## How does the app work?

- views.py is the application routing file
- base.html/index.html/result.html are template files, no algorithmic element at this
- run.py is the entry point of the application

## Algorithm

## Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


