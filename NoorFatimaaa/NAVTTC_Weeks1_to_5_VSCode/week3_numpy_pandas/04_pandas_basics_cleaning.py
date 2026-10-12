# Week 3 — Pandas Series/DataFrame, selection, nulls, replacement, CSV
import pandas as pd
from pathlib import Path

data = {
    "name": ["Ali", "Sara", "Hina", "Omar", "Zoya"],
    "age": [22, 24, None, 21, 25],
    "marks": [78, 91, 85, None, 88],
    "city": ["Lahore", "Lahore", "Karachi", "Lahore", "Karachi"]
}
df = pd.DataFrame(data)

print("First rows:\n", df.head())
print("\nInfo:")
df.info()
print("\nSummary:\n", df.describe(numeric_only=True))
print("\nColumns:", df.columns.tolist())
print("\nUnique cities:", df["city"].unique())
print("\nCity counts:\n", df["city"].value_counts())
print("\nRows with marks >= 85:\n", df.loc[df["marks"] >= 85, ["name", "marks"]])

print("\nMissing values:\n", df.isna().sum())
df["age"] = df["age"].fillna(df["age"].median())
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["city"] = df["city"].replace({"Karachi": "Karachi City"})
print("\nCleaned data:\n", df)

output = Path(__file__).with_name("students_cleaned.csv")
df.to_csv(output, index=False)
print("Saved:", output)
