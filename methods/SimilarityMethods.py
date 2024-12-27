import numpy as np

from config.custom_types import Cycle


class SimilarityMethods:
	@staticmethod
	def cycle_subtour_exponential(cycle1: Cycle, cycle2: Cycle) -> int:
		"""
		Calculate the cycle subtour exponential similarity between two cycles by actively looking for pieces of the that
		are the same, and exponentially rewarding the similarity of long sub tours.
		:param cycle1: First cycle.
		:param cycle2: Second cycle.
		:return: Similarity between the two cycles.
		"""
		cycle_length = len(cycle1)
		assert cycle_length == len(cycle2), "Cycles should have the same length"

		similarity = 0
		# Using a streak, so that the similarity is weighted by the length of the streak.
		# So cycles with the same long subtour will have a higher similarity than cycles with many shorter sub tours.
		streak = 0
		i = 0

		# Take into account if the first element is part of a sub tour but not the first element of the sub tour.
		# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		# [1, 2, 5, 6, 8, 7, 3, 4, 9, 0]
		# 0 is part of a sub tour, but not the first element of the sub tour, so it will think that only (0 1 2) is the
		# sub tour while it should be (9 0 1 2)
		city_i = cycle1[i]
		j = np.where(cycle2 == city_i)[0][0]

		# do the first time in reverse, so that the streak is correct, and we are sure we have the full first sub tour
		k = cycle_length - 1
		l = j - 1
		# but don't start on the first element, that's for the next while-loop
		while k >= 0 and cycle1[k] == cycle2[l % cycle_length]:
			similarity += 2 ** streak
			streak += 1
			k -= 1
			l -= 1

		# we already found a part of a sub tour from k, but we do want to check cycle[k] because that didn't match
		end = k + 1
		# now start on the first element
		while i < end:
			city_i = cycle1[i]
			# find the index of i in cycle2
			j = np.where(cycle2 == city_i)[0][0]

			while (i < end and
				   cycle1[i] == cycle2[j % cycle_length]):
				similarity += 2 ** streak
				streak += 1
				i += 1
				j += 1
			streak = 0

		return similarity