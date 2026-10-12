# Week 4 — Pandas plots: bar, histogram, line, scatter, box
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "sales": [120, 145, 138, 170, 190, 210],
    "expenses": [90, 95, 100, 115, 130, 140]
})

df.plot(x="month", y=["sales", "expenses"], kind="line", marker="o", title="Sales and Expenses")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

df["sales"].plot(kind="hist", title="Sales distribution")
plt.xlabel("Sales")
plt.tight_layout()
plt.show()

df.plot(x="expenses", y="sales", kind="scatter", title="Sales vs Expenses")
plt.tight_layout()
plt.show()

df[["sales", "expenses"]].plot(kind="box", title="Sales and Expenses boxplot")
plt.tight_layout()
plt.show()
