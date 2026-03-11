import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
file_path = "data/cleaned/superstore_cleaned.csv"
df = pd.read_csv(file_path)

# -------------------------
# Sales vs Profit scatter plot
# -------------------------

plt.figure(figsize=(10,6))

plt.scatter(df["Sales"], df["Profit"], alpha=0.5)

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("charts/sales_vs_profit.png")

plt.show()

print("Sales vs Profit chart created.")