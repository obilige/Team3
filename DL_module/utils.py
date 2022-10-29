import numpy as np
import pandas as pd
import sqlite3
from sklearn.model_selection import train_test_split
from os import mkdir

def read_lunch_SQL():
    ### start, end를 쿼리문에 잘 녹아들도록.
    ### db 내 적재된 datetime 기간 확인하고 start와 end가 그 기간에 들어가지 않으면 error 처리하기
    ### db에서 적재된 기간 자동으로 확인하고 이 기간 안에 있지 않으면 자동으로 에러처리하도록 발전시키기
    query_lunch = """SELECT l.lunch_number, l.datetime, vacation, worker_number, real_number, biztrip_number, overtime_number, telecom_number, vacation_number, new_lunch, lunch_rice, temperature, rain, wind, humidity, discomfort_index, perceived_temperature
    FROM lunch as l, weather as w, hr as h, calendar as c
    WHERE l.datetime = w.datetime
    AND w.datetime = h.datetime
    AND h.datetime = c.datetime;"""
    lunch_col = ['lunch_number', 'datetime', 'vacation', 'worker_number', 'real_number', 'biztrip_number', 'overtime_number', 'telecom_number', 'vacation_number', 'new_lunch', 'lunch_rice', 'temperature', 'rain', 'wind', 'humidity', 'discomfort_index', 'perceived_temperature']

    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute(query_lunch)
    lunch = [row for row in cursor]
    cursor.close

    return pd.DataFrame(lunch, columns=lunch_col)


def read_dinner_SQL():
    ### start, end를 쿼리문에 잘 녹아들도록.
    ### db 내 적재된 datetime 기간 확인하고 start와 end가 그 기간에 들어가지 않으면 error 처리하기
    ### db에서 적재된 기간 자동으로 확인하고 이 기간 안에 있지 않으면 자동으로 에러처리하도록 발전시키기
    query_dinner = """SELECT dinner_number, d.datetime, vacation, worker_number, real_number, biztrip_number, overtime_number, telecom_number, vacation_number, new_dinner, dinner_rice, temperature, rain, wind, humidity, discomfort_index, perceived_temperature
    FROM dinner as d, weather as w, hr as h, calendar as c
    WHERE d.datetime = w.datetime
    AND w.datetime = h.datetime
    AND h.datetime = c.datetime;"""

    dinner_col = ['dinner_number', 'datetime', 'vacation', 'worker_number', 'real_number', 'biztrip_number', 'overtime_number', 'telecom_number', 'vacation_number', 'new_dinner', 'dinner_rice', 'temperature', 'rain', 'wind', 'humidity', 'discomfort_index', 'perceived_temperature']

    conn = sqlite3.connect('data/database.db')
    cursor = conn.cursor()
    cursor.execute(query_dinner)
    dinner = [row for row in cursor]
    cursor.close

    return pd.DataFrame(dinner, columns=dinner_col)


def preprocessing(df):
    feature_df = df[df.columns[1:-1]]
    label_df = df[df.columns[0:1]]
    return feature_df, label_df


def train_test_split(feature_df, label_df, ratio=0.8):
    train_feature = feature_df.iloc[:len(feature_df.index)*ratio]
    train_label = label_df.iloc


def trans_train(feature_df, label_df, time_step):
    ### pythonic code! if you look this, TEST!
    ### feature = [feature_df[i:i+time_step] for i in range in range(len(feature_df) - time_step)]
    ### label = [label_df.iloc[i+time_step] for i in range in range(len(feature_df) - time_step)]
    
    feature_list = []
    label_list = []
    for i in range(len(feature_df) - time_step):
        feature_list.append(feature_df[i:i+time_step])
        label_list.append(label_df.iloc[i+time_step])
    return np.array(feature_list), np.array(label_list)


def trans_test(feature_df, time_step):
    # no label data
    # be expected feature data
    feature_list = []
    for i in range(len(feature_df) - time_step):
        feature_list.append(feature_df[i:i+time_step])
    return np.array(feature_list)


def split_timeseries(feature_np, label_np, ratio):    
    # train_X, target_X, train_y, target_y = train_test_split(feature_np, label_np, test_size=ratio, shuffle=True)
    # it`s bad bcs of timeseries

    boundary_index = len(feature_np) * (1 - ratio)
    
    train_X = feature_np[:boundary_index+1, :, :]
    train_y = label_np[:boundary_index+1]
    test_X = feature_np[boundary_index+1:, :, :]
    test_y = label_np[boundary_index+1:]

    return train_X, train_y, test_X, test_y
    



def save_SQL():
    pass

def save_CSV():
    pass
