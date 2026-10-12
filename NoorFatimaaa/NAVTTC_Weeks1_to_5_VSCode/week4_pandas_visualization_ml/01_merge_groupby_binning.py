# Week 4 — Merge, groupby, binning, save output
import pandas as pd
from pathlib import Path

students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "name": ["Ali", "Sara", "Hina", "Omar"],
    "marks": [65, 92, 78, 48]
})
attendance = pd.DataFrame({
    "student_id": [1, 2, 3, 5],
    "attendance_pct": [80, 95, 88, 70]
})

merged = pd.merge(students, attendance, on="student_id", how="left")
merged["grade_band"] = pd.cut(
    merged["marks"],
    bins=[0, 50, 70, 85, 100],
    labels=["Needs work", "C", "B", "A"],
    include_lowest=True
)
print("Merged data:\n", merged)
print("\nAverage marks by grade band:\n", merged.groupby("grade_band", observed=False)["marks"].mean())

output = Path(__file__).with_name("student_report.csv")
merged.to_csv(output, index=False)
print("Saved:", output)
