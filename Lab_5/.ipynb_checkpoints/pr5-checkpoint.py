import pandas as pd

# 1. Create a simple dataset and convert it into a DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [24, 27, 22, 32, 29],
    'Salary': [50000, 60000, 45000, 80000, 70000]
}
df = pd.DataFrame(data)

print("--- Original DataFrame ---")
print(df)

# 2. head(): View the first 2 rows
print("\n--- head(2): First 2 rows ---")
print(df.head(2))

# 3. tail(): View the last 2 rows
print("\n--- tail(2): Last 2 rows ---")
print(df.tail(2))

# 4. describe(): Get statistical summary of numeric columns
print("\n--- describe(): Summary Statistics ---")
print(df.describe())

# 5. max(): Find the maximum values
print("\n--- max(): Maximum values ---")
print(df.max())

# 6. min(): Find the minimum values
print("\n--- min(): Minimum values ---")
print(df.min())

# 7. sort_values(): Sort the DataFrame by Salary in descending order
print("\n--- sort_values(): Sorted by Salary (Highest to Lowest) ---")
print(df.sort_values(by='Salary', ascending=False))