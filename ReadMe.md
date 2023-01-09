Git Repository : https://github.com/Jaewoo-Shin/Riid
# 의존성 설치 방법
requirements.txt에 의존성이 저장되어 있다.
의존성 설치를 위해서 아래의 코드를 입력하면 된다.

```pip install -r requirements.txt```

# 모델 학습, 서빙 코드 실행 방법
### 모델 학습
question3.ipynb 파일을 통해서 데이터를 불러 온 뒤 XGBClassifier을 사용히여 모델을 학습시킨다.
이 때, param_grid의 파라미터 값들로 GridSearch를 진행하게 되는데, 파라미터는 추가할 수 있다.
최종적으로 모델은 model로 저장된다.
### 서빙 코드 실행 방법
터미널에서 아래의 명령어 실행하면 된다.

```FLASK_APP=app.py FLASK_DEBUG=1 flask run```
입력 값으로는 csv를 받게되고 출력은 list형태로 이루어진다.

# 모델 서빙 RESTful API interface

## POST `/predict`

### Request

- Files
  - `csv`: 학생 정보 테이블 (각 row가 한 학생을 나타냄)

### Json Response
각 학생의  Adaptivity level을 {"Low", "Moderate", "High"}으로 나타낸 string list

# 간단한 모델 선택 이유 및 성능 평가 매트릭
Classification을 위한 간단하지만 성능이 좋은 ML 모델로써 ensemble과 boosting을 사용하는 XGBoost를 사용하였다.
성능평가 metric으로는 accuracy를 사용하였다.

# 간단한 모델 서빙 서버 아키텍쳐 다이어그램

[architecture](./architecture.png)

