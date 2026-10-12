# Week 4 — Simple linear regression (one input feature)
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# Example: predict marks from study hours
X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]], dtype=float)
y = np.array([42, 48, 55, 61, 67, 74, 80, 87], dtype=float)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Actual:", y_test)
print("Predicted:", np.round(predictions, 2))
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
print("RMSE:", round(np.sqrt(mean_squared_error(y_test, predictions)), 2))
print("R²:", round(r2_score(y_test, predictions), 3))
print("Predicted marks for 5.5 study hours:", round(model.predict([[5.5]])[0], 2))

plt.scatter(X, y, label="Data")
plt.plot(X, model.predict(X), label="Regression line")
plt.xlabel("Study hours")
plt.ylabel("Marks")
plt.title("Simple Linear Regression")
plt.legend()
plt.tight_layout()
plt.show()
