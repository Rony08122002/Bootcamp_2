import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import make_circles
from sklearn.model_selection import train_test_split

X, y = make_circles(n_samples=1000, noise=0.03, random_state=42)

plt.scatter(X[:, 0], X[:, 1], c=y, cmap='bwr')
plt.title("Dataset visualization")
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(1, input_shape=(2,), activation='sigmoid')
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

history = model.fit(X_train, y_train, epochs=100, verbose=0)

loss, accuracy = model.evaluate(X_test, y_test)
print(f'Basic Model Accuracy: {accuracy:.4f}')

improved_model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

improved_model.compile(optimizer='adam',
                       loss='binary_crossentropy',
                       metrics=['accuracy'])

history_improved = improved_model.fit(X_train, y_train, epochs=150, verbose=0)

loss_improved, accuracy_improved = improved_model.evaluate(X_test, y_test)
print(f'Improved Model Accuracy: {accuracy_improved:.4f}')

def plot_decision_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 200),
                         np.linspace(y_min, y_max, 200))
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.7, cmap='bwr')
    plt.scatter(X[:, 0], X[:, 1], c=y, s=20, edgecolors='k', cmap='bwr')
    plt.title("Decision Boundary")
    plt.show()

plot_decision_boundary(improved_model, X_test, y_test)

print("""
Key Takeaways:
- The basic model struggled because it was too simple.
- The improved model performed significantly better due to additional layers and neurons.
- Visualization of decision boundaries helps clearly understand how the model classifies data.
- Hyperparameter tuning and activation functions strongly affect model performance.
""")
