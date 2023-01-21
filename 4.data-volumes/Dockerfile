FROM node:14

WORKDIR /app

COPY package.json .

RUN npm i

COPY . .

EXPOSE 80

# VOLUME [ "/app/feedback" ] Anonymous Volume

CMD [ "node", "server.js" ]