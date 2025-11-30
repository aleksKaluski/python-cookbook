# =====================================================================
# itertools — advanced iterator tools
#
# These functions RETURN ITERATORS.
# They are efficient because they DO NOT create full lists in memory.
# =====================================================================

import itertools as it

# ---------------------------------------------------------
# Infinite iterators
# ---------------------------------------------------------
it.count(start=0, step=1)
# → 0, 1, 2, 3, ... forever

it.cycle([1, 2, 3])
# → 1, 2, 3, 1, 2, 3, ... forever

it.repeat(10, 3)
# → 10, 10, 10


# ---------------------------------------------------------
# Accumulation and chaining
# ---------------------------------------------------------
it.accumulate([1, 2, 3])
# running totals: 1, 3, 6

it.chain([1, 2], [3, 4])
# flatten lists: 1, 2, 3, 4


# ---------------------------------------------------------
# Filtering and slicing
# ---------------------------------------------------------
it.islice(range(100), 10, 20)
# slice without making a list:
# → 10, 11, 12, ... 19

it.takewhile(lambda x: x < 5, [1, 2, 3, 6, 7])
# stop when condition becomes False:
# → 1, 2, 3

it.dropwhile(lambda x: x < 5, [1, 2, 3, 6, 7])
# skip values while condition is True, then return the rest:
# → 6, 7


# ---------------------------------------------------------
# Grouping
# ---------------------------------------------------------
it.groupby([1, 1, 2, 2, 3, 3])
# groups consecutive identical items:
# group 1 → [1, 1]
# group 2 → [2, 2]
# group 3 → [3, 3]
# NOTE: input must be pre-sorted for meaningful grouping.
