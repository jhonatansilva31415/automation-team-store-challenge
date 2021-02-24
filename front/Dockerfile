FROM node:14.15.5-alpine

WORKDIR /usr/src/front

ENV PATH /usr/src/front/node_modules/.bin:$PATH

COPY package.json ./
COPY package-lock.json ./
RUN yarn install 

COPY . ./

CMD ["yarn", "start"]