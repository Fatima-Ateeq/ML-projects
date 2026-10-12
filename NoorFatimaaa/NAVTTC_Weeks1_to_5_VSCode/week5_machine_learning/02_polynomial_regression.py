# Week 5 — Polynomial regression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

X = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=float).reshape(-1, 1)
y = np.array([15, 18, 25, 37, 54, 76, 103, 135], dtype=float)

model = make_pipeline(PolynomialFeatures(degree=2), LinearRegression())
model.fit(X, y)
pred = model.predict(X)

print("Predicted value at x=5.5:", round(model.predict([[5.5]])[0], 2))
print("R² on this practice dataset:", round(r2_score(y, pred), 3))

smooth_x = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
plt.scatter(X, y, label="Observed data")
plt.plot(smooth_x, model.predict(smooth_x), label="Polynomial curve")
plt.xlabel("Input")
plt.ylabel("Output")
plt.title("Polynomial Regression (degree 2)")
plt.legend()
plt.tight_layout()
plt.show()
