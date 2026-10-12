# Week 2 — Mean, median, mode, variance, standard deviation, z-score, percentiles
import statistics

scores = [55, 60, 60, 72, 80, 85, 90]
mean_value = statistics.mean(scores)
median_value = statistics.median(scores)
mode_value = statistics.mode(scores)
variance_value = statistics.variance(scores)
std_value = statistics.stdev(scores)

print("Scores:", scores)
print("Mean:", round(mean_value, 2))
print("Median:", median_value)
print("Mode:", mode_value)
print("Sample variance:", round(variance_value, 2))
print("Sample standard deviation:", round(std_value, 2))

score = 80
z_score = (score - mean_value) / std_value
print("Z-score of 80:", round(z_score, 2))
print("Approx. 75th percentile:", sorted(scores)[round((len(scores)-1)*0.75)])
