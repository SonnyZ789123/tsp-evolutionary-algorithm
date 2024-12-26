from r0829897 import r0829897


def main():
	solve_tsp = r0829897()
	solve_tsp.optimize("tour500.csv")

if __name__ == "__main__":
	main()
