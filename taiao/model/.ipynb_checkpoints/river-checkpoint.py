import tensorflow.keras as keras
import tensorflow.keras.backend as K
from tensorflow.keras.layers import Dense

def LSTM(depth,features,look_back,loss='mse',optimizer='adam'):
    model=keras.Sequential()
    model.add(keras.layers.LSTM(depth, input_shape=(look_back,features)))
    model.add(keras.layers.Dense(1))
    model.compile(loss=loss, optimizer=optimizer)
    return model
