import matplotlib.pyplot as plt
import numpy as np

file = open("tour50_means.txt")
mean_fitness_data = np.loadtxt(file, delimiter=",")
file.close()

# Plot histogram
plt.hist(mean_fitness_data, bins=50, edgecolor='black', alpha=0.7)
plt.title('Histogram of mean fitness for tour50.csv')
plt.xlabel('Mean fitness')
plt.ylabel('Frequency')

# Calculate and display standard deviation
std_dev_mean_fitness = np.std(mean_fitness_data)
plt.axvline(np.mean(mean_fitness_data), color='red', linestyle='dashed', linewidth=1, label=f'Mean: {np.mean(mean_fitness_data):.2f}')
plt.axvline(np.mean(mean_fitness_data) + std_dev_mean_fitness, color='green', linestyle='dashed', linewidth=1, label=f'+1 StdDev: {std_dev_mean_fitness:.2f}')
plt.axvline(np.mean(mean_fitness_data) - std_dev_mean_fitness, color='green', linestyle='dashed', linewidth=1)
plt.legend()

plt.show()



file = open("tour50_best.txt")
best_fitness_data = np.loadtxt(file, delimiter=",")
file.close()

# Plot histogram
plt.hist(best_fitness_data, bins=50, edgecolor='black', alpha=0.7)
plt.title('Histogram of best fitness for tour50.csv')
plt.xlabel('Best fitness')
plt.ylabel('Frequency')

# Calculate and display standard deviation
std_dev_best_fitness = np.std(best_fitness_data)
plt.axvline(np.mean(best_fitness_data), color='red', linestyle='dashed', linewidth=1, label=f'Mean: {np.mean(best_fitness_data):.2f}')
plt.axvline(np.mean(best_fitness_data) + std_dev_best_fitness, color='green', linestyle='dashed', linewidth=1, label=f'+1 StdDev: {std_dev_best_fitness:.2f}')
plt.axvline(np.mean(best_fitness_data) - std_dev_best_fitness, color='green', linestyle='dashed', linewidth=1)
plt.legend()

plt.show()
