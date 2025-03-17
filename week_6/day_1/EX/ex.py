# 2
# weight_temp = 0.6
# weight_rain = 0.4
# bias = 2

# def activation(sum):
#     return 1 if sum > 20 else 0

# def perceptron(temp, rain):
#     weighted_sum = temp * weight_temp + rain * weight_rain + bias
#     decision = activation(weighted_sum)
#     return decision, weighted_sum

# case1 = perceptron(70, 0)  # Temperature = 70°F, Rain = No
# case2 = perceptron(50, 1)  # Temperature = 50°F, Rain = Yes

# print(f"Case 1 (70°F, No rain): {'Go outside' if case1[0] else 'Stay inside'}, Weighted sum: {case1[1]}")
# print(f"Case 2 (50°F, Rainy): {'Go outside' if case2[0] else 'Stay inside'}, Weighted sum: {case2[1]}")


# 3
# import tensorflow as tf
# from tensorflow.keras.datasets import mnist
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Flatten
# from tensorflow.keras.utils import to_categorical

# (x_train, y_train), (x_test, y_test) = mnist.load_data()

# x_train = x_train / 255.0
# x_test = x_test / 255.0

# y_train = to_categorical(y_train, 10)
# y_test = to_categorical(y_test, 10)

# model = Sequential([
#     Flatten(input_shape=(28, 28)),
#     Dense(128, activation='relu'),
#     Dense(10, activation='softmax')
# ])

# model.compile(optimizer='adam',
#               loss='categorical_crossentropy',  # loss function suitable for multi-class classification
#               metrics=['accuracy'])

# model.fit(x_train, y_train, epochs=10, batch_size=32)

# loss, accuracy = model.evaluate(x_test, y_test)
# print(f'Test accuracy: {accuracy:.4f}')


# 4
# x1 = 2000
# x2 = 3
# w1 = 0.5
# w2 = 0.7
# bias = 50000
# z = (x1 * w1) + (x2 * w2) + bias
# def relu(value):
#     return max(0, value)

# price = relu(z)
# print(f"The predicted house price is: ${price:.2f}")

# 5
# import numpy as np

# x = np.array([4, 80])

# w = np.array([0.6, 0.3])
# b = 10 

# def forward_propagation(x, w, b):
#     z = np.dot(x, w) + b 
#     return z 

# y_pred = forward_propagation(x, w, b)
# y_true = 85   

# loss = 0.5 * (y_true - y_pred) ** 2

# grad_w = -(y_true - y_pred) * x 
# grad_b = -(y_true - y_pred)     
# learning_rate = 0.01 
# w_new = w - learning_rate * grad_w
# b_new = b - learning_rate * grad_b

# print("firs impretoin:", y_pred)
# print("Loss:", loss)
# print(" rebot:", w_new)
# print("the new base:", b_new)

# 6
# שלב 1 - טעינת ספריות והנתונים
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = Sequential([
    Flatten(input_shape=(28, 28)),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.fit(x_train, y_train, epochs=5, batch_size=32)

predictions = model.predict(x_test)

fig, axes = plt.subplots(1, 5, figsize=(15, 4))
for i, ax in enumerate(axes):
    ax.imshow(x_test[i], cmap='gray')
    ax.axis('off')
    predicted_label = predictions[i].argmax()
    true_label = y_test[i].argmax()
    ax.set_title(f"Predicted: {predicted_label}\nTrue: {true_label}")
    
plt.show()
