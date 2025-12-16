"""
NUMPY — Numerical Computing in Python
"""

import numpy as np

# =====================================================================
# Creating NumPy arrays
# =====================================================================

# From Python list
a = np.array([1, 2, 3])

# 2D array (matrix)
b = np.array([[1, 2, 3],
              [4, 5, 6]])

# Common array creators
np.zeros(5)              # [0. 0. 0. 0. 0.]
np.ones((2, 3))           # 2x3 matrix of ones
np.eye(3)                 # identity matrix
np.arange(0, 10, 2)       # [0 2 4 6 8]
np.linspace(0, 1, 5)      # evenly spaced values

# Random arrays
np.random.rand(3)         # uniform [0,1)
np.random.randn(3)        # normal distribution
np.random.randint(0, 10, size=5)


# =====================================================================
# Array properties
# =====================================================================

a.shape                  # dimensions (rows, cols)
a.ndim                   # number of dimensions
a.size                   # total number of elements
a.dtype                  # data type


# =====================================================================
# Indexing & slicing
# =====================================================================

a = np.array([10, 20, 30, 40, 50])

a[0]                     # first element
a[-1]                    # last element
a[1:4]                   # slicing

# 2D indexing
b = np.array([[1, 2, 3],
              [4, 5, 6]])

b[0, 1]                  # row 0, column 1
b[:, 1]                  # all rows, column 1
b[1, :]                  # row 1

# Boolean indexing
a[a > 25]                # elements greater than 25


# =====================================================================
# Vectorized operations (NO LOOPS!)
# =====================================================================

a = np.array([1, 2, 3])

a + 10                   # [11 12 13]
a * 2                    # [2 4 6]
a ** 2                   # [1 4 9]

b = np.array([4, 5, 6])
a + b                    # element-wise addition


# =====================================================================
# Mathematical functions
# =====================================================================

np.sum(a)
np.mean(a)
np.min(a)
np.max(a)
np.std(a)

np.sqrt(a)
np.exp(a)
np.log(a)

# Axis argument (important!)
m = np.array([[1, 2, 3],
              [4, 5, 6]])

np.sum(m, axis=0)        # column-wise sum
np.sum(m, axis=1)        # row-wise sum


# =====================================================================
# Reshaping arrays
# =====================================================================

a = np.arange(6)

a.reshape((2, 3))        # reshape to 2x3
a.reshape(-1, 1)         # column vector
a.flatten()              # 1D copy
a.ravel()                # 1D view (if possible)


# =====================================================================
# Broadcasting
# =====================================================================

# NumPy automatically expands smaller arrays
a = np.array([1, 2, 3])
b = np.array([[10],
              [20],
              [30]])

a + b
# Result:
# [[11 12 13]
#  [21 22 23]
#  [31 32 33]]


# =====================================================================
# Copy vs View (VERY IMPORTANT FOR EXAM)
# =====================================================================

a = np.array([1, 2, 3])

b = a        # reference
c = a.copy() # independent copy

a[0] = 100
b[0]         # 100 (same object)
c[0]         # 1   (separate memory)


# =====================================================================
# Stacking & concatenation
# =====================================================================

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

np.concatenate([a, b])
np.vstack([a, b])        # vertical stack
np.hstack([a, b])        # horizontal stack


# =====================================================================
# Loading & saving data
# =====================================================================

np.save("array.npy", a)
np.load("array.npy")

# Text files (CSV-like)
np.savetxt("data.txt", a)
np.loadtxt("data.txt")


# =====================================================================
# Linear algebra
# =====================================================================

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

A @ B                     # matrix multiplication
np.dot(A, B)

np.linalg.det(A)          # determinant
np.linalg.inv(A)          # inverse
np.linalg.eig(A)          # eigenvalues/vectors


# =====================================================================
# Comparison: NumPy vs Python lists
# =====================================================================

# Python list
lst = [1, 2, 3]
# lst + 1  -> ERROR

# NumPy array
arr = np.array(lst)
arr + 1                   # works (vectorized)

# NumPy is:
# - faster
# - memory efficient
# - designed for numerical operations
