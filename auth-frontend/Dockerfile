FROM node:12

WORKDIR /app
ADD ./auth-frontend /app

RUN yarn
RUN yarn build

ENV HOST 0.0.0.0
EXPOSE 3000

CMD [ "yarn", "start" ]
