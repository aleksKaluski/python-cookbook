"""
ITERATORS & GENERATORS
"""

# =====================================================================
# ITERATOR PROTOCOL
# To be an iterator, an object MUST implement:
#   1) __iter__()  -> returns the iterator object itself
#   2) __next__()  -> returns next value, or raises StopIteration
# =====================================================================

class MyIterator:
    def __init__(self):
        self.value = 0              # starting state of the iterator

    def __iter__(self):
        return self                 # iterator returns itself

    def __next__(self):
        # This defines how iteration progresses
        if self.value < 5:
            self.value += 1         # update state
            return self.value       # produce next value
        raise StopIteration         # required to stop the loop


# Using the iterator:
it = MyIterator()
for x in it:
    print(x)

# Output:
# 1
# 2
# 3
# 4
# 5

# The FOR loop internally:
#   it_obj = iter(it)
#   while True:
#       try: item = next(it_obj)
#       except StopIteration: break


# =====================================================================
# CUSTOM ITERABLE (separate iterable + iterator)
#
# This is how Python's range() works internally:
# - MyRange is an iterable (has __iter__)
# - MyRangeIterator is the iterator (has __next__)
#
# Advantage:
# Each iteration creates a NEW iterator, so you can loop multiple times.
# =====================================================================

class MyRange:
    def __init__(self, stop):
        self.stop = stop

    def __iter__(self):
        # Every time iter() is called, return a NEW iterator object
        return MyRangeIterator(self.stop)


class MyRangeIterator:
    def __init__(self, stop):
        self.current = 0
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        # Produce values until reaching stop
        if self.current < self.stop:
            val = self.current
            self.current += 1
            return val
        raise StopIteration


# This works like built-in range():
for x in MyRange(5):
    print(x)

# Output:
# 0 1 2 3 4



# ================================================================
# Generators — functions that use yield
# ================================================================
def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Lazy evaluation, memory efficient


# ================================================================
# Generator expressions
# ================================================================
gen = (x*x for x in range(5))   # similar to list comprehension
next(gen)


# ================================================================
# Using iter() and next()
# ================================================================
lst = [10, 20, 30]
it = iter(lst)

next(it)   # 10
next(it)   # 20
next(it)   # 30
# next(it) -> StopIteration


# ================================================================
# Why generators?
# - lazy (create values on demand)
# - memory efficient (do NOT store full data)
# - single pass only
# ================================================================



