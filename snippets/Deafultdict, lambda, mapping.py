

"""
defaultdict, Counter, map(), zip(), lambda, enumerate()
"""


# =====================================================================
# defaultdict — from collections
# Automatically creates a default value for missing keys
# =====================================================================
from collections import defaultdict

# Creates a dict where missing keys start with an empty list
d = defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["b"].append(3)

# defaultdict(int) → starts all values at 0 (useful for counting)
counts = defaultdict(int)
for char in "banana":
    counts[char] += 1
# {'b':1, 'a':3, 'n':2}

# defaultdict(set) → auto-creates a set (unique values)
groups = defaultdict(set)
groups["fruits"].add("apple")
groups["fruits"].add("banana")

# Good for: grouping, counting, building nested structures
# Example nested defaultdict:
tree = defaultdict(lambda: defaultdict(int))
tree["A"]["B"] = 10


# =====================================================================
# Counter — frequency counting of hashable items
# =====================================================================
from collections import Counter

c = Counter("banana")
# {'a': 3, 'n': 2, 'b': 1}

# most_common()
c.most_common(1)          # [('a', 3)]
c.most_common()           # all sorted by frequency

# update counts
c.update("aa")            # increases 'a' by 2

# subtract
c.subtract("n")           # decreases 'n' by 1

# convert back to list, dict
list(c.elements())
dict(c)


# =====================================================================
# map() — apply a function to each element of an iterable
# =====================================================================

nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))   # [2, 4, 6]

# map with built-in function
result = list(map(str, nums))               # converts to strings


# =====================================================================
# zip() — combine multiple iterables into pairs
# =====================================================================

a = [1, 2, 3]
b = ["a", "b", "c"]

pairs = list(zip(a, b))                     # [(1,'a'), (2,'b'), (3,'c')]

# unzip:
nums, letters = zip(*pairs)

# zip stops at the shortest iterable
zip([1,2,3], [10,20])                       # → (1,10), (2,20)


# =====================================================================
# lambda functions — anonymous inline functions
# =====================================================================

# Basic lambda
f = lambda x: x + 10
f(5)                                        # 15

# lambda in map()
list(map(lambda x: x**2, [1, 2, 3]))
# [1, 4, 9]

# =====================================================================
# Sorting with lambda
# =====================================================================

# Sort list of tuples by the second element
pairs = [(1, "b"), (3, "a"), (2, "c")]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

# Sort dict by value
d = {"a": 3, "b": 1, "c": 2}
sorted_by_value = sorted(d.items(), key=lambda x: x[1])

# Sort nested structures
students = [
    {"name": "Alice", "age": 22},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 23},
]

sorted_students = sorted(students, key=lambda s: s["age"])


# =====================================================================
# lambda as key function
# =====================================================================

# max/min with key=...
words = ["apple", "banana", "kiwi"]
max_len = max(words, key=lambda w: len(w))  # "banana"

# custom comparison
min_abs = min([-5, -2, 3], key=lambda x: abs(x))  #  -2


# =====================================================================
# enumerate() — get index + value when iterating
# =====================================================================

fruits = ["apple", "banana", "cherry"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
# 0 apple
# 1 banana
# 2 cherry

# Start index from 1
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)


# =====================================================================
# Combined example: enumerate + zip + lambda
# =====================================================================

# Pair each fruit with an index, sorted by string length
fruits = ["kiwi", "watermelon", "lime", "banana"]

indexed_sorted = sorted(
    list(enumerate(fruits)),
    key=lambda x: len(x[1])
)

# Result:
# [(0, 'kiwi'), (2, 'lime'), (3, 'banana'), (1, 'watermelon')]
