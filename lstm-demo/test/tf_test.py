import tensorflow as tf
# print(tf.__version__)
import numpy as np
from tensorflow import keras

model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)
ys = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)

model.fit(xs, ys,epochs=500)

model.predict([10.0])
