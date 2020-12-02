FROM node:lts-alpine

RUN npm install -g http-server

WORKDIR /app

COPY package.json package.json

COPY . .

RUN npm install

EXPOSE 4000

CMD [ "http-server", "dist" ]