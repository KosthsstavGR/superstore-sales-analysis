# superstore-sales-analysis
End-to-end Data Analysis project using Python, SQL, Excel and Power BI

# Data Loading

The dataset was loaded using Pandas.
During the import process, it was necessary to specify the correct column separator.

Some CSV files use semicolon (;) instead of comma (,) as a delimiter.
Without specifying the separator, Pandas would interpret the entire row as a single column.

df = pd.read_csv("data/raw/superstore.csv", sep=";")

This ensures that the dataset is properly structured into columns.
