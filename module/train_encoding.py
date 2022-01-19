from unicodedata import category

class Train_Encoding():
    def __init__(self, lunch, dinner):
        self.lunch = lunch
        self.dinner = dinner
    
    def Na(self):
        self.lunch = self.lunch.dropna()
        self.dinner = self.dinner.dropna()

        return self.lunch, self.dinner

    def split_lunch(self):
        lunch_data = self.lunch.drop("lunch_number", axis = "columns")
        lunch_target = self.lunch['lunch_number']
        self.lunch_X_train, self.lunch_X_test, self.lunch_y_train, self.lunch_y_test = train_test_split(lunch_data, lunch_target)

        return self.lunch_X_train, self.lunch_X_test, self.lunch_y_train, self.lunch_y_test

    def split_dinner(self):
        dinner_data = self.dinner.drop("dinner_number", axis = "columns")
        dinner_target = self.dinner['dinner_number']
        self.dinner_X_train, self.dinner_X_test, self.dinner_y_train, self.dinner_y_test = train_test_split(dinner_data, dinner_target)

        return self.dinner_X_train, self.dinner_X_test, self.dinner_y_train, self.dinner_y_test


    def format(self):
        data_list = [self.lunch_X_train, self.lunch_X_test, self.dinner_X_train, self.dinner_X_test]
        for data in data_list:
            data['year'] = data['year'].astype(category)
            data['month'] = data['month'].astype(category)
            data['date'] = data['date'].astype(category)
        
        return self.lunch_X_train, self.lunch_X_test, self.dinner_X_train, self.dinner_X_test
        
    def label_rice(self):
        data_list = [self.lunch_X_train, self.lunch_X_test, self.dinner_X_train, self.dinner_X_test]
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




    