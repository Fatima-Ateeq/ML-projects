# Week 3 — NumPy copy/view, append, insert, concatenate, split, sort, save/load
import numpy as np
from pathlib import Path

original = np.array([5, 2, 9, 1])
copied = original.copy()
copied[0] = 100
print("Original:", original)
print("Copy changed:", copied)
print("Sorted:", np.sort(original))
print("Append:", np.append(original, 7))
print("Insert:", np.insert(original, 1, 99))
print("Delete:", np.delete(original, 2))

left = np.array([1, 2])
right = np.array([3, 4])
print("Concatenate:", np.concatenate((left, right)))
print("Split:", np.split(np.array([10, 20, 30, 40]), 2))

output = Path(__file__).with_name("numbers.npy")
np.save(output, original)
print("Loaded saved array:", np.load(output))
