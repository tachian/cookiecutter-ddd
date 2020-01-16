FROM python:3.7-alpine3.9

LABEL maintainer="Lendico <contato@lendico.com.br>"
LABEL "service-name"="inbound-api"
LABEL "api-version"="1"

ENV HOME=/home/lendico
ENV DEPLOY_ENV=Production

RUN apk update && apk add --no-cache --update curl bash git openssh-client libffi-dev python3-dev postgresql-dev gcc musl-dev linux-headers \
    alpine-sdk curl-dev libressl-dev && addgroup lendico && adduser -D -G lendico lendico && mkdir -p ${HOME}/logs

WORKDIR ${HOME}
COPY . ${HOME}

RUN mkdir /root/.ssh/ && \
    mv ${HOME}/dockerfiles/id_rsa /root/.ssh && \
    sh -c "echo -e \"Host *\n StrictHostKeyChecking no\n\" > /root/.ssh/config" && \
    chmod 400 /root/.ssh/id_rsa && \
    pip install -r requirements.txt && \
    apk del openssh-client linux-headers alpine-sdk && \
    rm -rf /var/cache/apk/*

EXPOSE 9000

CMD ["flask", "run"]