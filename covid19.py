# COVID-19 Data Tracker Project
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV data
data = pd.read_csv("covid_data.csv")

# Step 2: Show dataset preview
print("📊 COVID Data Preview:")
print(data.head())

# Step 3: Summary statistics
print("\n📈 Data Summary:")
print(data.describe())

# Step 4: Check missing values
print("\n🔍 Missing Values:")
print(data.isnull().sum())

# Step 5: Plot new cases over time
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["New_Cases"], marker='o')
plt.title("Daily New COVID-19 Cases")
plt.xlabel("Date")
plt.ylabel("New Cases")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 6: Compare cases, recoveries & deaths
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["New_Cases"], marker='o', label="New Cases")
plt.plot(data["Date"], data["Recoveries"], marker='o', label="Recoveries")
plt.plot(data["Date"], data["Deaths"], marker='o', label="Deaths")
plt.title("COVID-19 Daily Trends")
plt.xlabel("Date")
plt.ylabel("Count")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 7: Find highest day stats
max_case_day = data.loc[data["New_Cases"].idxmax()]
max_recovery_day = data.loc[data["Recoveries"].idxmax()]
max_death_day = data.loc[data["Deaths"].idxmax()]

print(f"\n🔥 Highest Cases Day: {max_case_day['Date']} ({max_case_day['New_Cases']} cases)")
print(f"💚 Highest Recovery Day: {max_recovery_day['Date']} ({max_recovery_day['Recoveries']} recoveries)")
print(f"⚰️ Highest Death Day: {max_death_day['Date']} ({max_death_day['Deaths']} deaths)")
