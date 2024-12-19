from typing import Tuple
import numpy as np


class RecombinationMethods:
    @staticmethod
    def partially_mapped_crossover(parent1: np.ndarray, parent2: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """
        Performs Partially Mapped Crossover (PMX) for two parents.
        parent1, parent2: numpy arrays representing the cycles of the parents.

        Returns two offspring as numpy arrays.
        """
        size = len(parent1)
        assert size == len(parent2), "Parents must have the same length"

        # Randomly choose two crossover points
        cut1, cut2 = sorted(np.random.choice(range(size), 2, replace=False))

        # Initialize offspring with -1 (indicating empty spots)
        offspring1 = -1 * np.ones(size, dtype=int)
        offspring2 = -1 * np.ones(size, dtype=int)

        # Copy the segment from parents to offspring
        offspring1[cut1:cut2] = parent1[cut1:cut2]
        offspring2[cut1:cut2] = parent2[cut1:cut2]

        # Fill the rest of the offspring ensuring valid permutations
        def fill_offspring(offspring, parent, start, end):
            for i in range(start, end):
                if parent[i] not in offspring:
                    # Find the first available position
                    while offspring[i] != -1:
                        i = np.where(parent == offspring[i])[0][0]
                    offspring[i] = parent[i]

            # Fill remaining empty spots
            for i in range(len(offspring)):
                if offspring[i] == -1:
                    offspring[i] = parent[i]

        # Fill the remaining parts of the offspring
        fill_offspring(offspring1, parent2, cut1, cut2)
        fill_offspring(offspring2, parent1, cut1, cut2)

        return offspring1, offspring2
