"""
Task B: Pendulum Experiment Analyzer (Functional Programming)
=============================================================

Analyze pendulum experiment data to determine gravitational
acceleration using pure functional programming.

Physics refresher:
  A simple pendulum's period is  T = 2π √(L / g)
  Rearranging to solve for g:    g = 4π² L / T²

Rules (follow these strictly!):
  - NO classes (use namedtuples for data only)
  - All functions must be PURE (no side effects, no mutation)
  - Use higher-order functions (map, filter, sorted, reduce)
  - Use function composition to build complex operations

Run with: python <your_name>.py
"""

from functools import reduce
from collections import namedtuple
import math


# ── Data (DO NOT MODIFY) ──────────────────────────────────

Trial = namedtuple("Trial", [
    "trial_id",
    "length_m",       # pendulum length in meters
    "num_swings",     # number of complete swings timed
    "total_time_s",   # total time for all swings
    "location",       # where the experiment was done
    "notes",          # observations during the trial
])

EXPERIMENT_DATA = [
    Trial(1,  1.00, 10, 20.10, "Lab A",   "clean"),
    Trial(2,  1.00, 10, 20.05, "Lab A",   "clean"),
    Trial(3,  1.00, 10, 20.08, "Lab A",   "clean"),
    Trial(4,  0.50, 10, 14.18, "Lab A",   "clean"),
    Trial(5,  0.50, 10, 14.22, "Lab A",   "clean"),
    Trial(6,  2.00, 10, 28.38, "Lab A",   "clean"),
    Trial(7,  2.00, 10, 28.42, "Lab A",   "clean"),
    Trial(8,  1.00, 10, 20.12, "Lab B",   "clean"),
    Trial(9,  1.00, 10, 20.50, "Lab B",   "door draft"),
    Trial(10, 0.25, 10, 10.04, "Lab B",   "clean"),
    Trial(11, 0.25, 10, 10.08, "Lab B",   "clean"),
    Trial(12, 1.00,  5, 10.80, "Rooftop", "windy"),
    Trial(13, 1.00,  5, 12.50, "Rooftop", "very windy"),
    Trial(14, 1.50, 10, 24.58, "Lab B",   "clean"),
    Trial(15, 1.50, 10, 24.62, "Lab B",   "clean"),
]

ACCEPTED_G = 9.81  # m/s²


# ============================================================
# TODO 1: period(trial) -> float
#
# Calculate the period of a single swing in seconds.
# Period = total_time / num_swings
#
# Example: Trial with 10 swings in 20.10s → period = 2.01s
# ============================================================

def period(trial):
    pass


# ============================================================
# TODO 2: calculate_g(trial) -> float
#
# Derive gravitational acceleration from a single trial.
#
# Formula: g = 4π²L / T²
#   where L = trial.length_m, T = period(trial)
#
# Use math.pi for π.
#
# Example: L=1.0m, T=2.01s → g ≈ 9.77 m/s²
# ============================================================

def calculate_g(trial):
    pass


# ============================================================
# TODO 3: trials_by_location(trials) -> dict
#
# Group trials by location. Return {"Lab A": [...], "Lab B": [...], ...}
#
# Use reduce to build the dictionary.
# Do NOT mutate — use {**acc, ...} to create new dicts
# and [*list, item] to create new lists.
#
# Hint:
#   reduce(
#       lambda acc, t: {**acc, t.location: [*acc.get(t.location, []), t]},
#       trials,
#       {},
#   )
# ============================================================

def trials_by_location(trials):
    pass


# ============================================================
# TODO 4: average_g(trials) -> float
#
# Calculate the mean g value across a list of trials.
# Use reduce to sum up g values — NOT a for loop or sum().
#
# Handle the empty list case (return 0.0).
# ============================================================

def average_g(trials):
    pass


# ============================================================
# TODO 5: create_filter(predicate) -> function
#
# Higher-order function: takes a predicate function and returns
# a NEW function that filters a list of trials.
#
# This is a FUNCTION that RETURNS A FUNCTION.
#
# Usage:
#   clean_only = create_filter(lambda t: t.notes == "clean")
#   clean_trials = clean_only(EXPERIMENT_DATA)
# ============================================================

def create_filter(predicate):
    pass


# ============================================================
# TODO 6: compose(*functions) -> function
#
# Function composition: chains functions right-to-left.
#   compose(f, g)(x) = f(g(x))
#   compose(f, g, h)(x) = f(g(h(x)))
#
# Use reduce to combine the functions.
#
# Usage:
#   clean_only = create_filter(lambda t: t.notes == "clean")
#   indoor_only = create_filter(lambda t: t.location != "Rooftop")
#   clean_indoor = compose(clean_only, indoor_only)
#   result = clean_indoor(EXPERIMENT_DATA)
# ============================================================

def compose(*functions):
    pass


# ============================================================
# TODO 7: Demo
#
# Print a full analysis:
#   1. Per-trial table: trial ID, length, period, calculated g
#      Flag trials where g is >5% off from ACCEPTED_G
#   2. Group by location, show avg g and error % for each
#   3. Use create_filter + compose to get only clean indoor trials
#   4. Show the filtered average g and its error vs ACCEPTED_G
#
# Example output:
#
#   Individual Trials:
#     ID   L (m)   T (s)    g (m/s²)
#     ——————————————————————————————————
#      1    1.00   2.010     9.7722
#      2    1.00   2.005     9.8213
#     ...
#     13    1.00   2.500     6.3165  ⚠
#
#   By Location:
#     Lab A    |  7 trials | avg g =  9.7991 | error: 0.1%
#     Lab B    |  6 trials | avg g =  9.6878 | error: 1.2%
#     Rooftop  |  2 trials | avg g =  7.3901 | error: 24.7%
#
#   Filtered (clean + indoor): 12 trials
#     Average g = 9.7925 m/s²
#     Accepted  = 9.81 m/s²
#     Error     = 0.18%
# ============================================================

def demo():
    pass


# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# PHASE 2: EXTENSION TODOs
# You're from the OOP group — now extend this FP code!
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

# ============================================================
# EXT 1: Add new experiment data
#
# Add 4 new Trial entries from a "Basement" lab to
# EXPERIMENT_DATA. Use realistic values:
#   - Various pendulum lengths (e.g., 0.75m, 1.25m)
#   - 10 swings each
#   - notes = "clean"
#   - Use T = 2π√(L/g) with g ≈ 9.81 to generate realistic
#     total times (add small random-ish variation)
#
# The new data should automatically appear in all analyses.
# ============================================================



# ============================================================
# EXT 2: Add standard deviation calculation
#
# Create: std_deviation_g(trials) -> float
#
# Formula: σ = √( Σ(gᵢ - ḡ)² / n )
#   where ḡ = average_g(trials), n = len(trials)
#
# Must use reduce — no for loops!
# Display std dev for each location in the demo output.
#
# Notice: adding a new FUNCTION doesn't require changing
#         anything that already exists. How does this feel
#         compared to OOP?
# ============================================================



# ============================================================
# EXT 3: Find the most precise location
#
# Create: most_precise_location(trials) -> str
#
# The most precise location has the lowest standard deviation
# of g across its trials.
#
# Steps:
#   1. Use trials_by_location() to group the data
#   2. Use std_deviation_g() on each group
#   3. Use min() with a key function to find the winner
#
# Print a precision ranking of all locations in the demo.
# ============================================================



if __name__ == "__main__":
    demo()
