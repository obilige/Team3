# learning in Google Colab
# tf 2 / keras

# data read
# lunch = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/data/lunch_df_encoding.csv")
# dinner = pd.read_csv("/content/drive/MyDrive/Colab Notebooks/data/dinner_df_encoding.csv")

class LSTM:
    def __init__(self, lunch, dinner):
        self.lunch = lunch
        self.dinner = dinner
    

    def learning_lunch(self):
        lunch = self.lunch
        # 결측치 제거
        lunch = lunch.dropna()
        lunch = lunch.drop(['datetime', 'year', 'month', 'date'], axis = 'columns')

        # 데이터 스케일링
        standard_scaler = StandardScaler()
        lunch_fitted = standard_scaler.fit(lunch)
        lunch_output = standard_scaler.transform(lunch)
        lunch_output = pd.DataFrame(lunch_output, columns=lunch.columns, index=list(lunch.index.values))
        
        # train, validation, test data 만들기
        train_size = int(len(lunch_output)*0.6)
        validation_size = int(len(lunch_output)*0.3)+train_size
        #점심
        train_x = np.array(lunch_output[:train_size])
        train_y = np.array(lunch_output['lunch_number'][:train_size])
        validation_x =np.array(lunch_output[train_size:validation_size])
        validation_y = np.array(lunch_output['lunch_number'][train_size:validation_size])
        test_x = np.array(lunch_output[validation_size:])
        test_y = np.array(lunch_output['lunch_number'][validation_size:])
        
        # 파라미터
        learning_rate = 0.01
        training_cnt = 100
        batch_size = 200
        input_size = train_x.shape[1]
        time_step = 1

        # 시계열 배열 맞추기(데이터 총 수, ***time_step, 데이터 입력값 수)
        train_x = train_x.reshape(train_x.shape[0], time_step, input_size)
        validation_x = validation_x.reshape(validation_x.shape[0], time_step, input_size)
        test_x = test_x.reshape(test_x.shape[0], time_step, input_size)

        # 모델 구조
        model = Sequential()
        model.add(LSTM(1024,input_shape=(1,input_size))) # 512는 다른 숫자로도 가능
        model.add(Dropout(0.2)) 
        model.add(Dense(1))

        # 오차 및 최적화기 설정
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=learning_rate), metrics=['mae','mape'])
        model.summary()

        # 학습
        history = model.fit(train_x,train_y,epochs=training_cnt, batch_size=batch_size, verbose=1)
        val_mse, val_mae, val_mape = model.evaluate(test_x, test_y, verbose=0)

        # 결과 시각화
        pred = model.predict(validation_x)

        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(validation_y, label='True')
        ax.plot(pred, label='Prediction')
        ax.legend()
        plt.show()
        
        # 예상 사내 인원수, 예상 기온, 날씨 등 원인변수 입력하면 예측값이 나오도록 설정


    def learning_dinner(self):
        # 결측치 제거
        dinner = self.dinner
        dinner = dinner.dropna()
        dinner = dinner.drop(['datetime', 'year', 'month', 'date'], axis = 'columns')

        # 데이터 스케일링
        standard_scaler = StandardScaler()
        dinner_fitted = standard_scaler.fit(dinner)
        dinner_output = standard_scaler.transform(dinner)
        dinner_output = pd.DataFrame(dinner_output, columns=dinner.columns, index=list(dinner.index.values))
        
        # train, validation, test data 만들기
        train_size = int(len(lunch_output)*0.6)
        validation_size = int(len(lunch_output)*0.3)+train_size
        #저녁
        train_x = np.array(dinner_output[:train_size])
        train_y = np.array(dinner_output['dinner_number'][:train_size])
        validation_x =np.array(dinner_output[train_size:validation_size])
        validation_y = np.array(dinner_output['dinner_number'][train_size:validation_size])
        test_x = np.array(dinner_output[validation_size:])
        test_y = np.array(dinner_output['dinner_number'][validation_size:])

        # 파라미터
        learning_rate = 0.01
        training_cnt = 100
        batch_size = 200
        input_size = train_x.shape[1]
        time_step = 1

        # 시계열 배열 맞추기(데이터 총 수, ***time_step, 데이터 입력값 수)
        train_x = train_x.reshape(train_x.shape[0], time_step, input_size)
        validation_x = validation_x.reshape(validation_x.shape[0], time_step, input_size)
        test_x = test_x.reshape(test_x.shape[0], time_step, input_size)

        # 모델 구조
        model = Sequential()
        model.add(LSTM(1024,input_shape=(1,input_size))) # 512는 다른 숫자로도 가능
        model.add(Dropout(0.2)) 
        model.add(Dense(1))

        # 오차 및 최적화기 설정
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=learning_rate), metrics=['mae','mape'])
        model.summary()

        # 학습
        history = model.fit(train_x,train_y,epochs=training_cnt, batch_size=batch_size, verbose=1)
        val_mse, val_mae, val_mape = model.evaluate(test_x, test_y, verbose=0)

        # 결과 시각화
        pred = model.predict(validation_x)

        fig = plt.figure(facecolor='white', figsize=(20, 10))
        ax = fig.add_subplot(111)
        ax.plot(validation_y, label='True')
        ax.plot(pred, label='Prediction')
        ax.legend()
        plt.show()