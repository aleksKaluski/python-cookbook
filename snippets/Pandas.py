"""
PANDAS — Data analysis with DataFrame and Series (extended)
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

# From CSV / JSON / Excel
df = pd.read_csv("data.csv")
df = pd.read_json("data.json")
df = pd.read_excel("data.xlsx")


# =====================================================================
# Inspecting data
# =====================================================================

df.head()          # first rows
df.tail()          # last rows
df.sample(3)       # random rows
df.info()          # structure + dtypes
df.describe()      # statistics (numeric)
df.columns         # column names
df.dtypes          # data types
df.shape           # (rows, columns)


# =====================================================================
# Selecting data
# =====================================================================

df["age"]                  # single column (Series)
df[["name","age"]]         # multiple columns

df.iloc[0]                 # row by position
df.iloc[0:3]

df.loc[0]                  # row by label
df.loc[df["age"] > 20]


# =====================================================================
# Filtering rows
# =====================================================================

df[df["age"] >= 21]
df[(df["age"] >= 21) & (df["grade"] == "A")]

df.query("age >= 21 and grade == 'A'")

df[df["name"].str.startswith("A")]
df[df["age"].between(20, 22)]
df[df["grade"].isin(["A", "B"])]


# =====================================================================
# Adding / modifying columns
# =====================================================================

df["passed"] = df["grade"] == "A"
df["age_plus_one"] = df["age"] + 1

df.assign(age_double=df["age"] * 2)


# =====================================================================
# Deleting rows and columns
# =====================================================================

df.drop(columns=["grade"])           # remove column
df.drop(index=[0, 1])                # remove rows by index
df.drop(df[df["age"] < 21].index)    # conditional row deletion

df.pop("passed")                     # remove column and return it
del df["age_plus_one"]               # delete column (in-place)


# =====================================================================
# Sorting
# =====================================================================

df.sort_values("age")
df.sort_values("age", ascending=False)
df.sort_values(["grade","age"])

df.sort_index()                      # sort by index


# =====================================================================
# Grouping data
# =====================================================================

df.groupby("grade").mean(numeric_only=True)
df.groupby("grade")["age"].mean()

# Multiple aggregations
df.groupby("grade").agg({
    "age": ["mean", "min", "max"]
})

df.groupby("grade").size()           # group counts


# =====================================================================
# Applying functions
# =====================================================================

df["age_squared"] = df["age"].apply(lambda x: x*x)

df.apply(lambda row: row["age"] + 1, axis=1)

df["name_len"] = df["name"].map(len)
df["grade"] = df["grade"].replace({"A": 5, "B": 4})


# =====================================================================
# String operations (vectorized)
# =====================================================================

df["name"].str.lower()
df["name"].str.upper()
df["name"].str.contains("a", case=False)
df["name"].str.replace("a", "@", regex=True)
df["name"].str.split().str[0]


# =====================================================================
# Handling missing data
# =====================================================================

df.isna()
df.notna()

df.dropna()
df.dropna(subset=["age"])

df.fillna(0)
df.fillna({"age": df["age"].mean()})
df.fillna(method="ffill")     # forward fill
df.fillna(method="bfill")     # backward fill


# =====================================================================
# Data type conversion
# =====================================================================

df["age"] = df["age"].astype(int)
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["date"] = pd.to_datetime(df["date"], errors="coerce")


# =====================================================================
# Index operations
# =====================================================================

df.set_index("name")
df.reset_index()

df.rename(columns={"age": "Age"})
df.rename(index={0: "row_0"})


# =====================================================================
# Merging, joining & concatenation
# =====================================================================

pd.concat([df1, df2])              # vertical concat
pd.concat([df1, df2], axis=1)      # horizontal concat

pd.merge(df1, df2, on="id")
pd.merge(df1, df2, how="left", on="id")

df1.join(df2, on="id")


# =====================================================================
# Reading & writing files (advanced)
# =====================================================================

pd.read_csv("data.csv", sep=";", encoding="utf-8")
pd.read_csv("data.csv", usecols=["name","age"])
pd.read_csv("data.csv", chunksize=1000)   # large files

df.to_csv("out.csv", index=False)
df.to_json("out.json")
df.to_excel("out.xlsx", index=False)


# =====================================================================
# Dealing with files (with os / pathlib)
# =====================================================================

from pathlib import Path

p = Path("out.csv")
p.exists()           # check if file exists
p.unlink()           # delete file safely


# =====================================================================
# Basic plotting (uses matplotlib)
# =====================================================================

df["age"].plot()
df.plot(kind="bar", x="name", y="age")
df.plot(kind="hist", y="age")


# =====================================================================
# Performance & best practices (exam notes)
# =====================================================================

# - Prefer vectorized operations over loops
# - Use .loc for assignment to avoid SettingWithCopyWarning
# - Use categorical dtype for repeated string values
# - Read only needed columns for large files


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
# - file I/O and data cleaning
