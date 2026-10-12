# Week 5 — Logistic regression for multiclass classification
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

df = pd.DataFrame({
    "study_hours": [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 2.2, 3.2, 4.2, 5.2, 1.8, 4.8],
    "attendance":  [40, 45, 50, 52, 58, 62, 66, 70, 75, 80, 85, 92, 51, 60, 68, 78, 48, 73],
    "grade":       ["C", "C", "C", "C", "B", "B", "B", "B", "A", "A", "A", "A", "C", "B", "B", "A", "C", "A"]
})
X = df[["study_hours", "attendance"]]
y = df["grade"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)
model = make_pipeline(StandardScaler(), LogisticRegression(max_iter=1000, random_state=42))
model.fit(X_train, y_train)
pred = model.predict(X_test)

print("Classes:", model.named_steps["logisticregression"].classes_)
print("Accuracy:", round(accuracy_score(y_test, pred), 3))
print("Report:\n", classification_report(y_test, pred, zero_division=0))

new_student = pd.DataFrame({"study_hours": [4.8], "attendance": [76]})
print("Predicted grade:", model.predict(new_student)[0])
print("Probabilities:", model.predict_proba(new_student).round(3))
