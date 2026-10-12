# Week 5 — Optional: univariate linear regression with gradient descent
# This demonstrates the learning process without scikit-learn.
import numpy as np

X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

# Standardize X to make gradient descent easier to follow.
x_mean = X.mean()
x_std = X.std()
X_scaled = (X - x_mean) / x_std

weight = 0.0
bias = 0.0
learning_rate = 0.05
epochs = 2000
n = len(X)

for epoch in range(epochs):
    predictions = weight * X_scaled + bias
    error = predictions - y
    dw = (2 / n) * np.sum(error * X_scaled)
    db = (2 / n) * np.sum(error)
    weight -= learning_rate * dw
    bias -= learning_rate * db

print("Learned weight (scaled X):", round(weight, 3))
print("Learned bias:", round(bias, 3))
print("Predictions:", np.round(weight * X_scaled + bias, 2))
print("Expected pattern is approximately y = 2*x + 1.")
