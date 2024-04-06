import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt
import tensorflow as tf

fashion_mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(train_images.shape, train_labels.shape, test_images.shape, test_labels)

plt.imshow(train_images[555])

# 训练分类模型
model = keras.Sequential()
model.add(keras.layers.Flatten(input_shape=[28, 28]))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=10)
model.evaluate(test_images, test_labels)

p = model.predict(np.array([test_images[56]]))
print(np.argmax(p))
plt.imshow(test_images[56])
print(test_labels[56])



