from typing import List

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def generate_fitness_plot(iterations: List[int], y: List[float], x_label="Iteration", y_label="Fitness", title="TSP Algorithm"):
	def format_y(value, _):
		return f"{value // 1000:.0f}k"  # Divide by 1000 and add 'k' suffix

	plt.plot(iterations, y, marker='')
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()
	plt.gca().yaxis.set_major_formatter(FuncFormatter(format_y))  # Apply the formatter
	plt.show()


def generate_log_plot(iterations: List[int], y: List[float], x_label="Iteration", y_label="Variance",
					  title="TSP Algorithm"):
	plt.plot(iterations, y, marker='')
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.yscale('log')
	plt.grid()
	plt.show()
