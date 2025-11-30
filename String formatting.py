"""
String formatting
"""


# old-style
name = "Alice"
age = 25
print("Name: %s, Age: %d" % (name, age))

# str.format() method
"Hello {}, you are {}".format(name, age)

# with positions
"Hello {0}, you are {1}".format(name, age)

"Hello {n}, you are {a}".format(n=name, a=age)

# numbers
"Pi: {:.2f}".format(3.14159)

