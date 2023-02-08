#!/bin/sh
python manage.py makemigrations --noinput
python manage.py migrate --noinput
# python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8000

# 環境変数のAPP_ENVの値が 'production' の時はgunicornを、Falseの時はrunserverを実行します
# if [ $APP_ENV = 'production' ]; then
#     # gunicornを起動させる時はプロジェクト名を指定します
#     # 今回はdjangopjにします
#     gunicorn djangopj.wsgi:application --bind 0.0.0.0:8000
# else

# fi
