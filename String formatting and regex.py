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

# -----------------------------------------------------------
# Regular Expression Quantifiers:
#
# REGULAR EXPRESSION REFERENCE: Quantifiers, Classes, and Sets
#
# Pattern    | Type       | Meaning                                    | Example
# ------------------------------------------------------------------------------------------------
# **Quantifiers**
# *          | Quantifier | 0 or more occurrences                      | r'a*b' matches 'b', 'ab', 'aab'
# +          | Quantifier | 1 or more occurrences                      | r'a+b' matches 'ab', 'aab' (but not 'b')
# ?          | Quantifier | 0 or 1 occurrence (optional)               | r'a?b' matches 'b' or 'ab'
# {n}        | Quantifier | Exactly n occurrences                      | r'a{3}b' matches 'aaab'
# {n,m}      | Quantifier | Between n & m occurrences (inclusive)      | r'a{2,4}b' matches 'aab' to 'aaaab'
# {n,}       | Quantifier | Minimum n occurrences                      | r'a{2,}b' matches 'aab', 'aaab', and so on
# {,m}       | Quantifier | Up to m occurrences                        | r'a{,3}b' matches 'b' up to 'aaab'
#
# **Predefined Character Classes**
# \d         | Class      | Matches any single digit (0-9)                      | r'\d+' matches '100', '5'
# \D         | Class      | Matches any single non-digit                        | r'\D' matches 'a', '!'
# \w         | Class      | Matches any single alphanumeric (A-z, 0-9, _)       | r'\w+' matches 'word', 'id_123'
# \W         | Class      | Matches any single non-alphanumeric character       | r'\W' matches '$', '#'
# \s         | Class      | Matches any single whitespace (space, tab, newline) | r'\s+' matches a sequence of spaces
# \S         | Class      | Matches any single non-whitespace character         | r'\S+' matches 'word'
#
# **Character Sets (Brackets)**
# [abc]      | Set        | Matches any single character: 'a', 'b', or 'c'            | r'[aeiou]' matches a single vowel
# [a-z]      | Set Range  | Matches any single character in the range 'a' through 'z' | r'[A-Z]{3}' matches 'ABC'
# [0-9a-f]   | Set Range  | Matches any single digit or hex letter 'a' through 'f'    | r'[0-9a-f]+' matches a hex string
# [^abc]     | Negated Set| Matches any single character NOT in the set               | r'[^0-9]+' matches a sequence of non-digits
#
# Note: Append '?' to a quantifier to make it lazy (e.g., *? or +?).

# -----------------------------------------------------------
# Examples
re.findall(r"E\d{3}-\d{2}", text_data) # -> ['E404-01']

re.findall(r"([\w.-]+)@", text_data) # -> ['john.doe', 'alice_smith123', 'tech-support']
# it ommits @ since @ is outside of caputing group described by ()

re.findall(r"\$\d+\.\d{2}", text_data) # -> ['$12.99']
# if you want to find special chacarcters such as $ or. use \ or []




# -----------------------------------------------------------
# Greedy and Lazy Maching
# By default, regular expressions are greedy, meaning they try to match the longest possible string. To switch to lazy
# mode (matching the shortest possible string), you append an extra question mark (?)
# to the quantifier (e.g., *?, +?, ??, {n,m}?).