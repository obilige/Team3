# Final Project : 사내식당 식수 인원 예측 모델
![이미지](https://github.com/obilige/Team3/blob/master/image/Diagram_1.jpg)
- 목표 : 데이터 기반으로 정확도 높은 예측모델 수립해 잔반 발생량 등 사내식당에 들어가는 비용 절감
- 일정 : 2021.12.28 ~ 2022.01.20
- 과정 :  
    + pandas로 데이터 전처리 및 전처리 자동화
    + SQLite로 데이터 DB에 저장
    + R을 통해 변수가 통계적으로 의미있는지 파악
    + scikit-learn과 tensorflow로 예측모델 구축
    + DB 생성 및 DB에 데이터 입력, 데이터 전처리, 데이터 분석 모델 수립 및 실행까지 모듈화(module)
- 팀원 : @acesaga, @jiyun193, @kserjseob

## 1. Library
- python : 3.9.7
- sklearn : 1.0.1
- xgboost : 1.5.0
- lightgbm : 3.1.1
- tensorflow : 2.7
- pandas : 1.3.5
- numpy : 1.21.4
- matplotlib.pyplot : 3.5.0


## 2. DataFrame
![이미지](https://github.com/obilige/Team3/blob/master/image//Diagram_3.jpg)
- 결과변수 : 점심 인원 / 저녁 인원
- 원인변수 : 회사 근로자 수 / 일일 실질 근무자 수 / 메뉴 /
- 파생변수 :
    + 날짜 -> 계절, 월, 기온, 강수량, 강설량, 체감온도, 불쾌지수
    + 메뉴 -> 밥, 국, 메인반찬, 신메뉴 여부


## 3. Project
- 프로젝트 프로세스 :
![이미지](https://github.com/obilige/Team3/blob/master/image/Diagram_2.jpg)
![이미지](https://github.com/obilige/Team3/blob/master/image/Diagram_4.jpg)

## 4. Analysis
- Query : 쿼리문으로 DB에서 데이터를 조회, 분석해 다음과 같은 결과 도출
![이미지](https://github.com/obilige/Team3/blob/master/image/Diagram_5.png)
    + 메뉴에서 밥&특식, 찌개&국, 면유무 등에서 중식 인원 수에 영향이 있는 것으로 보임
    + 특히, 국 종류를 선호하는 것으로 판단
    + 기온별 차이에 따라 식수 인원 증감 X
    + 비 오는 경우 중식 이용 인원이 늘어나는 경향을 보임
    + 월요일에 이용 인원이 많으며 점점 줄어드는 경향을 보임
    + 마지막 주 수요일 저녁은 자기계발의 날로 석식 운영을 안한다는 것을 파악
    + 연휴 전날 식수 인원 줄어드는 경향 보임

- Machine Learning
    + XGBMRegressor가 84%로 가장 좋은 성능을 보임
    + 다만, 저녁 데이터에서 좋지 않은 예측 결과를 보이고 있음
    + Linear보다 Tree형 분석모델이 더 좋은 성능을 보이는 것으로 보아 Deep Learning에서 좋은 결과를 보여줄 것으로 추측
![이미지](https://github.com/obilige/Team3/blob/master/image/Diagram_6.jpg)

- Deep Learning
    + RNN, LSTM으로 시계열 분석 예측 진행
    + 점심 : loss: 0.0012 - mae: 0.0249 - mape: 11.6815
    + 저녁 : loss: 0.0013 - mae: 0.0250 - mape: 11.4684
    + Validation 데이터로 성능 점검해본 결과 Machine Learning보다 우수한 성능을 보임
![이미지](https://github.com/obilige/Team3/blob/master/image/Diagram_7.jpg)