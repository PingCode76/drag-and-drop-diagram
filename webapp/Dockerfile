FROM node:10
#https://www.docker.com/blog/getting-started-with-docker-using-node-jspart-i/


#RUN apt-get update -y
# Create app directory
#WORKDIR /usr/src/app
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package.json package.json
#COPY package-lock.json package-lock.json

#USER node
# RUN yarn install
RUN npm install
RUN npm install @vue/cli@3.7.0 -g

# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

#EXPOSE 4000
CMD [ "node", "server.js" ]