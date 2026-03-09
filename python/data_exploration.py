import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Φόρτωση καθαρισμένου dataset
file_path  = r"data\cleaned\superstore_cleaned.csv"
df = pd.read_csv(file_path)

# Ρίξε μια πρώτη ματιά
print(df.head())
print(df.describe())
print(df.info())