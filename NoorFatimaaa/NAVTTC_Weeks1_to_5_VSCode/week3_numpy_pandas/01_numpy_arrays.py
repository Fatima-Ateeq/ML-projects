# Week 3 — NumPy arrays, attributes, reshape, selection, operations
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])
print("Array:", numbers)
print("Shape:", numbers.shape, "Size:", numbers.size, "Dimensions:", numbers.ndim)
print("Data type:", numbers.dtype)
print("Min/max:", numbers.min(), numbers.max())
print("Index of maximum:", numbers.argmax())
print("Squared:", numbers ** 2)
print("Square roots:", np.sqrt(numbers))
print("Values above 25:", numbers[numbers > 25])

matrix = np.arange(1, 13).reshape(3, 4)
print("\nMatrix:\n", matrix)
print("First row:", matrix[0])
print("Rows 1 onward, columns 2 onward:\n", matrix[1:, 2:])
print("Column sums:", matrix.sum(axis=0))

random_values = np.random.default_rng(42).integers(1, 100, size=5)
print("Reproducible random values:", random_values)
