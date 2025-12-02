# Weather Data Analysis Project
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the CSV file
data = pd.read_csv("Date,Temperature,Humidity,Rainfall.csv")

# Step 2: Show the first few rows
print(" Weather Dataset Preview:")
print(data.head())

# Step 3: Get basic statistics
print("\n Summary Statistics:")
print(data.describe())

# Step 4: Check for missing values
print("\n Missing Values:")
print(data.isnull().sum())

# Step 5: Plot temperature trend
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Temperature"], marker='o')
plt.title("Temperature Trend Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 6: Plot humidity and rainfall comparison
plt.figure(figsize=(10, 5))
plt.bar(data["Date"], data["Humidity"], color='skyblue', label='Humidity')
plt.plot(data["Date"], data["Rainfall"], color='red', marker='o', label='Rainfall (mm)')
plt.title("Humidity and Rainfall Comparison")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 7: Find hottest and rainiest days
max_temp_day = data.loc[data["Temperature"].idxmax()]
max_rain_day = data.loc[data["Rainfall"].idxmax()]

print(f"\n Hottest Day: {max_temp_day['Date']} ({max_temp_day['Temperature']}°C)")
print(f" Rainiest Day: {max_rain_day['Date']} ({max_rain_day['Rainfall']} mm)")
