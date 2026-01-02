import numpy as np

# Question 1
# What should be put instead of __ to obtain the output (2, 3)?
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.__)

# Answer:

# Question 2
# What should be put instead of __ to turn a 1D array of 6 elements
# into a 2D array with 3 rows and 2 columns?
arr = np.arange(6)
new_arr = arr.__(3, 2)
print(new_arr.shape)

# Answer:

# Question 3
# What should be put instead of __ to select the last two elements of the array?
# Output: [8 9]
arr = np.array([5, 6, 7, 8, 9])
print(arr[__])

# Answer:

# Question 4
# What should be put instead of __ to extract only the values that are greater than 10?
# Output: [12 15]
arr = np.array([5, 12, 8, 15, 3])
print(arr[__])

# Answer:

# Question 5
# What should be put instead of __ to calculate the mean of each column (vertically)?
# Output: [2. 3.]
arr = np.array([[1, 2], [3, 4]])
print(arr.mean(axis=__))

# Answer:

# Question 6
# What should be put instead of __ to find the indices of all elements
# that are exactly equal to 7?
# Output: (array([2]),)
arr = np.array([1, 5, 7, 2, 9])
print(__(arr == 7))

# Answer:

# Question 7
# In NumPy, which bitwise operator should be put instead of __
# to filter values that are both greater than 5 AND even?
# Output: [6 8]
arr = np.array([2, 5, 6, 7, 8, 9])
mask = (arr > 5)__(arr % 2 == 0)
print(arr[mask])

# Answer:

# Question 8
# What should be put instead of __ to create an array of 4 evenly
# spaced values starting from 0 and ending at 1?
# Output: [0. 0.33333333 0.66666667 1. ]
arr = np.__(0, 1, 4)
print(arr)

# Answer:

# Question 9
# What should be put instead of __ to check the memory size
# of a single element in the array (in bytes)?
arr = np.array([1, 2, 3], dtype=np.int64)
print(arr.__)

# Answer:

# Question 10
# What should be put instead of __ to perform a vectorized operation
# that multiplies every element in the array by 10?
# Output: [10 20 30]
arr = np.array([1, 2, 3])
result = arr
__
10
print(result)

# Answer: