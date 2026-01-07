"""
MPI Code Challenge: SOLUTION
============================

This is the completed solution for the Monte Carlo Pi calculation.

Run with: mpirun -n 4 python solution.py
"""

from mpi4py import MPI
import random

# Total number of random points to generate (across all processes)
TOTAL_POINTS = 1_000_000


def is_inside_circle(x: float, y: float) -> bool:
    """Check if a point (x, y) is inside the quarter circle of radius 1."""
    return x * x + y * y <= 1


def main():
    # ===========================================
    # TODO 1: Initialize MPI
    # Get the communicator, rank, and size
    # ===========================================
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # ===========================================
    # TODO 2: Calculate how many points this process should generate
    # Divide the work evenly among all processes
    # ===========================================
    points_per_process = TOTAL_POINTS // size

    # ===========================================
    # TODO 3: Generate random points and count hits
    # A "hit" is when the point falls inside the quarter circle
    # ===========================================
    local_hits = 0

    for _ in range(points_per_process):
        x = random.random()
        y = random.random()
        if is_inside_circle(x, y):
            local_hits += 1

    # ===========================================
    # TODO 4: Use MPI to sum up all local_hits from every process
    # The result should only be stored on rank 0
    # ===========================================
    total_hits = comm.reduce(local_hits, op=MPI.SUM, root=0)

    # ===========================================
    # TODO 5: Calculate and print Pi (only on rank 0)
    # Remember: Pi ≈ 4 * (hits inside circle) / (total points)
    # ===========================================
    if rank == 0:
        total_points = points_per_process * size
        pi_estimate = 4.0 * total_hits / total_points
        print(f"Estimated Pi = {pi_estimate:.6f} (using {total_points:,} total points across {size} processes)")
        print(f"Actual Pi    = 3.141593...")
        print(f"Error        = {abs(pi_estimate - 3.141592653589793):.6f}")


if __name__ == "__main__":
    main()
