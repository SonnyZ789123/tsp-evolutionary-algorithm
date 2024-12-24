from typing import List


def normalize_list(values: List[float], bottom: int = 0, top: int = 100) -> List[float]:
	min_val = min(values)
	max_val = max(values)

	# Ensure the range is non-zero to avoid division by zero
	range_val = max_val - min_val
	if range_val == 0:
		return [100.0 for _ in values]  # All values are the same

	# Normalize values to [0, 1] and then scale to [bottom, top]
	normalized_range = top - bottom
	normalized = [((x - min_val) / range_val * normalized_range) + bottom for x in values]
	return normalized