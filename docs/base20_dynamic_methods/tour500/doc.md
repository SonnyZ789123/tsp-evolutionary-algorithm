# Tour500 optimization (baseline 157034)

## Common

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- fitness: `negative_of_length`

## Iteration 1 (last iteration algorithm)

- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=30`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: `k_opt` with `proportion_worst=0.5`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.5`,
  `mixed_elitist_with_crowding_k=5`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

- Elapsed time for solving TSP: 93.81 seconds
- Best individual cycle length: 167427

---

- Elapsed time for solving TSP: 126.73 seconds
- Best individual cycle length: 162013

---

- Elapsed time for solving TSP: 158.75 seconds
- Best individual cycle length: 166706

---

Best solution gets stuck in first iteration.

## Iteration 2 (increase `best_fitness_count` convergence and quadratic decay mutation)

- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=100`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.4` and `alpha_decay_rate=0.001`
- local optimisation: `k_opt` with `proportion_worst=0.2`, `opt_probability=0.5`, `k_opt_pool_size=3`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.5`,
  `mixed_elitist_with_crowding_k=5`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

Convergence `best_fitness_count_threshold` increased from 30 to 100, to make sure it can run long enough to generate a
good individual.

---

- Elapsed time for solving TSP: 301.34 seconds
- Best individual cycle length: 160123

---

- Elapsed time for solving TSP: 300.06 seconds
- Best individual cycle length: 168826

---

- Elapsed time for solving TSP: 300.24 seconds
- Best individual cycle length: 168642

---

It's already better, I see the best individual increasing.

## Iteration 3 (half the population size)

- population size: 100
- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=100`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
  mutation: `reverse_subtour` with `alpha=0.4` and `alpha_decay_rate=0.001`
- local optimisation: `k_opt` with `proportion_worst=0.2`, `opt_probability=0.5`, `k_opt_pool_size=3`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.5`,
  `mixed_elitist_with_crowding_k=5`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

- Elapsed time for solving TSP: 187.19 seconds
- Best individual cycle length: 166047

---

- Elapsed time for solving TSP: 114.43 seconds
- Best individual cycle length: 163037

---

- Elapsed time for solving TSP: 300.70 seconds
- Best individual cycle length: 163027

---

- Elapsed time for solving TSP: 231.33 seconds
- Best individual cycle length: 166385

---

- Elapsed time for solving TSP: 188.32 seconds
- Best individual cycle length: 168846

---

> Average Elapsed Time: 204.4

> Average Cycle Length: 165468.25

Seems like halving the population just makes the diversity worse because not a lot of times does a new best solution get
found.

## Iteration 4 (increase `best_fitness_count` convergence and increase population size)

Trying to increase diversity by increasing the crowding parameters.

- population size: 200
- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=100`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
  mutation: `reverse_subtour` with `alpha=0.4` and `alpha_decay_rate=0.001`
- local optimisation: `k_opt` with `proportion_worst=0.2`, `opt_probability=0.5`, `k_opt_pool_size=3`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.4`,
  `mixed_elitist_with_crowding_k=7`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

- Elapsed time for solving TSP: 300.65 seconds
- Best individual cycle length: 167839

---

- Elapsed time for solving TSP: 301.84 seconds
- Best individual cycle length: 162390

---

- Elapsed time for solving TSP: 300.84 seconds
- Best individual cycle length: 160725

---

- Elapsed time for solving TSP: 301.18 seconds
- Best individual cycle length: 164307

---

- Elapsed time for solving TSP: 300.10 seconds
- Best individual cycle length: 165827

---

> Average Elapsed Time: 300.92

> Average Cycle Length: 164217.77

It's not significantly better, but I see that the best individual changes a couple of times, and the computation time is
higher.

## Iteration 5 (increase local optimisation for worst individuals)

Increased `alpha` probability mutation to 0.5, `k_opt` pool size to 5 and `proportion_worst` to 0.3.

- population size: 200
- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=100`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
  mutation: `reverse_subtour` with `alpha=0.5` and `alpha_decay_rate=0.001`
- local optimisation: `k_opt` with `proportion_worst=0.3`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.4`,
  `mixed_elitist_with_crowding_k=7`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

- Elapsed time for solving TSP: 300.50 seconds
- Best individual cycle length: 165418

---

- Elapsed time for solving TSP: 300.92 seconds
- Best individual cycle length: 161359

---

- Elapsed time for solving TSP: 301.66 seconds
- Best individual cycle length: 161621

---

- Elapsed time for solving TSP: 301.29 seconds
- Best individual cycle length: 164161

---

- Elapsed time for solving TSP: 302.06 seconds
- Best individual cycle length: 167176

---
> Average Elapsed Time: 301.29

> Average Cycle Length: 163947.01

Better, I think that increasing the mutation probability really helped.

## Iteration 5 (increase local optimisation for worst individuals)

Using `elitist_k_tournament` elimination method to increase diversity. Remove the "insert diversity" because I think it
is not necessary anymore.

- population size: 200
- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=100`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
  mutation: `reverse_subtour` with `alpha=0.5` and `alpha_decay_rate=0.001`
- local optimisation: `k_opt` with `proportion_worst=0.3`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `elitist_k_tournament` with `elitist_k_tournament_k=3`.
- insert diversity: None

---

- Elapsed time for solving TSP: 301.26 seconds
- Best individual cycle length: 201786

---

- Elapsed time for solving TSP: 300.34 seconds
- Best individual cycle length: 174779

Didn't work so good because we lose the best individual.

## Iteration 6 (keep k best individuals)

Using `elitist_k_tournament_keep_s_best` elimination method to increase diversity, and keep the s best individuals.

- population size: 200
- convergence: `max_iterations` and `best_fitness_count` with `best_fitness_count_threshold=100`
- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
  mutation: `reverse_subtour` with `alpha=0.5` and `alpha_decay_rate=0.001`
- local optimisation: `k_opt` with `proportion_worst=0.3`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `elitist_k_tournament_keep_s_best` with `elitist_k_tournament_keep_s_best_k=3`,
  `elitist_k_tournament_keep_s_best_s=5`.
- insert diversity: None

---

- Elapsed time for solving TSP: 300.81 seconds
- Best individual cycle length: 168149

---

- Elapsed time for solving TSP: 300.11 seconds
- Best individual cycle length: 165905

---

- Elapsed time for solving TSP: 300.13 seconds
- Best individual cycle length: 164412

---

- Elapsed time for solving TSP: 300.53 seconds
- Best individual cycle length: 159324

---

- Elapsed time for solving TSP: 300.97 seconds
- Best individual cycle length: 166224

---

> Average Elapsed Time: 300.51

> Average Cycle Length: 164802.76

Actually pretty good results, not better but is faster. With this version it got to 210 iterations, while the algorithm
with `mixed_elitist_with_crowding` and `replace_worst_with_random` got to 140 iterations. So I keep this version.