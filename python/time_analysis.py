import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
file_path = "data/cleaned/superstore_cleaned.csv"
df = pd.read_csv(file_path)

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Year-Month column
df["YearMonth"] = df["Order Date"].dt.to_period("M")

# Sales by Month
monthly_sales = df.groupby("YearMonth")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Plot chart
plt.figure(figsize=(12,6))
monthly_sales.plot()

plt.title("Sales Over Time")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("charts/sales_over_time.png")

plt.show()