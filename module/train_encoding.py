from sklearn.model_selection import train_test_split
from unicodedata import category

class Train_Encoding():
    def __init__(self, lunch, dinner):
        self.lunch = lunch
        self.dinner = dinner
    
    def kor_eng_lunch(self):
        lunch = self.lunch
        for i in range(len(lunch.index)):
            if lunch['season'][i] == "겨울":
                lunch['season'][i] = "winter"
            elif lunch['season'][i] == "봄":
                lunch['season'][i] = "spring"
            elif lunch['season'][i] == "여름":
                lunch['season'][i] = "summer"
            elif lunch['season'][i] == "가을":
                lunch['season'][i] = "fall"
            else:
                pass
        
        for i in range(len(lunch.index)):
            if lunch['weekdays'][i] == "월":
                lunch['weekdays'][i] = "monday"
            elif lunch['weekdays'][i] == "화":
                lunch['weekdays'][i] = "tuesday"
            elif lunch['weekdays'][i] == "수":
                lunch['weekdays'][i] = "wednesday"
            elif lunch['weekdays'][i] == "목":
                lunch['weekdays'][i] = "thursday"
            elif lunch['weekdays'][i] == "금":
                lunch['weekdays'][i] = "friday"
            elif lunch['weekdays'][i] == "토":
                lunch['weekdays'][i] = "saturday"
            elif lunch['weekdays'][i] == "일":
                lunch['weekdays'][i] = "sunday"
            else:
                pass
    
    def kor_eng_dinner(self):
        dinner = self.dinner
        for i in range(len(dinner.index)):
            if dinner['season'][i] == "겨울":
                dinner['season'][i] = "winter"
            elif dinner['season'][i] == "봄":
                dinner['season'][i] = "spring"
            elif dinner['season'][i] == "여름":
                dinner['season'][i] = "summer"
            elif dinner['season'][i] == "가을":
                dinner['season'][i] = "fall"
            else:
                pass
        
        for i in range(len(dinner.index)):
            if dinner['weekdays'][i] == "월":
                dinner['weekdays'][i] = "monday"
            elif dinner['weekdays'][i] == "화":
                dinner['weekdays'][i] = "tuesday"
            elif dinner['weekdays'][i] == "수":
                dinner['weekdays'][i] = "wednesday"
            elif dinner['weekdays'][i] == "목":
                dinner['weekdays'][i] = "thursday"
            elif dinner['weekdays'][i] == "금":
                dinner['weekdays'][i] = "friday"
            elif dinner['weekdays'][i] == "토":
                dinner['weekdays'][i] = "saturday"
            elif dinner['weekdays'][i] == "일":
                dinner['weekdays'][i] = "sunday"
            else:
                pass

    #결측치 제거
    def dropna_lunch(self):
        lunch = self.kor_eng_lunch().dropna()

        return lunch

    def dropna_dinner(self):
        dinner = self.kor_eng_dinner().dropna()

        return dinner


    #밥, 국, 메인반찬은 종류가 onehot encoding시 너무 복잡해집니다. 그래서 일반 밥과 특식 밥 메뉴 둘로 나눴고 Y, N으로 구분해줍니다.
    def rice_lunch(self):
        lunch = self.dropna_lunch()
        for index in range(len(lunch['lunch_rice'])):
            if index == "밥":
                lunch['lunch_rice'][index] = "Y"
            else:
                lunch['lunch_rice'][index] = "N"
        
        del lunch['lunch_soup']
        del lunch['lunch_main']

        return lunch
        
    def rice_dinner(self):
        dinner = self.dropna_dinner()
        for index in range(len(dinner['dinner_rice'])):
            if index == "밥":
                dinner['dinner_rice'][index] = "Y"
            else:
                dinner['lunch_rice'][index] = "N"
        
        del dinner['dinner_soup']
        del dinner['dinner_main']
        
        return dinner

    
    #훈련 성능을 위해 원핫인코딩 진행합니다.
    #추가적으로 MinMax Scalar, Feature Scaling 같은 정규화 작업도 추가해주면 좋을 듯합니다. 다음에
    def onehot_lunch(self):
        lunch = self.rice_lunch()

        time = ["year", "month", "date"]
        for col in time:
            lunch[col] = lunch[col].astype('category')

        lunch = pd.get_dummies(lunch)

        for col in time:
            lunch[col] = lunch[col].astype(int)
        
        return lunch
    
    def onehot_dinner(self):
        dinner = self.rice_dinner()

        time = ["year", "month", "date"]
        for col in time:
            dinner[col] = dinner[col].astype('category')

        dinner = pd.get_dummies(dinner)

        for col in time:
            dinner[col] = dinner[col].astype(int)

        return dinner


    # 최종적으로 훈련용과 테스트용으로 데이터를 나누는 함수입니다. 랜덤하게 뽑기 위해 sklearn에 train_test_split 사용했습니다.
    def split_lunch(self):
        lunch_data = self.onehot_lunch().drop("lunch_number", axis = "columns")
        lunch_target = self.onehot_lunch()['lunch_number']
        lunch_X_train, lunch_X_test, lunch_y_train, lunch_y_test = train_test_split(lunch_data, lunch_target)

        return lunch_X_train, lunch_X_test, lunch_y_train, lunch_y_test

    def split_dinner(self):
        dinner_data = self.onehot_dinner().drop("dinner_number", axis = "columns")
        dinner_target = self.onehot_dinner()['dinner_number']
        dinner_X_train, dinner_X_test, dinner_y_train, dinner_y_test = train_test_split(dinner_data, dinner_target)

        return dinner_X_train, dinner_X_test, dinner_y_train, dinner_y_test


    # 형태를 변경해줘야하는건 train 데이터만
    # split_lunch와 split_dinner에서 train 데이터만 뽑아오는게 효율적일까? 유지보수 측면에서 불리하지 않울까?