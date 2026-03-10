import pandas as pd
import matplotlib.pyplot as plt
import os

# Load cleaned dataset
file_path = "data/cleaned/superstore_cleaned.csv"
df = pd.read_csv(file_path)

# Create charts folder if it doesn't exist
os.makedirs("charts", exist_ok=True)

# -------------------------
# Sales by Category
# -------------------------
sales_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sales_category.plot(kind='bar', color='skyblue')
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/sales_by_category.png")
plt.close()

# -------------------------
# Profit by Category
# -------------------------
profit_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
profit_category.plot(kind='bar', color='lightgreen')
plt.title("Total Profit by Category")
plt.ylabel("Profit")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/profit_by_category.png")
plt.close()

# -------------------------
# Top 10 States by Sales
# -------------------------
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
top_states.plot(kind='bar', color='coral')
plt.title("Top 10 States by Sales")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/top_states.png")
plt.close()

# -------------------------
# Sales by Customer Segment
# -------------------------
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(6,4))
segment_sales.plot(kind='bar', color='violet')
plt.title("Sales by Customer Segment")
plt.ylabel("Sales")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("charts/segment_sales.png")
plt.close()

print("All charts saved in 'charts/' folder successfully!")