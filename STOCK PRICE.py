# Stock Price Trend Analysis Project
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load CSV file
data = pd.read_csv("Date,Open,High,Low,Close,Volume.csv")

# Step 2: Show dataset preview
print("Stock Data Preview:")
print(data.head())

# Step 3: Summary statistics
print("\nSummary Statistics:")
print(data.describe())

# Step 4: Missing values
print("\nMissing Values:")
print(data.isnull().sum())

# Step 5: Plot Closing Price Trend
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Close"], marker='o')
plt.title("Stock Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 6: Plot Open vs Close comparison
plt.figure(figsize=(10, 5))
plt.plot(data["Date"], data["Open"], marker='o', label="Open Price")
plt.plot(data["Date"], data["Close"], marker='o', label="Close Price")
plt.title("Open vs Close Price Trend")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)
plt.show()

# Step 7: Highest Close & Highest Volume Day
max_close = data.loc[data["Close"].idxmax()]
max_volume = data.loc[data["Volume"].idxmax()]

print(f"\nHighest Closing Price: {max_close['Date']} ({max_close['Close']})")
print(f"Highest Trading Volume: {max_volume['Date']} ({max_volume['Volume']})")
