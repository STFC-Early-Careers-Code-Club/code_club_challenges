# MPI Code Challenge: Distributed Pi Calculation

## Overview

In this challenge, you'll use MPI to calculate the value of Pi using a Monte Carlo simulation distributed across multiple processes.

## The Problem

The Monte Carlo method estimates Pi by randomly throwing "darts" at a square with a quarter circle inscribed in it. The ratio of darts landing inside the quarter circle to total darts approximates Pi/4.

```
  1 +-------------+
    |   *  *      |
    | *      *    |
    |*   *     *  |
    |*      *     |
    | *  *     *  |
    |   *    *    |
  0 +-------------+
    0             1
```

**Formula:** `Pi ≈ 4 * (points inside circle) / (total points)`

## Your Task

Complete the skeleton code in `challenge.py` to:

1. **Initialize MPI** - Set up the MPI environment
2. **Distribute the work** - Each process should generate its share of random points
3. **Count local hits** - Each process counts how many of its points fall inside the quarter circle
4. **Reduce results** - Use MPI to gather all local counts and calculate the final Pi estimate
5. **Print the result** - Only rank 0 should print the final answer

## Running the Code

```bash
# Run with 4 processes
mpirun -n 4 python challenge.py

# Or using mpiexec
mpiexec -n 4 python challenge.py
```

## Expected Output

```
Estimated Pi = 3.14159... (using 1000000 total points across 4 processes)
```

## Hints

- `comm.Get_rank()` returns the process ID (0, 1, 2, ...)
- `comm.Get_size()` returns the total number of processes
- `comm.reduce(local_value, op=MPI.SUM, root=0)` sums values from all processes
- A point (x, y) is inside the quarter circle if `x² + y² <= 1`

## Bonus Challenges

1. Time the computation and see how speedup scales with more processes
2. Have each process print its local estimate before the final reduction
3. Use `comm.Reduce()` (capital R) with numpy arrays for better performance

Good luck!
