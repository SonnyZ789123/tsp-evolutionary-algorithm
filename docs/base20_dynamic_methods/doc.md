# Base 20 - Dynamic Methods based on Problem Size

## Common

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations` and `best_fitness_count`
- fitness: `negative_of_length`

## Tour50 (baseline 27723)

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour`
- local optimisation: `k_opt`
- elimination: `mixed_elitist_with_crowding`
- insert diversity: `replace_worst_with_random`

## Tour100 (baseline 90851)

Pretty sure this is the best, but have to recheck.


- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: `k_opt` with `proportion_worst=0.5`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitism_rest_merged_random_mixed_elitist_proportion=0.5`, `mixed_elitism_rest_merged_random_proportion_size=0.5`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

## Tour200 (baseline 39745)

## Tour500 (baseline 157034)

## Tour750 (baseline 197541)

## Tour1000 (baseline 195848)