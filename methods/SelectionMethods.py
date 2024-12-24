import numpy as np


class SelectionMethods:
    @staticmethod
    def random(population):
        return population.individuals[np.random.randint(0, population.size)]

    @staticmethod
    def k_tournament(population, k):
        selected = []
        for _ in range(k):
            selected.append(SelectionMethods.random(population))
        return max(selected, key=lambda x: x.fitness)
