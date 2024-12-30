# Tour50 optimization (baseline 27723)

## Common

- initialization: 1 `generate_greedy_population` with `nearest_neighbour` and rest `generate_random_valid_population`
- convergence: `max_iterations` and `best_fitness_count`
- fitness: `negative_of_length`

## Iteration 1 (last iteration algorithm)

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: `k_opt` with `proportion_worst=0.5`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.5`,
  `mixed_elitist_with_crowding_k=5`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

- Elapsed time for solving TSP: 35.66 seconds
- Best individual cycle length: 28495

---

- Elapsed time for solving TSP: 34.72 seconds
- Best individual cycle length: 26901

---

- Elapsed time for solving TSP: 35.98 seconds
- Best individual cycle length: 26178

---

- Elapsed time for solving TSP: 32.40 seconds
- Best individual cycle length: 25869

---

- Elapsed time for solving TSP: 35.02 seconds
- Best individual cycle length: 25888

---

- Elapsed time for solving TSP: 24.08 seconds
- Best individual cycle length: 26652

---

- Elapsed time for solving TSP: 26.12 seconds
- Best individual cycle length: 29142

---

- Elapsed time for solving TSP: 36.06 seconds
- Best individual cycle length: 28532

---

- Elapsed time for solving TSP: 35.32 seconds
- Best individual cycle length: 28828

---

- Elapsed time for solving TSP: 19.23 seconds
- Best individual cycle length: 28584

---

- Elapsed time for solving TSP: 19.23 seconds
- Best individual cycle length: 27155

---

- Elapsed time for solving TSP: 25.09 seconds
- Best individual cycle length: 26169

---

- Elapsed time for solving TSP: 18.50 seconds
- Best individual cycle length: 28240

---

- Elapsed time for solving TSP: 29.17 seconds
- Best individual cycle length: 26384

---

> Average Elapsed Time: 29.04 seconds

> Average Cycle Length: 27358.35

## Iteration 2 (minimal with `mixed_elitist_with_crowding`)

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: None
- elimination: `mixed_elitist_with_crowding` with `mixed_elitist_with_crowding_proportion=0.5`,
  `mixed_elitist_with_crowding_k=5`
- insert diversity: None

---

- Elapsed time for solving TSP: 9.94 seconds
- Best individual cycle length: 26840

---

- Elapsed time for solving TSP: 18.34 seconds
- Best individual cycle length: 28421

---

- Elapsed time for solving TSP: 9.29 seconds
- Best individual cycle length: 26356

---

- Elapsed time for solving TSP: 11.36 seconds
- Best individual cycle length: 26806

---

- Elapsed time for solving TSP: 13.46 seconds
- Best individual cycle length: 30016

---

- Elapsed time for solving TSP: 10.95 seconds
- Best individual cycle length: 26278

---

- Elapsed time for solving TSP: 10.39 seconds
- Best individual cycle length: 29956

---

- Elapsed time for solving TSP: 10.10 seconds
- Best individual cycle length: 26418

---

- Elapsed time for solving TSP: 12.13 seconds
- Best individual cycle length: 26368

---

- Elapsed time for solving TSP: 10.51 seconds
- Best individual cycle length: 27136

---

- Elapsed time for solving TSP: 12.00 seconds
- Best individual cycle length: 25951

---

- Elapsed time for solving TSP: 13.71 seconds
- Best individual cycle length: 26563

---

- Elapsed time for solving TSP: 10.12 seconds
- Best individual cycle length: 26733

---

- Elapsed time for solving TSP: 9.11 seconds
- Best individual cycle length: 28073

---

- Elapsed time for solving TSP: 13.73 seconds
- Best individual cycle length: 26104

---

- Elapsed time for solving TSP: 13.34 seconds
- Best individual cycle length: 26470

---

- Elapsed time for solving TSP: 11.51 seconds
- Best individual cycle length: 26697

---

- Elapsed time for solving TSP: 13.40 seconds
- Best individual cycle length: 26427

---

- Elapsed time for solving TSP: 12.69 seconds
- Best individual cycle length: 26597

---

- Elapsed time for solving TSP: 16.05 seconds
- Best individual cycle length: 25660

---

The average elapsed time is **12.11 seconds**, and the average best cycle length is **26,993.5**.

## Iteration 3 (minimal with `mixed_elitist`)

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: None
- elimination: `mixed_elitist` with `mixed_elitism_proportion=0.5`
- insert diversity: None

---

- Elapsed time for solving TSP: 15.06 seconds
- Best individual cycle length: 27576

---

- Elapsed time for solving TSP: 12.52 seconds
- Best individual cycle length: 26264

---

- Elapsed time for solving TSP: 9.42 seconds
- Best individual cycle length: 26063

---

- Elapsed time for solving TSP: 8.87 seconds
- Best individual cycle length: 26083

---

- Elapsed time for solving TSP: 8.58 seconds
- Best individual cycle length: 26981

---

- Elapsed time for solving TSP: 8.54 seconds
- Best individual cycle length: 26191

---

- Elapsed time for solving TSP: 11.83 seconds
- Best individual cycle length: 26645

---

- Elapsed time for solving TSP: 8.56 seconds
- Best individual cycle length: 25786

---

- Elapsed time for solving TSP: 11.75 seconds
- Best individual cycle length: 26742

---

- Elapsed time for solving TSP: 8.48 seconds
- Best individual cycle length: 27892

--- 

- Elapsed time for solving TSP: 9.34 seconds
- Best individual cycle length: 25891

---

- Elapsed time for solving TSP: 10.36 seconds
- Best individual cycle length: 27363

---

- Elapsed time for solving TSP: 9.29 seconds
- Best individual cycle length: 25939

---

- Elapsed time for solving TSP: 10.90 seconds
- Best individual cycle length: 26816

---

- Elapsed time for solving TSP: 6.76 seconds
- Best individual cycle length: 26793

---

- Elapsed time for solving TSP: 12.64 seconds
- Best individual cycle length: 27190

---

- Elapsed time for solving TSP: 14.59 seconds
- Best individual cycle length: 27565

---

- Elapsed time for solving TSP: 7.50 seconds
- Best individual cycle length: 28852

---

- Elapsed time for solving TSP: 11.56 seconds
- Best individual cycle length: 28465

---

- Elapsed time for solving TSP: 7.88 seconds
- Best individual cycle length: 26497

---

The average elapsed time is **10.22 seconds**, and the average best cycle length is **26,879.7**.

## Iteration 4 (minimal with `merged_fitness_based`)

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: None
- elimination: `merged_fitness_based`
- insert diversity: None

---

- Elapsed time for solving TSP: 10.23 seconds
- Best individual cycle length: 25917

---

- Elapsed time for solving TSP: 7.55 seconds
- Best individual cycle length: 27332

---

- Elapsed time for solving TSP: 14.93 seconds
- Best individual cycle length: 28330

---

- Elapsed time for solving TSP: 9.95 seconds
- Best individual cycle length: 26333

---

- Elapsed time for solving TSP: 6.37 seconds
- Best individual cycle length: 27416

---

- Elapsed time for solving TSP: 7.89 seconds
- Best individual cycle length: 27716

---

- Elapsed time for solving TSP: 8.99 seconds
- Best individual cycle length: 26567

---

- Elapsed time for solving TSP: 9.26 seconds
- Best individual cycle length: 27028

---

- Elapsed time for solving TSP: 9.82 seconds
- Best individual cycle length: 28430

---

- Elapsed time for solving TSP: 10.58 seconds
- Best individual cycle length: 26603

---

The average elapsed time is **9.56 seconds**, and the average best cycle length is **27,167.2**.

# Iteration 5 (minimal with `mixed_elitist` with `mixed_elitism_proportion=0.7`)

> Average to beat: elapsed time is **10.22 seconds**, and best cycle length **26,879.7**.

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: None
- elimination: `mixed_elitist` with `mixed_elitism_proportion=0.7`
- insert diversity: None

---

- Elapsed time for solving TSP: 10.03 seconds
- Best individual cycle length: 26762

---

- Elapsed time for solving TSP: 9.18 seconds
- Best individual cycle length: 29009

---

- Elapsed time for solving TSP: 10.18 seconds
- Best individual cycle length: 27193

---

- Elapsed time for solving TSP: 12.11 seconds
- Best individual cycle length: 27023

---

- Elapsed time for solving TSP: 8.16 seconds
- Best individual cycle length: 28631

---

- Elapsed time for solving TSP: 16.60 seconds
- Best individual cycle length: 27667

---

- Elapsed time for solving TSP: 9.02 seconds
- Best individual cycle length: 28260

---

- Elapsed time for solving TSP: 14.67 seconds
- Best individual cycle length: 26040

---

- Elapsed time for solving TSP: 11.76 seconds
- Best individual cycle length: 26906

---

- Elapsed time for solving TSP: 9.76 seconds
- Best individual cycle length: 26572

---

> Average Elapsed Time: 11.15 seconds

> Average Cycle Length: 27406.3

# Iteration 6 (minimal with `mixed_elitist` with `mixed_elitism_proportion=0.3`)

> Average to beat: elapsed time is **10.22 seconds**, and best cycle length **26,879.7**.

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: None
- elimination: `mixed_elitist` with `mixed_elitism_proportion=0.3`
- insert diversity: None

---

- Elapsed time for solving TSP: 13.04 seconds
- Best individual cycle length: 26332

---

- Elapsed time for solving TSP: 10.51 seconds
- Best individual cycle length: 26221

---

- Elapsed time for solving TSP: 5.80 seconds
- Best individual cycle length: 28274

---

- Elapsed time for solving TSP: 9.74 seconds
- Best individual cycle length: 26331

---

- Elapsed time for solving TSP: 6.31 seconds
- Best individual cycle length: 26030

---

- Elapsed time for solving TSP: 8.28 seconds
- Best individual cycle length: 27226

---

- Elapsed time for solving TSP: 9.36 seconds
- Best individual cycle length: 26631

---

- Elapsed time for solving TSP: 9.59 seconds
- Best individual cycle length: 26305

---

- Elapsed time for solving TSP: 12.44 seconds
- Best individual cycle length: 26502

---

- Elapsed time for solving TSP: 9.49 seconds
- Best individual cycle length: 28138

---

> Average Elapsed Time: 9.46 seconds

> Average Cycle Length: 26799.0

!!! new best

## Iteration 7 (latest best iteration with `insert_diversity`)

> Average to beat: Cycle Length: 26799.0

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: None
- elimination: `mixed_elitist` with `mixed_elitism_proportion=0.3`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

- Elapsed time for solving TSP: 22.78 seconds
- Best individual cycle length: 27043

---

- Elapsed time for solving TSP: 12.08 seconds
- Best individual cycle length: 27024

---

- Elapsed time for solving TSP: 12.03 seconds
- Best individual cycle length: 28990

---

- Elapsed time for solving TSP: 10.93 seconds
- Best individual cycle length: 27177

---

- Elapsed time for solving TSP: 24.35 seconds
- Best individual cycle length: 29955

---

- Elapsed time for solving TSP: 20.09 seconds
- Best individual cycle length: 27969

---

- Elapsed time for solving TSP: 22.69 seconds
- Best individual cycle length: 27127

---

- Elapsed time for solving TSP: 27.44 seconds
- Best individual cycle length: 25890

---

- Elapsed time for solving TSP: 20.47 seconds
- Best individual cycle length: 28553

---

- Elapsed time for solving TSP: 21.36 seconds
- Best individual cycle length: 26003

---

> Average Elapsed Time: 19.42 seconds

> Average Cycle Length: 27573.1

## Iteration 8 (latest best iteration with `local_optimisation`)

> Average to beat: Cycle Length: 26799.0

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: `k_opt` with `proportion_worst=0.5`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `mixed_elitist` with `mixed_elitism_proportion=0.3`
- insert diversity: None

---

Elapsed time for solving TSP: 20.89 seconds
Best individual cycle length: 25589
Elapsed time for solving TSP: 13.77 seconds
Best individual cycle length: 28334
Elapsed time for solving TSP: 16.72 seconds
Best individual cycle length: 26560
Elapsed time for solving TSP: 15.31 seconds
Best individual cycle length: 26835
Elapsed time for solving TSP: 12.74 seconds
Best individual cycle length: 27136
Elapsed time for solving TSP: 15.33 seconds
Best individual cycle length: 26171
Elapsed time for solving TSP: 14.89 seconds
Best individual cycle length: 26261
Elapsed time for solving TSP: 12.08 seconds
Best individual cycle length: 28240
Elapsed time for solving TSP: 12.73 seconds
Best individual cycle length: 25966
Elapsed time for solving TSP: 16.59 seconds
Best individual cycle length: 26430
Elapsed time for solving TSP: 22.94 seconds
Best individual cycle length: 25927
Elapsed time for solving TSP: 14.87 seconds
Best individual cycle length: 25986
Elapsed time for solving TSP: 21.17 seconds
Best individual cycle length: 26652
Elapsed time for solving TSP: 17.72 seconds
Best individual cycle length: 28314
Elapsed time for solving TSP: 17.36 seconds
Best individual cycle length: 27960
Elapsed time for solving TSP: 20.72 seconds
Best individual cycle length: 27607
Elapsed time for solving TSP: 15.08 seconds
Best individual cycle length: 26778
Elapsed time for solving TSP: 11.35 seconds
Best individual cycle length: 25994
Elapsed time for solving TSP: 16.99 seconds
Best individual cycle length: 26859
Elapsed time for solving TSP: 13.48 seconds
Best individual cycle length: 28268

Average Elapsed Time: 17.17
Average Cycle Length: 27034.57
---

> Average Elapsed Time: 16.14 seconds

> Average Cycle Length: 26893.39

## Iteration 9 (latest best iteration with `elitisit_k_tournament_keep_s_best` elimination)

> Average to beat: Cycle Length: 26799.0

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: `k_opt` with `proportion_worst=0.5`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `elitisit_k_tournament_keep_s_best` with `elitisit_k_tournament_keep_s_best_k=3`,
  `elitisit_k_tournament_keep_s_best_s=5`
- insert diversity: None

---

Elapsed time for solving TSP: 27.43 seconds
Best individual cycle length: 26627
Elapsed time for solving TSP: 22.00 seconds
Best individual cycle length: 26970
Elapsed time for solving TSP: 29.09 seconds
Best individual cycle length: 26599
Elapsed time for solving TSP: 14.17 seconds
Best individual cycle length: 27000
Elapsed time for solving TSP: 25.12 seconds
Best individual cycle length: 26267
Elapsed time for solving TSP: 18.00 seconds
Best individual cycle length: 26141
Elapsed time for solving TSP: 32.84 seconds
Best individual cycle length: 28707
Elapsed time for solving TSP: 20.59 seconds
Best individual cycle length: 26555
Elapsed time for solving TSP: 12.03 seconds
Best individual cycle length: 28123
Elapsed time for solving TSP: 32.80 seconds
Best individual cycle length: 26235
Elapsed time for solving TSP: 19.43 seconds
Best individual cycle length: 27349
Elapsed time for solving TSP: 19.37 seconds
Best individual cycle length: 26166
Elapsed time for solving TSP: 27.60 seconds
Best individual cycle length: 25873
Elapsed time for solving TSP: 27.36 seconds
Best individual cycle length: 27134
Elapsed time for solving TSP: 30.62 seconds
Best individual cycle length: 28281
Elapsed time for solving TSP: 13.48 seconds
Best individual cycle length: 28274
Elapsed time for solving TSP: 12.83 seconds
Best individual cycle length: 26611
Elapsed time for solving TSP: 17.63 seconds
Best individual cycle length: 26147
Elapsed time for solving TSP: 16.51 seconds
Best individual cycle length: 28230
Elapsed time for solving TSP: 15.96 seconds
Best individual cycle length: 28073

---

> Average Elapsed Time: 21.75 seconds

> Average Cycle Length: 27068.11

## Iteration 10 (latest best iteration with `elitisit_k_tournament_keep_s_best` elimination)

> Average to beat: Cycle Length: 26799.0

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: None
- elimination: `elitisit_k_tournament_keep_s_best` with `elitisit_k_tournament_keep_s_best_k=3`,
  `elitisit_k_tournament_keep_s_best_s=5`
- insert diversity: None

---

Elapsed time for solving TSP: 18.97 seconds
Best individual cycle length: 27179
Elapsed time for solving TSP: 16.09 seconds
Best individual cycle length: 25986
Elapsed time for solving TSP: 11.61 seconds
Best individual cycle length: 28411
Elapsed time for solving TSP: 10.53 seconds
Best individual cycle length: 26407
Elapsed time for solving TSP: 7.91 seconds
Best individual cycle length: 28399
Elapsed time for solving TSP: 11.52 seconds
Best individual cycle length: 26922
Elapsed time for solving TSP: 10.31 seconds
Best individual cycle length: 26959
Elapsed time for solving TSP: 14.11 seconds
Best individual cycle length: 25746
Elapsed time for solving TSP: 15.53 seconds
Best individual cycle length: 27687
Elapsed time for solving TSP: 11.67 seconds
Best individual cycle length: 26754
Elapsed time for solving TSP: 15.63 seconds
Best individual cycle length: 26210
Elapsed time for solving TSP: 15.19 seconds
Best individual cycle length: 28016
Elapsed time for solving TSP: 10.42 seconds
Best individual cycle length: 26179
Elapsed time for solving TSP: 11.52 seconds
Best individual cycle length: 30216
Elapsed time for solving TSP: 9.26 seconds
Best individual cycle length: 26407
Elapsed time for solving TSP: 9.58 seconds
Best individual cycle length: 28077
Elapsed time for solving TSP: 14.86 seconds
Best individual cycle length: 28016
Elapsed time for solving TSP: 16.13 seconds
Best individual cycle length: 28621
Elapsed time for solving TSP: 11.67 seconds
Best individual cycle length: 28274
Elapsed time for solving TSP: 16.69 seconds
Best individual cycle length: 25950

---

> Average Elapsed Time: 12.96

> Average Cycle Length: 27320.83

## Iteration 11 (latest best iteration with `elitisit_k_tournament_keep_s_best` elimination and
`replace_worst_with_random` insert diversity)

> Average to beat: Cycle Length: 26799.0

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: None
- elimination: `elitisit_k_tournament_keep_s_best` with `elitisit_k_tournament_keep_s_best_k=3`,
  `elitisit_k_tournament_keep_s_best_s=5`
- insert diversity: `replace_worst_with_random` with `replace_worst_with_random_k=0.3`

---

Elapsed time for solving TSP: 15.68 seconds
Best individual cycle length: 26977
Elapsed time for solving TSP: 31.40 seconds
Best individual cycle length: 28093
Elapsed time for solving TSP: 14.01 seconds
Best individual cycle length: 27950
Elapsed time for solving TSP: 22.24 seconds
Best individual cycle length: 27691
Elapsed time for solving TSP: 15.53 seconds
Best individual cycle length: 26249
Elapsed time for solving TSP: 17.82 seconds
Best individual cycle length: 26756
Elapsed time for solving TSP: 23.36 seconds
Best individual cycle length: 29528
Elapsed time for solving TSP: 14.43 seconds
Best individual cycle length: 26736
Elapsed time for solving TSP: 28.01 seconds
Best individual cycle length: 26760
Elapsed time for solving TSP: 13.65 seconds
Best individual cycle length: 28830
Elapsed time for solving TSP: 14.40 seconds
Best individual cycle length: 28274
Elapsed time for solving TSP: 25.15 seconds
Best individual cycle length: 29313
Elapsed time for solving TSP: 13.35 seconds
Best individual cycle length: 28231
Elapsed time for solving TSP: 21.50 seconds
Best individual cycle length: 26448
Elapsed time for solving TSP: 18.98 seconds
Best individual cycle length: 26386
Elapsed time for solving TSP: 21.03 seconds
Best individual cycle length: 26770
Elapsed time for solving TSP: 14.12 seconds
Best individual cycle length: 26932
Elapsed time for solving TSP: 13.72 seconds
Best individual cycle length: 28189
Elapsed time for solving TSP: 16.21 seconds
Best individual cycle length: 28240
Elapsed time for solving TSP: 26.60 seconds
Best individual cycle length: 26500

---

> Average Elapsed Time: 19.06

> Average Cycle Length: 27542.65

meh

## Final iteration 

- selection: `k_tournament` with `k=3`
- recombination: `order_crossover`
- mutation: `reverse_subtour` with `alpha=0.1`
- local optimisation: `k_opt` with `proportion_worst=0.5`, `opt_probability=0.5`, `k_opt_pool_size=5`, `k_opt_k=2`
- elimination: `mixed_elitist` with `mixed_elitism_proportion=0.3`
- insert diversity: None