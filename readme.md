### 가상환경 설치 후 활성화
```
python -m venv .venv
.venv/scripts/activate (윈도우 기준)
```
### 템플릿 폴더 생성 후 html 파일 넣음
### requirements.txt를 생성후 필요한 패키지 넣기
```
pip install -r requirements.txt
```
### django 앱 생성
```
django-admin startproject core .
python manage.py startapp survey
```
### 모델정의 후 슈퍼유저 생성
```
python manage.py createsuperuser
```
### 관리자 페이지 언어 및 시간대 설정 변경
```
setting.py 부분에서 language 부분 ko-kr, timezone 부분을 Asia/Seoul 로 변경
```
### 240413 - 설문테스트 및 응답자 분포도 차트 생성 완료 및 테스트 성공
### 240414 - 질문당 차트 시각화 테스트 성공. 질문별 시각화 부분 수정 완료. 배포 준비중.
![](https://github.com/kyoorochi/OSStudy/blob/9a5cbf774508a68c3cc88c1175db7a498a8ff98b/05-Day5/images/testresultimage.jpg)