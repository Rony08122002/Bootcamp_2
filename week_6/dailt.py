import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train_flat = x_train.reshape(-1, 28 * 28).astype("float32") / 255.0
x_test_flat = x_test.reshape(-1, 28 * 28).astype("float32") / 255.0
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

fc_model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dropout(0.3),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

fc_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
fc_history = fc_model.fit(x_train_flat, y_train_cat, validation_split=0.1, epochs=10)

x_train_cnn = x_train.reshape(-1, 28, 28, 1).astype("float32") / 255.0
x_test_cnn = x_test.reshape(-1, 28, 28, 1).astype("float32") / 255.0

cnn_model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

cnn_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
cnn_history = cnn_model.fit(x_train_cnn, y_train_cat, validation_split=0.1, epochs=10)

fc_loss, fc_acc = fc_model.evaluate(x_test_flat, y_test_cat)
cnn_loss, cnn_acc = cnn_model.evaluate(x_test_cnn, y_test_cat)
print(f"Fully Connected NN Test Accuracy: {fc_acc:.4f}")
print(f"CNN Test Accuracy: {cnn_acc:.4f}")

plt.plot(fc_history.history['val_accuracy'], label='FCN Val Accuracy')
plt.plot(cnn_history.history['val_accuracy'], label='CNN Val Accuracy')
plt.title('Validation Accuracy Comparison')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()
#אני חייב לציין שכאן הייתי אבוד צ'ט GPT עשה בשבילי את רוב העבודה 