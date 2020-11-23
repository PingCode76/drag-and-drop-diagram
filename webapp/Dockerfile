FROM node:lts-alpine
#https://www.docker.com/blog/getting-started-with-docker-using-node-jspart-i/

RUN npm install -g http-server
#RUN apt-get update -y
# Create app directory
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)

# COPY package*.json ./
COPY package.json ./ 
#COPY package-lock.json package-lock.json

#USER node

RUN npm install
#RUN npm install @vue/cli@3.7.0 -g

# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

#RUN npm run serve --port 4000
# or package.json "scripts": {     "serve": "vue-cli-service serve --port 4000"   }
#RUN npm run serve

EXPOSE 4000

#ENTRYPOINT ["run.py"]   #client/src/main.js

#CMD [ "node", "server.js" ]
CMD [ "http-server", "dist" ]