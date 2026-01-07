"""
MPI Code Challenge: Distributed Monte Carlo Pi Calculation
===========================================================

Complete the TODOs below to calculate Pi using MPI!

Run with: mpirun -n 4 python challenge.py
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
    comm = None  # Get the MPI communicator
    rank = None  # Get this process's rank (ID)
    size = None  # Get the total number of processes

    # ===========================================
    # TODO 2: Calculate how many points this process should generate
    # Divide the work evenly among all processes
    # ===========================================
    points_per_process = None  # How many points should each process handle?

    # ===========================================
    # TODO 3: Generate random points and count hits
    # A "hit" is when the point falls inside the quarter circle
    # ===========================================
    local_hits = 0

    for _ in range(points_per_process):
        x = random.random()  # Random float between 0 and 1
        y = random.random()
        # TODO: Check if point is inside circle and increment local_hits
        pass

    # ===========================================
    # TODO 4: Use MPI to sum up all local_hits from every process
    # The result should only be stored on rank 0
    # ===========================================
    total_hits = None  # Use comm.reduce() to sum all local_hits

    # ===========================================
    # TODO 5: Calculate and print Pi (only on rank 0)
    # Remember: Pi ≈ 4 * (hits inside circle) / (total points)
    # ===========================================
    if rank == 0:
        # TODO: Calculate pi_estimate and print it
        pass


if __name__ == "__main__":
    main()
