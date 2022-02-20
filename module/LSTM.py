# learning in Google Colab
# tf 2 / keras

# data read
# lunch = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/data/lunch_df_encoding.csv")
# dinner = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/data/dinner_df_encoding.csv")

class LSTM():
    def __init__(self, lunch, dinner):
        self.lunch = lunch
        self.dinner = dinner
    
    def Data(self):
        # 결측치 제거
        self.lunch = self.lunch.dropna()
        self.dinner = self.dinner.dropna()

        # 데이터 스케일링
        standard_scaler = StandardScaler()
        #점심
        lunch_fitted = standard_scaler.fit(self.lunch)
        lunch_output = standard_scaler.transform(self.lunch)
        lunch_output = pd.DataFrame(lunch_output, columns=self.lunch.columns, index=list(self.lunch.index.values))
        print(lunch_output.head())
        #저녁
        dinner_fitted = standard_scaler.fit(self.dinner)
        dinner_output = standard_scaler.transform(self.dinner)
        dinner_output = pd.DataFrame(dinner_output, columns=self.dinner.columns, index=list(self.dinner.index.values))
        print(dinner_output.head())

        
        