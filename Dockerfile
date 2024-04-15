# Docker 이미지의 기반을 정의 (Python 3.12 버전을 사용하는 공식 이미지)
FROM python:3.12

# 환경변수 설정 (Python이 버퍼링 없이 직접 콘솔에 출력하도록 함)
ENV PYTHONUNBUFFERED 1

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# 현재 디렉토리의 모든 파일을 컨테이너의 작업 디렉토리로 복사
COPY . /app/