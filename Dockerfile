# Docker 이미지의 기반이 될 파이썬 버전을 지정합니다.
FROM python:3.8

# 작업 디렉토리 설정
WORKDIR /app

# 현재 디렉토리의 파일들을 컨테이너의 작업 디렉토리로 복사합니다.
COPY . /app

# 필요한 패키지를 설치합니다.
RUN pip install -r requirements.txt

# uWSGI를 사용하여 애플리케이션을 실행합니다.
CMD ["uwsgi", "--http", ":8000", "--module", "MiniSurveyProject-Django.wsgi"]

# docker-entrypoint.sh 스크립트 복사 및 실행 권한 부여
COPY docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# 컨테이너 실행 시 실행될 명령
ENTRYPOINT ["docker-entrypoint.sh"]