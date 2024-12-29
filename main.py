from r0829897 import r0829897


def main():
	solve_tsp = r0829897()
	return solve_tsp.optimize("tour500.csv")

if __name__ == "__main__":
	best_cycle_lengths = []
	elapsed_times = []
	for _ in range(5):
		elapsed_time, best_cycle_length = main()
		best_cycle_lengths.append(best_cycle_length)
		elapsed_times.append(elapsed_time)
	print("Average Elapsed Time:", round(sum(elapsed_times) / len(elapsed_times), 2))
	print("Average Cycle Length:", round(sum(best_cycle_lengths) / len(best_cycle_lengths), 2))

