# Team 3 회의록
- Member
    + 정재훈, 박지윤, 이행철, 변주섭





## 2021.12.23 :: Telecommuting
- 1. TITLE : 머신러닝, 딥러닝 기반으로 예측하거나 분류 가능한 주제
    + 식수인원예측
    + 주차장차량예측
    + 영화 흥행 예측


## 2021.12. 27 :: Telecommuting
- 1. TITLE : 사내식당 식수인원예측
- 2. PURPOSE : 데이터 기반 사내식당 식수인원예측을 통해 비용절감 가능
3. CONCEPT
    + CJ프레시웨이, 삼성웰스토리 등 관련 기업과 연결지어 프로젝트 진행
    + 사내식당 관련 데이터에서 계절, 메뉴 등 관련 파생변수 생성
    + 기상청에서 날짜별 날씨 데이터 확보해 사내식당 관련 데이터와 결합
4. PLAN
    + 데이터 전처리(1월 6일)
    + R을 통한 통계적 의미 파악(1월 10일)
    + 예측모델 수립(1월 16일)
5. Language & Library
    + Python
    + Pandas
    + Seaborn
    + scikit-learn
    + tensorflow
    + R
    + SQLite


## 2022.01.06 :: Offline-Communication
1. Colarboration Tool
    + Git & Github : Master 설정 후 Branch에서 작업
    + 1월 10일 Merge 예정
    + Github url : http://github.com/obilige/team3
    + 행철, 지윤, 주섭 : EDA와 Visualization 강화, 변수 관련 코드 정리 끝내기(7일)
    + 재훈 : 7일날 받은 코드로 전처리 완료 및 SQLite로 DB생성 및 테이블 만들기
2. SQL
    + 인사 데이터, 사내식당데이터, 날씨데이터로 3등분. Key는 일자로 datetime형태


## 2022.01.10 :: Offline-Communication
1. EDA 결합 : 팀원들 각자 진행한 EDA 결합
2. Encoding
    - R 분석에 적합한 형태
    - One-Hot, Min-Max, 카테고리로 나눈 형태
3. SQL로 EDA에 맞게 데이터 조회하는 쿼리문 짜기
	- SELECT WHERE IN 등 다양하게 사용해 데이터 뽑아내기
	- 뽑아낸 데이터 SQLite3로 파이썬으로 추출하기
4. py파일로 소스화하는 방법에 대해 여쭤보고 계획 짜기


## 2022.01.11 :: Telecommuting
1. SQLite Setting 완료
2. Github merge
3. Data Encoding에서 MinMax Scalar or Standard Scalar는 필요에 따라 각자.
4. Data Encoding에서는 One-Hot Encoding과 불필요한 메뉴 제거, 카테고리화 작업 진행