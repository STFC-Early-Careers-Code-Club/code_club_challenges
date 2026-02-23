"""
Task B: Pendulum Experiment Analyzer (Functional Programming)
=============================================================

Analyze pendulum experiment data to determine gravitational
acceleration using pure functional programming.

Physics: T = 2π √(L / g)  →  g = 4π² L / T²

Run with: python task_b_fp.py
"""

from functools import reduce
from collections import namedtuple
import math


# ── Data ───────────────────────────────────────────────────

Trial = namedtuple("Trial", [
    "trial_id",
    "length_m",
    "num_swings",
    "total_time_s",
    "location",
    "notes",
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


# ── TODO 1 ─────────────────────────────────────────────────

def period(trial):
    """Calculate the period of a single swing in seconds."""
    return trial.total_time_s / trial.num_swings


# ── TODO 2 ─────────────────────────────────────────────────

def calculate_g(trial):
    """Derive gravitational acceleration from a trial.

    g = 4π²L / T²
    """
    t = period(trial)
    return (4 * math.pi ** 2 * trial.length_m) / (t ** 2)


# ── TODO 3 ─────────────────────────────────────────────────

def trials_by_location(trials):
    """Group trials by location using reduce. No mutation."""
    return reduce(
        lambda acc, t: {**acc, t.location: [*acc.get(t.location, []), t]},
        trials,
        {},
    )


# ── TODO 4 ─────────────────────────────────────────────────

def average_g(trials):
    """Calculate the mean g value from a list of trials using reduce."""
    if not trials:
        return 0.0
    total = reduce(lambda acc, t: acc + calculate_g(t), trials, 0.0)
    return total / len(trials)


# ── TODO 5 ─────────────────────────────────────────────────

def create_filter(predicate):
    """Higher-order function: returns a function that filters trials."""
    return lambda trials: list(filter(predicate, trials))


# ── TODO 6 ─────────────────────────────────────────────────

def compose(*functions):
    """Compose functions right-to-left: compose(f, g)(x) = f(g(x))."""
    return reduce(lambda f, g: lambda *args: f(g(*args)), functions)


# ── TODO 7: Demo ───────────────────────────────────────────

def demo():
    print("=" * 55)
    print("      PENDULUM EXPERIMENT ANALYSIS")
    print("=" * 55)

    # Per-trial results
    print(f"\n  {'ID':>4s}   {'L (m)':>6s}   {'T (s)':>7s}   {'g (m/s²)':>9s}   Location")
    print(f"  {'—' * 50}")
    for trial in EXPERIMENT_DATA:
        t = period(trial)
        g = calculate_g(trial)
        flag = " ⚠" if abs(g - ACCEPTED_G) / ACCEPTED_G > 0.05 else ""
        print(
            f"  {trial.trial_id:4d}   {trial.length_m:6.2f}   "
            f"{t:7.4f}   {g:9.4f}{flag}"
        )

    # By location
    print(f"\n  By Location:")
    print(f"  {'—' * 50}")
    grouped = trials_by_location(EXPERIMENT_DATA)
    for loc in sorted(grouped.keys()):
        trials = grouped[loc]
        avg = average_g(trials)
        error_pct = abs(avg - ACCEPTED_G) / ACCEPTED_G * 100
        print(
            f"    {loc:10s} | {len(trials):2d} trials | "
            f"avg g = {avg:.4f} m/s² | error: {error_pct:.1f}%"
        )

    # Filtered analysis using composition
    clean_only = create_filter(lambda t: t.notes == "clean")
    indoor_only = create_filter(lambda t: t.location != "Rooftop")
    clean_indoor = compose(clean_only, indoor_only)

    filtered = clean_indoor(EXPERIMENT_DATA)
    filtered_avg = average_g(filtered)
    error_pct = abs(filtered_avg - ACCEPTED_G) / ACCEPTED_G * 100

    print(f"\n  Filtered (clean + indoor): {len(filtered)} trials")
    print(f"    Average g = {filtered_avg:.4f} m/s²")
    print(f"    Accepted  = {ACCEPTED_G} m/s²")
    print(f"    Error     = {error_pct:.2f}%")

    print(f"\n{'=' * 55}")


# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
# PHASE 2 EXTENSIONS
# ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒

# ── EXT 1: New experiment data ─────────────────────────────

BASEMENT_DATA = [
    Trial(16, 0.75, 10, 17.38, "Basement", "clean"),
    Trial(17, 0.75, 10, 17.42, "Basement", "clean"),
    Trial(18, 1.25, 10, 22.42, "Basement", "clean"),
    Trial(19, 1.25, 10, 22.38, "Basement", "clean"),
]

ALL_DATA = [*EXPERIMENT_DATA, *BASEMENT_DATA]


# ── EXT 2: Standard deviation ─────────────────────────────

def std_deviation_g(trials):
    """Standard deviation of g values: σ = √(Σ(gᵢ - ḡ)² / n)."""
    if not trials:
        return 0.0
    mean = average_g(trials)
    sum_sq = reduce(
        lambda acc, t: acc + (calculate_g(t) - mean) ** 2,
        trials,
        0.0,
    )
    return math.sqrt(sum_sq / len(trials))


# ── EXT 3: Most precise location ──────────────────────────

def most_precise_location(trials):
    """Find location with lowest std deviation of g."""
    grouped = trials_by_location(trials)
    return min(grouped.keys(), key=lambda loc: std_deviation_g(grouped[loc]))


def demo_extensions():
    print("\n" + "=" * 55)
    print("      PHASE 2 EXTENSIONS")
    print("=" * 55)

    # Precision ranking
    grouped = trials_by_location(ALL_DATA)
    print(f"\n  Precision Ranking (by std deviation of g):")
    print(f"  {'—' * 50}")

    ranked = sorted(grouped.keys(), key=lambda loc: std_deviation_g(grouped[loc]))
    for i, loc in enumerate(ranked, 1):
        trials = grouped[loc]
        avg = average_g(trials)
        std = std_deviation_g(trials)
        print(
            f"    {i}. {loc:10s} | {len(trials):2d} trials | "
            f"avg g = {avg:.4f} | σ = {std:.4f} m/s²"
        )

    best = most_precise_location(ALL_DATA)
    print(f"\n  Most precise location: {best}")

    print(f"\n{'=' * 55}")


if __name__ == "__main__":
    demo()
    demo_extensions()
