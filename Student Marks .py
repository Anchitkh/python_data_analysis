# Student Marks Analysis (with seaborn & correlation)
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load CSV
data = pd.read_csv("Student,Class,Maths,Science,English.csv")

print("Preview:")
print(data.head())

# Step 2: Class-wise average marks using groupby
class_avg = data.groupby("Class")[["Maths", "Science", "English"]].mean()
print("\nClass Wise Average Marks:")
print(class_avg)

# Step 3: Correlation Heatmap (NEW )
plt.figure(figsize=(7, 5))
sns.heatmap(data[["Maths", "Science", "English"]].corr(), annot=True, cmap="coolwarm")
plt.title("Subject Correlation Heatmap")
plt.show()

# Step 4: Best subject performance chart (NEW: seaborn barplot)
plt.figure(figsize=(8, 5))
sns.barplot(data=data, x="Student", y="Maths")
plt.title("Maths Marks Comparison")
plt.xticks(rotation=45)
plt.show()

# Step 5: Find Toppers
topper_math = data.loc[data["Maths"].idxmax()]
topper_science = data.loc[data["Science"].idxmax()]
topper_english = data.loc[data["English"].idxmax()]

print("\nTop Performers:")
print(f"Maths Topper: {topper_math['Student']} - {topper_math['Maths']}")
print(f"Science Topper: {topper_science['Student']} - {topper_science['Science']}")
print(f"English Topper: {topper_english['Student']} - {topper_english['English']}")
