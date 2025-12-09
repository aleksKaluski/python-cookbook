
"""
Dictionaries — useful operations
"""


# -------------------------------------------------------
# Creating dictionaries
# -------------------------------------------------------
d = {"a": 1, "b": 2}
d = dict(a=1, b=2)
d = dict([("a", 1), ("b", 2)])
d = {}                           # empty dict

# -------------------------------------------------------
# Accessing values
# -------------------------------------------------------
d["a"]                           # direct access (KeyError if missing)
d.get("a")                       # safe access (None if missing)
d.get("a", 0)                    # default value if missing

# -------------------------------------------------------
# Adding / Updating values
# -------------------------------------------------------
d["c"] = 3
d.update({"d": 4})

# -------------------------------------------------------
# Removing entries
# -------------------------------------------------------
d.pop("a")                       # returns value + removes key
d.pop("a", None)                 # safe pop (no KeyError)
d.popitem()                      # remove last inserted (LIFO)
del d["b"]                       # delete key
d.clear()                        # remove everything

# -------------------------------------------------------
# Checking membership
# -------------------------------------------------------
"a" in d                         # checks *keys*
1 in d.values()                  # check in values

# -------------------------------------------------------
# Looping
# -------------------------------------------------------
for k in d:                      # keys
    print(k)

for v in d.values():             # values
    print(v)

for k, v in d.items():           # key + value
    print(k, v)

# -------------------------------------------------------
# Dictionary comprehensions
# -------------------------------------------------------
squares = {x: x*x for x in range(5)}
even_values = {k: v for k, v in d.items() if v % 2 == 0}

# -------------------------------------------------------
# Merging dictionaries
# -------------------------------------------------------
new = d1 | d2                    # Python 3.9+
d1.update(d2)                    # older versions

# -------------------------------------------------------
# Useful methods
# -------------------------------------------------------
d.keys()
d.values()
d.items()
d.copy()

d.setdefault("x", 0)             # set default if key missing

# -------------------------------------------------------
# Nested dictionaries
# -------------------------------------------------------
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob":   {"age": 21, "grade": "B"},
}

students["Alice"]["grade"]
