import pandas as pd

# Absolute path για να μην έχουμε errors
file_path = r"C:\Users\kosth\Desktop\superstore-sales-analysis\data\raw\superstore.csv"

# Load dataset
df = pd.read_csv(file_path,encoding="latin1",sep=";")

print("Original dataset shape:", df.shape)

# 1️⃣ Remove duplicates
df = df.drop_duplicates()

# 2️⃣ Check missing values
print("\nMissing values per column:")
print(df.isnull().sum())

# 3️⃣ Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# 4️⃣ Create new feature (Delivery time)
df['Delivery Days'] = (df['Ship Date'] - df['Order Date']).dt.days

# 5️⃣ Save cleaned dataset
clean_path = r"C:\Users\kosth\Desktop\superstore-sales-analysis\data\cleaned\superstore_cleaned.csv"
df.to_csv(clean_path, index=False)

print("\nCleaned dataset shape:", df.shape)
print("Cleaned data saved successfully!")