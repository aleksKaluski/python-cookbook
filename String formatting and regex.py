# ===========================================================
# Basic string methods
# ===========================================================

s = "  Hello, World!  "

# Stripping whitespace
s.strip()       # "Hello, World!"
s.lstrip()      # strip left side
s.rstrip()      # strip right side

# Changing case
s.lower()
s.upper()
s.title()
s.capitalize()

# Splitting / joining
"one,two,three".split(",")       # → ["one","two","three"]
" ".join(["Python","is","fun"])  # → "Python is fun"

# Finding / replacing
s.find("World")     # returns index or -1
s.replace("World", "Python")

# Starts/ends checking
s.startswith("He")
s.endswith("!")

# Reversing string
s[::-1]

# Removing characters
"abc123".strip("abc")   # removes these chars from both ends

# String formatting
name = "Alice"
age = 21

# old %
"%s is %d years old" % (name, age)

# str.format()
"{} is {} years old".format(name, age)
"{name} is {age}".format(name=name, age=age)

# f-strings (best)
f"{name} is {age} years old"
f"{3.14159:.2f}"       # formatting numbers

# ===========================================================
# Regular expressions (regex)
# ===========================================================

import re

text = "My phone is 123-456-789"

# Basic search
re.search(r"\d+", text)    # first number match

# Find all occurrences
re.findall(r"\d+", text)   # → ["123","456","789"]

# Matching pattern at start
re.match(r"My", text)

# Replace
re.sub(r"\d", "X", text)

# Groups
m = re.search(r"(\d{3})-(\d{3})-(\d{3})", text)
m.group(1)     # "123"
m.group(2)     # "456"

# Splitting on pattern
re.split(r"[- ]", text)

# Precompiled pattern (faster)
pattern = re.compile(r"\d{3}")
pattern.findall(text)
