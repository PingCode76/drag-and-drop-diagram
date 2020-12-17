# Drag and drop system for diagram

Generate a data with a diagram, created with drag and drop

## Use the app 

## Technologies
    - Flask
    - Vue.js
    - Drag and Drop Component : Easy-Dnd ( https://github.com/rlemaigre/Easy-DnD ) 

## Generality

install the necessary library

```bash
$ pip install pipreqs
$ pipreqs
$ pip install -r requirements.txt
```

Launch a python server in /api, available in http://127.0.0.1:5000/ :

```bash
$ flask run 
```

Launch a Vue server with yarn or npm in webapp folder, available in http://localhost:4000/:

```bash
$ npm install
$ npm run serve
```

or

```bash
$ yarn install
$ yarn serve
```

## DataBase

    - Install PostGresSQL et create database 
    - change database configuration ( config.py ) 
    
```bash
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```

## Docker
```bash
$ Docker-compose up --build
```

## Algorithm

## Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).


