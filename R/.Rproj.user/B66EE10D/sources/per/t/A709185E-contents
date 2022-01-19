lunch <- read.csv("data/lunch_r.csv")
dinner <- read.csv("data/dinner_r.csv")
library(dplyr)
library(pwr)
library(pgirmess)
library(leaps)


#### 점검해봐야할 변수들
### 결과변수 : lunch_number / dinner_number
### 원인변수
## 이산변수 
# 2개 분류 : vacation, new_lunch & new_dinner
# 3개 이상 분류 : season, weekdays, month & day(Too much)
## 연속변수
# 이하 모든 변수들

### 분석방법에 대해
## 이산변수는 2분류는 t-test / 3 이상 분류는 anova
## 연속변수는 AIC로 파악





#### 1. t-test
### vacation이 Yes/No 일 때 점심, 저녁의 평균, 분산 차이 있나? 통계적으로 유의미한가?
## 점심
#	정규분포 확인. 휴일날 값이 정규분포를 따르지 않음
shapiro.test(lunch$lunch_number[lunch$vacation == "Y"])
shapiro.test(lunch$lunch_number[lunch$vacation == "N"])

#	wilcox test(정규분포가 아닐 때)
#	p-value : 1.08e-08 통계적으로 유의미한 차이 존재.
wilcox.test(lunch_number ~ vacation, data = lunch)


## 저녁
#	정규분포 확인. 다음날이 휴일일 때 값이 정규분포를 따르지 않음
shapiro.test(dinner$dinner_number[dinner$vacation == "Y"])
shapiro.test(dinner$dinner_number[dinner$vacation == "N"])

#	wilcox test(정규분포가 아닐 때)
#	p-value : 1.72e-10. 통계적으로 유의미한 차이 존재.
wilcox.test(dinner_number ~ vacation, data = dinner)





### new menu가 나오는 날일 때 평균, 분산 차이 있나? 통계적으로 유의미한가?
## 점심
#	정규분포 확인. 신메뉴가 나왔을 때의 값이 정규분포를 따르지 않음
shapiro.test(lunch$lunch_number[lunch$new_lunch == "Y"])
shapiro.test(lunch$lunch_number[lunch$new_lunch == "N"])

#	wilcox test(정규분포가 아닐 때)
#	p-value : 0.2538. 통계적으로 유의미한 차이 없음.
wilcox.test(lunch_number ~ new_lunch, data = lunch)


## 저녁
#	정규분포 확인. p-value < 2.2e-16으로 정규분포 아님
shapiro.test(dinner$dinner_number[dinner$new_dinner == "Y"])
shapiro.test(dinner$dinner_number[dinner$new_dinner == "N"])

#	wilcox test(정규분포가 아닐 때)
#	p-value : 0.5997. 통계적으로 유의미한 차이 없음.
wilcox.test(dinner_number ~ new_dinner, data = dinner)



#### 2. ANOVA
### 계절별 사내식당 인원 수 차이가 통계적으로 유의미한가? -> 계절별로 차이가 발생한다.
## 점심
#	정규분포 확인. p-value = 8.531e-06
result = aov(lunch_number ~ season, data = lunch)
shapiro.test(resid(result))

# Kruskal분석(정규분포가 아닐 때)
kruskal.test(lunch_number ~ season, data = lunch)
kruskalmc(lunch$lunch_number, lunch$season)


## 저녁
#	정규분포 확인. p-value < 2.2e-16
result = aov(dinner_number ~ season, data = dinner)
shapiro.test(resid(result))

# Kruskal분석(정규분포가 아닐 때)
kruskal.test(dinner_number ~ season, data = dinner)
kruskalmc(dinner$dinner_number, dinner$season)



### 요일별 사내식당 인원 수 차이가 통계적으로 유의미한가?
## 점심
#	정규분포 확인. p-value < 2.2e-16
result = aov(lunch_number ~ weekdays, data = lunch)
shapiro.test(resid(result))

# Kruskal분석(정규분포가 아닐 때)
kruskal.test(lunch_number ~ weekdays, data = lunch)
kruskalmc(lunch$lunch_number, lunch$weekdays)


## 저녁
#	정규분포 확인. p-value < 2.2e-16
result = aov(dinner_number ~ weekdays, data = dinner)
shapiro.test(resid(result))

# Kruskal분석(정규분포가 아닐 때)
kruskal.test(dinner_number ~ weekdays, data = dinner)
kruskalmc(dinner$dinner_number, dinner$weekdays)




#### 3. AIC & All Subset Regression
### DataFrame 내 모든 변수 중 선형회귀분석에 가장 적합한 변수들은 무엇인지 파악
## 점심
# AIC
fit <- lm(lunch_number ~ worker_number + real_number + vacation_number + biztrip_number + overtime_number + telecom_number + temperature + rain + wind + humidity + discomfort_index + perceived_temperature, data = lunch)
summary(fit)

AIC(fit)
# df      AIC
# fit   6 241.6429

# Backward Stepwise Regression
full.model <- lm(lunch_number ~ worker_number + real_number + vacation_number + biztrip_number + overtime_number + telecom_number + temperature + rain + wind + humidity + discomfort_index + perceived_temperature, data = lunch)
reduced.model <- step(full.model, direction = "backward")
reduced.model
# call에 최적의 회귀선을 도출해준다.
# lm(formula = Murder ~ Population + Illiteracy, data = df)


# Fowward Stepwise Regression
empty.model <- lm(lunch_number ~ worker_number + real_number + vacation_number + biztrip_number + overtime_number + telecom_number + temperature + rain + wind + humidity + discomfort_index + perceived_temperature, data = lunch)
added.model <- step(empty.model, direction = "forward",
                    scope = (lunch_number ~ .))
added.model
# call에 최적의 회귀선을 도출해준다.
# lm(formula = Murder ~ Population + Illiteracy, data = df)


## 저녁
# AIC
fit <- lm(dinner_number ~ worker_number + real_number + vacation_number + biztrip_number + overtime_number + telecom_number + temperature + rain + wind + humidity + discomfort_index + perceived_temperature, data = dinner)
summary(fit)

AIC(fit)

# Backward Stepwise Regression
full.model <- lm(dinner_number ~ worker_number + real_number + vacation_number + biztrip_number + overtime_number + telecom_number + temperature + rain + wind + humidity + discomfort_index + perceived_temperature, data = dinner)
reduced.model <- step(full.model, direction = "backward")
reduced.model


# Fowward Stepwise Regression
empty.model <- lm(dinner_number ~ worker_number + real_number + vacation_number + biztrip_number + overtime_number + telecom_number + temperature + rain + wind + humidity + discomfort_index + perceived_temperature, data = dinner)
added.model <- step(empty.model, direction = "forward",
                    scope = (lunch_number ~ .))
added.model



## 점심
# All Subset Regression
result <- regsubsets(lunch_number ~ worker_number + real_number + vacation_number + biztrip_number + overtime_number + telecom_number + temperature + rain + wind + humidity + discomfort_index + perceived_temperature, data = lunch, nbest = 13)
result
plot(result, scale="adjr2")

## 저녁
# All Subset Regression
result <- regsubsets(dinner_number ~ worker_number + real_number + vacation_number + biztrip_number + overtime_number + telecom_number + temperature + rain + wind + humidity + discomfort_index + perceived_temperature, data = dinner, nbest = 13)
result
plot(result, scale="adjr2")
