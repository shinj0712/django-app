FROM node:18.14.0-alpine3.17
LABEL maintener="sakamoto shinji"

RUN mkdir /src
WORKDIR /src

# bash aliasを設定
COPY ./docker/bash.alias /root
RUN cat /root/bash.alias >> /root/.bashrc

COPY --chown=node:node ./frontend/src/package.json /frontend/src/package-lock.json ./src/
RUN yarn install --prod --frozen-lockfile

COPY --chown=node:node ./frontend/src ./src

# CMD ["node", "index.js"]