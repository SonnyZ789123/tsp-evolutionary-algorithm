from typing import List

import matplotlib.pyplot as plt


def generate_plot(iterations: List[int], y: List[float], x_label="Iteration", y_label="fitness"):
	plt.plot(iterations, y, marker='')
	plt.title("Line Plot Example")
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()
	plt.show()


def normalize_to_0_100(values: List[float], bottom: int = 0, top: int = 100) -> List[float]:
	min_val = min(values)
	max_val = max(values)

	# Ensure the range is non-zero to avoid division by zero
	range_val = max_val - min_val
	if range_val == 0:
		return [100.0 for _ in values]  # All values are the same

	# Normalize values to [0, 1] and then scale to [0, 100]
	normalized = [((x - min_val) / range_val * top) + bottom for x in values]
	return normalized
