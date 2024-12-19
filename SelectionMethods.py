import numpy as np


class SelectionMethods:
    @staticmethod
    def random(population):
        return population.individuals[np.random.randint(0, population.size)]

