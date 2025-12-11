# ===========================================================
# Reading and writing CSV
# ===========================================================

import csv

# Reading CSV
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Reading into dictionaries (header → keys)
with open("data.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["age"])

# Writing CSV
data = [
    ["name", "age"],
    ["Alice", 20],
    ["Bob", 30],
]

with open("out.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Writing dicts
rows = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 30},
]

with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name","age"])
    writer.writeheader()
    writer.writerows(rows)

# ===========================================================
# Reading / Writing TXT
# ===========================================================

# Reading TXT file (entire content as a single string)
with open("document.txt", "r", encoding="utf-8") as f:
    text_content = f.read()

# Reading TXT file (content as a list of lines)
with open("document.txt", "r", encoding="utf-8") as f:
    lines_list = f.readlines()
    # Optional: Strip newline characters from each line
    # lines_list = [line.strip() for line in lines_list]

# if you fail to open a file with "r" mode FileNotFoundError is raised!


# Writing TXT file (overwrites the file)
output_content = "This is the first line.\n" + "This is the second line."
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(output_content)

# Appending to a TXT file (adds to the end)
append_content = "\nThis line is appended."
with open("output.txt", "a", encoding="utf-8") as f:
    f.write(append_content)

# ===========================================================
# Reading / Writing JSON
# ===========================================================

import json

# Reading JSON file
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Writing JSON (pretty)
with open("out.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# Converting Python <-> JSON strings
json_str = json.dumps(data)       # Python → JSON string
py_obj = json.loads(json_str)     # JSON string → Python object




