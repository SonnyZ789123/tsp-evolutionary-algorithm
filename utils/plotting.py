from typing import List

import matplotlib.pyplot as plt


def generate_plot(iterations: List[int], y: List[float], x_label="Iteration", y_label="fitness", title="TSP Algorithm"):
	plt.plot(iterations, y, marker='')
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()
	plt.show()

def generate_log_plot(iterations: List[int], y: List[float], x_label="Iteration", y_label="fitness", title="TSP Algorithm"):
	plt.plot(iterations, y, marker='')
	plt.title(title)
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.yscale('log')
	plt.grid()
	plt.show()
