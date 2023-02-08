# pythonイメージ
FROM python:3.11-slim

# pycファイル(および__pycache__)の生成を行わないようにする
ENV PYTHONDONTWRITEBYTECODE=1
# 標準出力・標準エラーのストリームのバッファリングを行わない
ENV PYTHONUNBUFFERED=1

# コンテナのワークディレクトリを /code に指定
RUN mkdir /src
WORKDIR /src

# 必要なライブラリをインストール
RUN apt-get update && apt-get install -y \
    cron \
    busybox-static \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

# ローカルのrequirements.txtをコンテナの/codeフォルダ直下に置く
COPY ./docker/app/requirements.txt /src
RUN pip install -r requirements.txt

# bash aliasを設定
COPY ./docker/app/bash.alias /root
RUN cat /root/bash.alias >> /root/.bashrc
