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
# Searches for the pattern anywhere in the string.
# Returns the first Match object found (or None if no match).
re.search(r"\d+", text)    # first number match

# Find all occurrences
# Returns a list of strings containing all matches.
re.findall(r"\d+", text)   # → ["123","456","789"]

# Checks if the entire string matches the pattern
# Returns a Match object if the whole string matches (or None).
re.fullmatch(r"\d+", text, flags=0)

# Matching pattern at start
re.match(r"My", text)

# Substitutes all matches of the pattern
# with the replacement string (repl).
# Returns the string after substitution.
re.sub(r"\d", "X", text)

# Groups
m = re.search(r"(\d{3})-(\d{3})-(\d{3})", text)
m.group(1)     # "123"
m.group(2)     # "456"

# Splits the string by the matches of the pattern.
# Returns a list of strings resulting from the split.
re.split(r"[- ]", text)

# Precompiled pattern (faster)
pattern = re.compile(r"\d{3}")
pattern.findall(text)


# Regular Expression Quantifiers:
#
# Quantifier | Meaning                   | Example
# -------------------------------------------------------------------
# *          | 0 or more occurrences     | a*b matches b, ab, aab
# +          | 1 or more occurrences     | a+b matches ab, aab (but not b)
# ?          | 0 or 1 occurrence         | a?b matches b or ab
# {n}        | Exactly n occurrences     | a{3}b matches aaab
# {n,m}      | Between n & m occurrences | a{2,4}b matches aab, aaab, aaaab
# {n,}       | Minimum n occurrences     | a{2,}b matches aab, aaab, and so on
# {,m}       | Up to m occurrences       | a{,3}b matches b, ab, aab, aaab
#
# Note: Append '?' to make a quantifier lazy (e.g., *? or +?).