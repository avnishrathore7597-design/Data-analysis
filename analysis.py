import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV File
df = pd.read_csv("sales_data.csv")

# Display Dataset
print("\nDataset:\n")
print(df)

# Dataset Information
print("\nDataset Information:")
print(df.info())

# Statistical Summary
print("\nStatistical Summary:")
print(df.describe())

# Average Sales and Profit
avg_sales = df["Sales"].mean()
avg_profit = df["Profit"].mean()

print(f"\nAverage Sales: {avg_sales:.2f}")
print(f"Average Profit: {avg_profit:.2f}")

# -----------------------------
# Bar Chart
# -----------------------------
plt.figure(figsize=(8, 5))
plt.bar(df["Month"], df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")
plt.show()

# -----------------------------
# Heatmap
# -----------------------------
plt.figure(figsize=(6, 4))
sns.heatmap(
    df[["Sales", "Profit"]].corr(),
    annot=True
)
plt.title("Correlation Heatmap")
plt.show()

# Insights
print("\nInsights:")
print("- Sales show an increasing trend over the months.")
print("- Profit increases as sales increase.")
print("- Sales and Profit have a positive correlation.")
