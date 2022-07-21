import tensorflow as tf
import keras.backend as K
from tensorflow.keras import layers
from tensorflow.keras import activations
from tensorflow.keras import models
from tensorflow.keras.models import Sequential
from keras.layers.core import Dense, Dropout
from tensorflow.keras.layers import LSTM
from keras.callbacks import EarlyStopping, ModelCheckpoint


def LSTM(maxchannel, col_num, learning_rate):   
    model = Sequential()
    model.add(LSTM(maxchannel,input_shape=(1, col_num)))
    model.add(Dropout(0.2)) 
    model.add(Dense(1))

    model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=learning_rate), metrics=['mae','mape'])

    return model