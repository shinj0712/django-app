FROM python:3.10-slim

# コンソールのバッファを無効にする
ENV PYTHONBURRERED 1

# 必要なライブラリをインストール
RUN apt-get update && apt-get install -y \
    cron \
    busybox-static \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY ./docker/backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

# bash aliasを設定
COPY ./.alias /root
RUN cat /root/.alias >> /root/.bashrc

RUN mkdir /backend
WORKDIR /backend
