# Final Project : 사내식당 식수 인원 예측 모델
![이미지](https://github.com/obilige/Team3/blob/jaehoon/image/Diagram_1.jpg)
- 목표 : 데이터 기반으로 정확도 높은 예측모델 수립해 잔반 발생량 등 사내식당에 들어가는 비용을 줄이고자 합니다.
- 일정 : 2021.12.28 ~ 2022.01.20
- 과정 :  
    + pandas로 데이터 전처리 및 전처리 자동화
    + SQLite로 데이터 DB에 저장
    + R을 통해 변수가 통계적으로 의미있는지 파악
    + scikit-learn과 tensorflow로 예측모델 구축
- 팀원 : @acesaga, @jiyun193, @kserjseob

## 1. Library
- python : 3.9.7
- tensorflow : 2.7

## 2. DataFrame
![이미지](https://github.com/obilige/Team3/blob/jaehoon/image/Diagram_3.jpg)
- 결과변수 : 점심 인원 / 저녁 인원
- 원인변수 : 회사 근로자 수 / 일일 실질 근무자 수 / 메뉴 /
- 파생변수 :
    + 날짜 -> 계절, 월, 기온, 강수량, 강설량, 체감온도, 불쾌지수
    + 메뉴 -> 밥, 국, 메인반찬, 신메뉴 여부
