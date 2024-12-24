from typing import List

import matplotlib.pyplot as plt


def generate_plot(iterations: List[int], y: List[float], x_label="Iteration", y_label="fitness"):
	plt.plot(iterations, y, marker='')
	plt.title("Line Plot Example")
	plt.xlabel(x_label)
	plt.ylabel(y_label)
	plt.grid()
	plt.show()
