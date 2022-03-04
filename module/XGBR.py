class learning_val():
    def __init__(self, X_train, X_test, y_train, y_test, forecast):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test
        self.forecast = forecast

    def XGB_gs(self):
        param = {
        'max_depth':[2,3,4],
        'n_estimators':range(300,600,100), #  'n_estimators':range(600,700,50) 여기에 cv 10 (이거와 별반차이가 없다.)
        'colsample_bytree':[0.5,0.7,1],
        'colsample_bylevel':[0.5,0.7,1]
        }

        model = XGBRegressor()

        gs = GridSearchCV(estimator=model, param_grid=param, cv=10, 
                           scoring='neg_mean_squared_error',
                           n_jobs=multiprocessing.cpu_count())

        gs.fit(self.X_train, self.y_train)

        print(self.gs.best_params_)
        print(gs.best_score_)

        return self.gs.best_params_
    
    def XGB_fit(self):
        self.XGB_gs().fit(self.X_train, self.y_train)
        xgb.plot_importance(self.XGB_gs())

    
    def XGB_score(self):
        print("훈련결과 : {}".format(self.XGB_gs().score(self.X_train, self.y_train)))
        print("점검결과 : {}".format(self.XGB_gs().score(self.X_test, self.y_test)))
    

    def XGB_predict(self):
        model = self.XGB_gs().fit(self.X_train, self.y_train)
        forecast = model.predict(self.forecast)
        forecast_df = pd.DataFrame(forecast)
        forecast_df.columns = ['forecast']
        forecast_df.to_csv("data/forecast/fore_data.csv", encoding='utf-8', index=False)

        return forecast_df
        
