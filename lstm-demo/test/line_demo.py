import numpy as np
from tensorflow import keras

# 训练线性回归模型 y=ax + b
model = keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])
model.compile(optimizer='sgd', loss='mean_squared_error')

xs = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], dtype=float)
ys = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0], dtype=float)

model.fit(xs, ys, epochs=100, batch_size=10, verbose=1)

model.predict(np.array([9], dtype=float))

model.summary()
