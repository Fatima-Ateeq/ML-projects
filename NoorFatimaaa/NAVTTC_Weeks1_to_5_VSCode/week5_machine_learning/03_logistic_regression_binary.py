# Week 5 — Logistic regression for binary classification
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

df = pd.DataFrame({
    "study_hours": [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 1.2, 2.2, 3.2, 4.2],
    "attendance":  [40, 45, 50, 55, 60, 62, 65, 70, 75, 80, 85, 90, 48, 58, 66, 74],
    "passed":      [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1]
})
X = df[["study_hours", "attendance"]]
y = df["passed"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42, stratify=y
)
model = make_pipeline(StandardScaler(), LogisticRegression(random_state=42))
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Accuracy:", round(accuracy_score(y_test, pred), 3))
print("Confusion matrix:\n", confusion_matrix(y_test, pred))
print("Report:\n", classification_report(y_test, pred, zero_division=0))

new_student = pd.DataFrame({"study_hours": [3.8], "attendance": [72]})
print("Pass prediction (1=pass, 0=not pass):", model.predict(new_student)[0])
print("Pass probability:", round(model.predict_proba(new_student)[0][1], 3))
