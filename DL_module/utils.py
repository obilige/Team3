import numpy as np
import sqlite3
from os import mkdir

def read_SQL():
    pass

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
