#!/bin/sh
# docker-entrypoint.sh

# 데이터베이스 마이그레이션 실행
python manage.py makemigrations
python manage.py migrate

# Django 개발 서버 시작
python manage.py runserver 0.0.0.0