import numpy as np

# this program performs Statistical operations like mean, max and std deviation
arr = np.array([1.1, 2.2, 3.3, 4.4, 5.5])

# Computing the mean
mean = np.mean(arr)

# Computing the mininum value & maximum value
min_value = np.min(arr)
max_value = np.max(arr)

# Computing the standard deviation
std_dev = np.std(arr)

# Printing
print(arr)
print("Mean  = ",mean)
print(" Min  = ",min_value)
print(" Max  = ",max_value)
print("Std dev = ",std_dev)
print()
