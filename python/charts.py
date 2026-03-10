import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path = "data/cleaned/superstore_cleaned.csv"
df = pd.read_csv(file_path)

# -------------------------
# Sales by Category
# -------------------------
sales_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=sales_category.index, y=sales_category.values, palette="viridis")
plt.title("Total Sales by Category")
plt.ylabel("Sales")
plt.xlabel("Category")
plt.savefig("charts/sales_by_category.png")
plt.close()

# -------------------------
# Profit by Category
# -------------------------
profit_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=profit_category.index, y=profit_category.values, palette="magma")
plt.title("Total Profit by Category")
plt.ylabel("Profit")
plt.xlabel("Category")
plt.savefig("charts/profit_by_category.png")
plt.close()

# -------------------------
# Top 10 States by Sales
# -------------------------
top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x=top_states.values, y=top_states.index, palette="coolwarm")
plt.title("Top 10 States by Sales")
plt.xlabel("Sales")
plt.ylabel("State")
plt.savefig("charts/top_10_states.png")
plt.close()

# -------------------------
# Sales by Customer Segment
# -------------------------
segment_sales = df.groupby("Segment")["Sales"].sum().sort_values(ascending=False)
plt.figure(figsize=(8,5))
sns.barplot(x=segment_sales.index, y=segment_sales.values, palette="plasma")
plt.title("Sales by Customer Segment")
plt.ylabel("Sales")
plt.xlabel("Segment")
plt.savefig("charts/sales_by_segment.png")
plt.close()