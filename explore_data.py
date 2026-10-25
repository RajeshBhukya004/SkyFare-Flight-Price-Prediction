
import pandas as pd

# Load the dataset
df = pd.read_csv("data/flight_price.csv")

# 1. Display dataset size
print("Dataset size:")
print(df.shape)

# 2. Display column names
print("\nColumn names:")
print(df.columns.tolist())

# 3. Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# 4. Check duplicate rows
print("\nNumber of duplicate rows:")
print(df.duplicated().sum())

# 5. Show basic statistics
print("\nNumerical statistics:")
print(df.describe())

# 6. Show the first five records
print("\nFirst five flight records:")
print(df.head())
