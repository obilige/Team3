from unicodedata import category

class Train_Encoding():
    def __init__(self, lunch, dinner):
        self.lunch = lunch
        self.dinner = dinner
    
    def dropna_lunch(self):
        self.lunch = self.lunch.dropna()

        return self.lunch

    def dropna_dinner(self):
        self.dinner = self.dinner.dropna()

        return self.dinner

    # db엔 점심, 저녁 따로 저장되어있음
    # 실수 : 식수인원 칼럼명을 lunch_number가 아닌 number로 바꾸면 클래스 입력된 데이터에 따라 자유롭게 적용 가능
    # 여기선 lunch_number, dinner_number 따로 해놨으므로 함수를 두 번 만들어야하는 번거로움 발생
    def split_lunch(self):
        lunch_data = self.dropna_lunch().drop("lunch_number", axis = "columns")
        lunch_target = self.lunch['lunch_number']
        self.lunch_X_train, self.lunch_X_test, self.lunch_y_train, self.lunch_y_test = train_test_split(lunch_data, lunch_target)

        return self.lunch_X_train, self.lunch_X_test, self.lunch_y_train, self.lunch_y_test

    def split_dinner(self):
        dinner_data = self.dropna_dinner().drop("dinner_number", axis = "columns")
        dinner_target = self.dinner['dinner_number']
        self.dinner_X_train, self.dinner_X_test, self.dinner_y_train, self.dinner_y_test = train_test_split(dinner_data, dinner_target)

        return self.dinner_X_train, self.dinner_X_test, self.dinner_y_train, self.dinner_y_test


    # 형태를 변경해줘야하는건 train 데이터만
    # split_lunch와 dinner에서 train 데이터만 뽑아오는게 효율적일까? 유지보수 측면에서 불리하지 않울까?

    def format(self):
        data_list = [self.dropna_lunch()[0], self.dropna_lunch()[2], self.dropna_dinner[0], self.dropna_dinner[2]]
        for data in data_list:
            data['year'] = data['year'].astype(category)
            data['month'] = data['month'].astype(category)
            data['date'] = data['date'].astype(category)
        
        return self.lunch_X_train, self.lunch_X_test, self.dinner_X_train, self.dinner_X_test
        
    def label_rice(self):
        data_list = [self.format()]
        for data in data_list:
            for index in range(len(data['lunch_rice'])):
                if index == "밥":
                    data['lunch_rice'][index] = "Y"
                else:
                    data['lunch_rice'][index] = "N"
        
            del data['lunch_soup']
            del data['lunch_main']
            
        return self.lunch_X_train, self.lunch_X_test, self.dinner_X_train, self.dinner_X_test


    def onehot(self):
        data_list = [self.lunch_X_train, self.lunch_X_test, self.dinner_X_train, self.dinner_X_test]
        for data in data_list:
            data = pd.get_dummies(data)
        
        return self.lunch_X_train, self.lunch_X_test, self.dinner_X_train, self.dinner_X_test




    