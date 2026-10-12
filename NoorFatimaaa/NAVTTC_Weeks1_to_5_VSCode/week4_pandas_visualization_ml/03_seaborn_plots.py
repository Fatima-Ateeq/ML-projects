# Week 4 — Seaborn distribution, categorical, and heatmap plots
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "study_hours": [1, 2, 3, 4, 5, 2, 4, 6, 7, 3],
    "marks": [45, 50, 58, 65, 75, 52, 68, 82, 88, 60],
    "class": ["A", "A", "B", "B", "A", "B", "A", "B", "A", "B"]
})

sns.histplot(data=df, x="marks", kde=True)
plt.title("Marks distribution")
plt.tight_layout()
plt.show()

sns.boxplot(data=df, x="class", y="marks")
plt.title("Marks by class")
plt.tight_layout()
plt.show()

sns.scatterplot(data=df, x="study_hours", y="marks", hue="class")
plt.title("Study hours vs marks")
plt.tight_layout()
plt.show()

sns.heatmap(df[["study_hours", "marks"]].corr(), annot=True, vmin=-1, vmax=1)
plt.title("Correlation heatmap")
plt.tight_layout()
plt.show()
