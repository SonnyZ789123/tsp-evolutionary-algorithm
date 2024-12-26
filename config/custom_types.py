from typing import Callable, List

import numpy as np
from numpy.typing import NDArray

DistanceMatrix = NDArray[float]  # A 2D numpy array
Cycle = NDArray[np.int64]  # A 1D numpy array
InitializationHeuristic = Callable[[int, DistanceMatrix, List[int]], int]
INFINITY_REPRESENTATION = 1e+10
