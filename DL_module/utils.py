import numpy as np


def read_SQL():
    pass

def preprocessing(df):
    df
    return df

def preprocessing(X_df, y_df, time_step):
    feature_list = []
    label_list = []
    for i in range(len(X_df) - time_step):
        feature_list.append(X_df[i:i+time_step])
        label_list.append(y_df.iloc[i+time_step])
    return np.array(feature_list), np.array(label_list)