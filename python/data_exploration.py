import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Load cleaned dataset ---
file_path = "data/cleaned/superstore_cleaned.csv"
df = pd.read_csv(file_path)

# --- Basic Info ---
print("Dataset shape:", df.shape)
print("\nMissing values per column:")
print(df.isnull().sum())

print("\nSummary statistics:")
print(df.describe())

print("\nData types:")
print(df.dtypes)

# --- Sales & Profit Distribution ---
plt.figure(figsize=(12,5))
sns.histplot(df['Sales'], bins=50, kde=True)
plt.title('Distribution of Sales')
plt.xlabel('Sales')
plt.ylabel('Count')
plt.show()

plt.figure(figsize=(12,5))
sns.histplot(df['Profit'], bins=50, kde=True, color='green')
plt.title('Distribution of Profit')
plt.xlabel('Profit')
plt.ylabel('Count')
plt.show()

# --- Sales and Profit by Category ---
plt.figure(figsize=(10,5))
sns.barplot(data=df.groupby('Category')['Sales'].sum().reset_index(), x='Category', y='Sales', palette='pastel')
plt.title('Total Sales by Category')
plt.show()

plt.figure(figsize=(10,5))
sns.barplot(data=df.groupby('Category')['Profit'].sum().reset_index(), x='Category', y='Profit', palette='muted')
plt.title('Total Profit by Category')
plt.show()

# --- Top 10 Products by Sales ---
top_products = df.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12,6))
sns.barplot(x=top_products.values, y=top_products.index, palette='bright')
plt.title('Top 10 Products by Sales')
plt.xlabel('Sales')
plt.ylabel('Product Name')
plt.show()

# --- Delivery Days Analysis ---
plt.figure(figsize=(10,5))
sns.countplot(x='Delivery Days', data=df, palette='cool')
plt.title('Distribution of Delivery Days')
plt.show()