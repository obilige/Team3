import numpy as np
import pandas as pd
import sqlite3
from os import mkdir

def read_SQL(start, end):
### 2022.07.29, jaehoon : start, end를 쿼리문에 잘 녹아들도록.
### db 내 적재된 datetime 기간 확인하고 start와 end가 그 기간에 들어가지 않으면 error 처리하기
### db에서 적재된 기간 자동으로 확인하고 이 기간 안에 있지 않으면 자동으로 에러처리하도록 발전시키기
    query_lunch = """SELECT l.lunch_number, l.datetime, vacation, worker_number, real_number, biztrip_number, overtime_number, telecom_number, vacation_number, new_lunch, lunch_rice, temperature, rain, wind, humidity, discomfort_index, perceived_temperature
    FROM lunch as l, weather as w, hr as h, calendar as c
    WHERE l.datetime = w.datetime
    AND w.datetime = h.datetime
    AND h.datetime = c.datetime;"""

    query_dinner = """SELECT dinner_number, d.datetime, vacation, worker_number, real_number, biztrip_number, overtime_number, telecom_number, vacation_number, new_dinner, dinner_rice, temperature, rain, wind, humidity, discomfort_index, perceived_temperature
    FROM dinner as d, weather as w, hr as h, calendar as c
    WHERE d.datetime = w.datetime
    AND w.datetime = h.datetime
    AND h.datetime = c.datetime;"""

    lunch_col = ['lunch_number', 'datetime', 'vacation', 'worker_number', 'real_number', 'biztrip_number', 'overtime_number', 'telecom_number', 'vacation_number', 'new_lunch', 'lunch_rice', 'temperature, rain', 'wind, humidity', 'discomfort_index', 'perceived_temperature']
    dinner_col = ['dinner_number', 'datetime', 'vacation', 'worker_number', 'real_number', 'biztrip_number', 'overtime_number', 'telecom_number', 'vacation_number', 'new_dinner', 'dinner_rice', 'temperature, rain', 'wind, humidity', 'discomfort_index', 'perceived_temperature']

    q_list = [query_lunch, query_dinner]
    df_list = []

    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    for q in q_list, :
        cursor.execute(q)
        data = []
        for row in cursor:
            data.append(row)
        df_list.append(data)   
    cursor.close

    return pd.DataFrame(df_list[0], columns=lunch_col), pd.DataFrame(df_list[1], columns=dinner_col)





def preprocessing(df):
    feature_df = df[1:]
    label_df = df[:-1]
    return feature_df, label_df

def trans_train(feature_df, label_df, time_step):
    feature_list = []
    label_list = []
    for i in range(len(feature_df) - time_step):
        feature_list.append(feature_df[i:i+time_step])
        label_list.append(label_df.iloc[i+time_step])
    return np.array(feature_list), np.array(label_list)

def trans_test(feature_df, time_step):
    feature_list = []
    for i in range(len(feature_df) - time_step):
        feature_list.append(feature_df[i:i+time_step])
    return np.array(feature_list)

def split_timeseries(feature_np, label_np, ratio):
    pass

def save_SQL():
    pass

def save_CSV():
    pass
