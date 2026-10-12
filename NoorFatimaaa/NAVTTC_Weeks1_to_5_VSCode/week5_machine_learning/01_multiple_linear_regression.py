# Week 5 — Multiple linear regression (more than one input feature)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 2, 6, 3, 7],
    "attendance":  [60, 65, 70, 72, 80, 85, 90, 95, 68, 82, 75, 92],
    "marks":       [40, 45, 53, 58, 66, 73, 81, 90, 48, 75, 56, 84]
})

X = df[["study_hours", "attendance"]]
y = df["marks"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Feature coefficients:", dict(zip(X.columns, model.coef_)))
print("Intercept:", round(model.intercept_, 2))
print("Actual marks:", y_test.tolist())
print("Predictions:", [round(x, 2) for x in pred])
print("MAE:", round(mean_absolute_error(y_test, pred), 2))
print("RMSE:", round(mean_squared_error(y_test, pred) ** 0.5, 2))
print("R²:", round(r2_score(y_test, pred), 3))

new_student = pd.DataFrame({"study_hours": [5], "attendance": [80]})
print("Prediction for new student:", round(model.predict(new_student)[0], 2))
