# 3
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import mean_squared_error

# np.random.seed(0)
# x = np.arange(-1, 1, 0.1)
# y = -x**2 + np.random.normal(0, 0.05, len(x))

# plt.scatter(x, y, color='blue', label='Data with noise')
# plt.title('Scatter plot of generated data with noise')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.grid()
# plt.show()

# x_train, y_train = x[:12], y[:12]
# x_test, y_test = x[12:], y[12:]

# print("Training Set:\n", x_train, y_train)
# print("\nTest Set:\n", x_test, y_test)

# 4
# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(0)
# x = np.arange(-1, 1, 0.1)
# y = -x**2 + np.random.normal(0, 0.05, len(x))

# x_train, y_train = x[:12], y[:12]
# x_test, y_test = x[12:], y[12:]

# def polynomial_fit(degree):
#     return np.poly1d(np.polyfit(x_train, y_train, degree))

# def plot_polyfit(degree):
#     poly = polynomial_fit(degree)
#     x_range = np.linspace(-1, 1, 100)

#     plt.scatter(x_train, y_train, color='blue', label='Training data')
#     plt.scatter(x_test, y_test, color='red', label='Test data')
#     plt.plot(x_range, poly(x_range), color='green', label=f'Polynomial degree {degree}')
#     plt.title(f'Polynomial Fit (degree={degree})')
#     plt.xlabel('X')
#     plt.ylabel('Y')
#     plt.legend()
#     plt.grid(True)
#     plt.show()

# for degree in [1, 7, 11]:
#     plot_polyfit(degree)

# 5
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

np.random.seed(0)
x = np.arange(-1, 1, 0.1)
y = -x**2 + np.random.normal(0, 0.05, len(x))

x_train, y_train = x[:12], y[:12]
x_test, y_test = x[12:], y[12:]

results = []

degrees = range(1, 12)
for degree in degrees:
    poly = np.poly1d(np.polyfit(x_train, y_train, degree))
    
    y_train_pred = poly(x_train)
    y_test_pred = poly(x_test)
    
    rmse_train = np.sqrt(mean_squared_error(y_train, y_train_pred))
    rmse_test = np.sqrt(mean_squared_error(y_test, y_test_pred))
    
    results.append((degree, rmse_train, rmse_test))

results = np.array(results)

plt.figure(figsize=(10,6))
plt.plot(results[:,0], results[:,1], label='Training RMSE', marker='o')
plt.plot(results[:,0], results[:,2], label='Test RMSE', marker='s')

plt.yscale('log')
plt.xlabel('Polynomial Degree')
plt.ylabel('RMSE (log scale)')
plt.title('RMSE for different Polynomial Degrees')
plt.legend()
plt.grid(True)
plt.show()

optimal_degree = int(results[np.argmin(results[:,2]),0])
print(f"The optimal polynomial degree is: {optimal_degree}")
