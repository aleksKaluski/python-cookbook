"""
NUMPY — Numerical Computing in Python
Comprehensive Snippets for Learning & Test Prep
"""

import numpy as np

# =====================================================================
# 1. Creating NumPy Arrays
# =====================================================================

# From Python list (1D)
a = np.array([1, 2, 3])

# 2D array (matrix)
b = np.array([[1, 2, 3],
              [4, 5, 6]])

# 3D array (tensor) -
c = np.array([[[1, 2], [3, 4]],
              [[5, 6], [7, 8]]])

# Common array creators
np.zeros(5)               # [0. 0. 0. 0. 0.]
np.ones((2, 3))           # 2x3 matrix of ones
np.full((3, 2), 5)        # 3x2 matrix filled with 5
np.eye(3)                 # 3x3 identity matrix
np.arange(0, 10, 2)       # [0 2 4 6 8] (start, stop, step)
np.linspace(0, 1, 5)      # 5 evenly spaced values between 0 and 1

# Random arrays
np.random.rand(3)         # uniform distribution [0,1)
np.random.randn(3)        # normal distribution (mean=0, var=1)
np.random.randint(0, 10, size=(2,2)) # random integers

# =====================================================================
# 2. Array Properties & Data Types
# =====================================================================

# Attributes
a.shape                   # dimensions (rows, cols)
a.ndim                    # number of dimensions (axes)
a.size                    # total number of elements
a.dtype                   # data type (e.g., int64, float64)

# Specific Data Types & Memory
# Smaller bits = less memory; Larger bits = more precision
d = np.array([1, 2], dtype=np.int16)
e = np.array([1, 2], dtype=np.float128) # high precision

# Type Conversion
f = a.astype(float)       # casts array to float

# =====================================================================
# 3. Reshaping and Slicing
# =====================================================================

# Reshaping
grid = np.arange(12).reshape(3, 4)

# Basic Slicing
# array[row_start:row_stop, col_start:col_stop]
grid[0:2, 1:3]            # rows 0-1, columns 1-2
grid[:, 0]                # all rows, first column only
grid[1, :]                # second row, all columns

# =====================================================================
# 4. Advanced Indexing
# =====================================================================

# Fancy Indexing (Integer Indexing)
# Selecting specific elements by providing lists of coordinates
arr = np.array([10, 20, 30, 40, 50])
arr[[0, 2, 4]]            # [10, 30, 50]

# Boolean Indexing (Masking)
mask = arr > 25           # [False, False, True, True, True]
arr[mask]                 # [30, 40, 50]
arr[arr % 20 == 0]        # elements divisible by 20

# Bitwise Logic for Filtering
# & (and), | (or), ~ (not)
arr[(arr > 10) & (arr < 50)]
arr[(arr == 10) | (arr == 50)]
arr[~(arr == 30)]         # Everything except 30

# Examples:

# Given a 4x4 matrix, extract the 2x2 "inner" sub-matrix
matrix = np.arange(16).reshape(4, 4)
inner_square = matrix[1:3, 1:3]
# Slicing from index 1 up to (but not including) index 3
# selects the middle two elements in both dimensions.

# Extract the scores (2nd column)
# only for the rows where the score is 80 or higher
results = np.array([[101, 75], [102, 90], [103, 82], [104, 60]])
high_scores = results[:, 1] >= 80
# The first part of the index is a boolean mask for the rows;
# the second part ', 1' selects the second column.
# =====================================================================
# 5. Vectorization & Broadcasting
# =====================================================================

# Vectorization: Avoid loops; operations are element-wise
arr1 = np.array([1, 2, 3])
arr1 * 5                  # [5, 10, 15]

# Broadcasting: Operating on arrays of different shapes
# Rule: Dimensions must match or one must be 1
m = np.ones((3, 3))       # 3x3 matrix
v = np.array([1, 2, 3])   # 1D vector (shape 3,)
m + v                     # v is "stretched" to 3x3 and added to each row

# =====================================================================
# 6. Useful Functions
# =====================================================================

# Finding Indices
np.where(arr > 30)        # returns indices where condition is True

# Membership Testing
np.isin(arr, [10, 50])    # [True, False, False, False, True]

# Aggregations
arr.sum(), arr.mean(), arr.std()
arr.max(), arr.min()
grid.mean(axis=0)         # mean of each column (downwards)
grid.mean(axis=1)         # mean of each row (across)

# =====================================================================
# 7. Linear Algebra & Stacking
# =====================================================================

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Multiplication
A @ B                     # matrix multiplication
np.dot(A, B)

# Stacking
np.vstack([A, B])         # vertical stack
np.hstack([A, B])         # horizontal stack
np.concatenate([A, B], axis=0)

# Matrix Operations
np.linalg.det(A)          # determinant
np.linalg.inv(A)          # inverse

# =====================================================================
# 8. Loading & Saving
# =====================================================================

np.save("my_array.npy", A)
loaded = np.load("my_array.npy")

# =====================================================================
# 9. ADVANCED: The "Why" — Static Typing & Core Library
# =====================================================================

# Dynamic Typing (Python) vs Static Typing (NumPy/C)
# Python lists allow mixed types (slow); NumPy requires one type (fast)
# NumPy is faster because:
# 1. Core Library: Written in C/C++
# 2. Fixed Data Type: homogeneous elements allow optimal handling
# 3. Minimized Transfer: vectorization limits data pass between Python and C

# =====================================================================
# 10. ADVANCED: Broadcasting Rules in Detail
# =====================================================================

# Rule: Compatible if dimensions match or one of them is 1
# Example 1: (4, 3) and (3,) -> Compatible (3 matches 3)
# Example 2: (4, 3) and (4, 1) -> Compatible (1 can be stretched to 3)
# Example 3: (4, 3) and (4,) -> ERROR (Trailing dims must match)

x = np.arange(12).reshape(4, 3)
y = np.array([1, 0, 1])   # shape (3,)
result = x + y            # adds y to every row of x

# =====================================================================
# 11. ADVANCED: Deep Boolean Masking
# =====================================================================

# Mixing standard indexing and boolean masks
# Select all rows, but only columns where the mask is True
mask_cols = [True, False, True]
sub_grid = grid[:, mask_cols]

# Selecting specific coordinates using two masks
rows = [True, False, True]
cols = [True, False, False, True]
# grid[rows, cols] would select specific elements like integer indexing

# =====================================================================
# 12. ADVANCED: Universal Functions (ufuncs)
# =====================================================================

# ufuncs perform element-wise operations on ndarrays
np.exp(a)      # exponential
np.sqrt(a)     # square root
np.sin(a)      # trigonometric
np.add(a, b)   # binary ufunc (same as a + b)

# =====================================================================
# 13. ADVANCED: Memory & Performance
# =====================================================================

# Performance testing (use %timeit in Jupyter/Lab)
# Vectorized operations are often 10x-100x faster than for-loops

# Copy vs. View (Critical for tests!)
# Slicing creates a VIEW (changes to slice affect original)
# Fancy indexing/Masking creates a COPY (changes do NOT affect original)

orig = np.array([1, 2, 3])
view_slice = orig[0:2]    # This is a view
copy_mask = orig[orig > 1] # This is a copy