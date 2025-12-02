# Sales Data Cleaning & Outlier Detection
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load CSV
data = pd.read_csv("Day,Sales.csv")

print("Original Data:")
print(data)

# Step 2: Check missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 3: Fill missing values (NEW )
data["Sales"] = data["Sales"].fillna(data["Sales"].mean())
print("\nAfter Filling Missing Values:")
print(data)

# Step 4: Outlier Detection using IQR (NEW )
Q1 = data["Sales"].quantile(0.25)
Q3 = data["Sales"].quantile(0.75)
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nIQR Range:", lower_limit, "to", upper_limit)

# Step 5: Filter outliers
outliers = data[(data["Sales"] < lower_limit) | (data["Sales"] > upper_limit)]
print("\nDetected Outliers:")
print(outliers)

# Step 6: Boxplot to visualize outliers (NEW)
plt.figure(figsize=(6,4))
sns.boxplot(data["Sales"])
plt.title("Sales Outlier Visualization")
plt.show()

# Step 7: Remove outliers (optional)
clean_data = data[(data["Sales"] >= lower_limit) & (data["Sales"] <= upper_limit)]
print("\nCleaned Data (Without Outliers):")
print(clean_data)
