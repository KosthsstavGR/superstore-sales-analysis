import pandas as pd

# Load cleaned dataset
file_path = "data/cleaned/superstore_cleaned.csv"
df = pd.read_csv(file_path)

# -------------------------
# Sales by Category
# -------------------------
sales_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)

print("\nTotal Sales by Category:")
print(sales_category)

# -------------------------
# Profit by Category
# -------------------------
profit_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)

print("\nTotal Profit by Category:")
print(profit_category)

# -------------------------
# Top 10 States by Sales
# -------------------------
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

print("\nTop 10 States by Sales:")
print(top_states)

# -------------------------
# Sales by Customer Segment
# -------------------------
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)

print("\nSales by Customer Segment:")
print(segment_sales)