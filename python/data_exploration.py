import pandas as pd

# Φόρτωση raw data
file_path = "../data/raw/superstore.csv"
df = pd.read_csv(file_path)

# Αφαίρεση διπλοτύπων
df = df.drop_duplicates()

print("Duplicates removed. Shape now:", df.shape)