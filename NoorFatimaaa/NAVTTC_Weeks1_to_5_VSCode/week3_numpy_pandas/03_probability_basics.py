# Week 3 — Basic probability, joint and conditional probability examples

# A fair six-sided die: each outcome has probability 1/6.
probability_even = 3 / 6
probability_greater_than_4 = 2 / 6
print("P(even):", probability_even)
print("P(greater than 4):", probability_greater_than_4)

# Example group of 100 students
total = 100
likes_python = 60
likes_numpy = 40
likes_both = 25
print("P(Python):", likes_python / total)
print("P(NumPy):", likes_numpy / total)
print("P(Python and NumPy):", likes_both / total)
print("P(NumPy | Python):", likes_both / likes_python)

# Bayes' theorem demonstration
p_disease = 0.01
p_positive_given_disease = 0.95
p_positive_given_no_disease = 0.05
p_positive = (p_positive_given_disease * p_disease +
              p_positive_given_no_disease * (1 - p_disease))
p_disease_given_positive = p_positive_given_disease * p_disease / p_positive
print("P(disease | positive):", round(p_disease_given_positive, 4))
