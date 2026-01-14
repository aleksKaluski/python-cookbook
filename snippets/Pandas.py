"""
PANDAS — Data analysis with DataFrame and Series
"""

# =====================================================================
# Importing pandas
# =====================================================================

import pandas as pd


# =====================================================================
# Creating Series
# =====================================================================

s = pd.Series([10, 20, 30])
s = pd.Series([10, 20, 30], index=["a", "b", "c"])

s.values          # underlying numpy array
s.index           # index labels


# =====================================================================
# Creating DataFrame
# =====================================================================

# From dictionary
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Charlie"],
    "age": [20, 21, 22],
    "grade": ["A", "B", "A"]
})

# From list of dicts
df = pd.DataFrame([
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 21}
])

# From CSV
df = pd.read_csv("data.csv")


# =====================================================================
# Inspecting data
# =====================================================================

df.head()          # first rows
df.tail()          # last rows
df.info()          # structure + dtypes
df.describe()      # statistics (numeric)
df.columns         # column names
df.shape           # (rows, columns)


# =====================================================================
# Selecting data
# =====================================================================

df["age"]          # single column (Series)
df[["name","age"]] # multiple columns

df.iloc[0]         # row by index (position)
df.iloc[0:3]

df.loc[0]          # row by label
df.loc[df["age"] > 20]


# =====================================================================
# Filtering rows
# =====================================================================

df[df["age"] >= 21]
df[(df["age"] >= 21) & (df["grade"] == "A")]

df.query("age >= 21 and grade == 'A'")


# =====================================================================
# Adding / modifying columns
# =====================================================================

df["passed"] = df["grade"] == "A"

df["age_plus_one"] = df["age"] + 1


# =====================================================================
# Sorting
# =====================================================================

df.sort_values("age")
df.sort_values("age", ascending=False)
df.sort_values(["grade","age"])


# =====================================================================
# Grouping data
# =====================================================================

df.groupby("grade").mean(numeric_only=True)
df.groupby("grade")["age"].mean()

# Multiple aggregations
df.groupby("grade").agg({
    "age": ["mean", "min", "max"]
})


# =====================================================================
# Applying functions
# =====================================================================

# apply to column
df["age_squared"] = df["age"].apply(lambda x: x*x)

# apply to rows
df.apply(lambda row: row["age"] + 1, axis=1)


# =====================================================================
# Handling missing data
# =====================================================================

df.isna()
df.dropna()
df.fillna(0)
df.fillna(method="ffill")     # forward fill


# =====================================================================
# Reading & writing files
# =====================================================================

pd.read_csv("data.csv")
pd.read_json("data.json")

df.to_csv("out.csv", index=False)
df.to_json("out.json")


# =====================================================================
# Merging & concatenation
# =====================================================================

pd.concat([df1, df2])          # vertical concat
pd.concat([df1, df2], axis=1)  # horizontal

pd.merge(df1, df2, on="id")
pd.merge(df1, df2, how="left", on="id")


# =====================================================================
# Basic plotting (uses matplotlib)
# =====================================================================

df["age"].plot()
df.plot(kind="bar", x="name", y="age")
df.plot(kind="hist", y="age")


# =====================================================================
# Pandas vs NumPy (exam note)
# =====================================================================

# NumPy:
# - fast numerical arrays
# - no labels

# Pandas:
# - labeled data (rows + columns)
# - missing values handling
# - grouping, filtering, statistics
