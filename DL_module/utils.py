import numpy as np


def read_SQL():
    pass

def preprocessing(df):
    feature_df = df[1:]
    label_df = df[:-1]
    return feature_df, label_df

def trans_timeseries(feature_df, label_df, time_step):
    feature_list = []
    label_list = []
    for i in range(len(feature_df) - time_step):
        feature_list.append(feature_df[i:i+time_step])
        label_list.append(label_df.iloc[i+time_step])
    return np.array(feature_list), np.array(label_list)