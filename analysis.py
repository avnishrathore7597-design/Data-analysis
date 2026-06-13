import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Average of selected column
avg_sepal_length = df["sepal_length"].mean()
print("\nAverage Sepal Length:", avg_sepal_length)

# Basic statistics
print("\nDataset Statistics:")
print(df.describe())

# Bar Chart
species_count = df["species"].value_counts()

plt.figure(figsize=(6,4))
species_count.plot(kind="bar")
plt.title("Species Count")
plt.xlabel("Species")
plt.ylabel("Count")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,4))
plt.scatter(df["sepal_length"], df["petal_length"])
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.show()

# Heatmap
correlation = df.select_dtypes(include='number').corr()

plt.figure(figsize=(6,4))
plt.imshow(correlation, cmap="coolwarm")
plt.colorbar()

plt.xticks(range(len(correlation.columns)),
           correlation.columns,
           rotation=45)

plt.yticks(range(len(correlation.columns)),
           correlation.columns)

plt.title("Correlation Heatmap")
plt.show()