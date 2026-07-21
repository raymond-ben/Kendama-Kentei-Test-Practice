import pandas as pd

df = pd.read_excel("data/tricks.xlsx")

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 10 rows:")
print(df.head(10))

print("\nNumber of rows:")
print(len(df))