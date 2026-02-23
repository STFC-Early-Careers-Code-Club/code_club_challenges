# Python Code Challenge: OOP vs Functional Programming

## The Experiment

Which paradigm makes code easier to extend — **Object-Oriented** or **Functional**?

We'll find out empirically. Half the group builds something in OOP, the other half in FP. Then you swap codebases and try to extend someone else's work.

## Session Flow

### Phase 1: Build

The group splits in half:

| Group | Task | Folder |
|-------|------|--------|
| **OOP** | Projectile Motion Simulator | `oop/` |
| **FP**  | Pendulum Experiment Analyzer | `functional/` |

Each person works in their own file (e.g., `oop/kiran.py`, `functional/george.py`).

### Phase 2: Extend 

Swap! Each person picks a file from the **other** folder and extends it:

- **OOP people** → pick a file from `functional/` and extend it
- **FP people** → pick a file from `oop/` and extend it

You can extend however you want — add features, change the design, mix paradigms. See the [Extension Ideas](#extension-ideas) section for inspiration.

### Phase 3: Discuss (10 minutes)

Compare experiences. See [Discussion Questions](#discussion-questions).

## Facilitator Setup

Before the session, create named copies of the starters:

```bash
# OOP group
cp oop/_starter.py oop/alice.py
cp oop/_starter.py oop/bob.py
# ... one per participant

# FP group
cp functional/_starter.py functional/charlie.py
cp functional/_starter.py functional/dave.py
# ... one per participant
```

The `.vsls.json` hides the `solution/` folder from Live Share participants.

## Task A: Projectile Motion Simulator (OOP)

Simulate projectile trajectories across different planets using classes, abstract base classes, and the Strategy pattern.

**Physics:** In a vacuum, projectiles follow parabolic paths governed by gravity. The same baseball launched on Earth, Moon, and Mars will fly very differently.

**What you'll build:**
1. `Projectile` abstract class + concrete types (Baseball, Cannonball, GolfBall)
2. `GravityModel` abstract class + planet implementations (Earth, Moon, Mars)
3. `Simulator` class that runs Euler method integration
4. Demo that prints a comparison table

**SOLID principles in action:**
- **SRP:** Each class has one job
- **OCP:** New projectile or planet = new class, no existing code changes
- **LSP:** Any `Projectile` subclass works wherever `Projectile` is expected
- **DIP:** `Simulator` depends on `GravityModel` abstraction, not `Earth`/`Moon`/`Mars`

**Expected output:**
```
==============================================================
         PROJECTILE MOTION SIMULATOR
==============================================================

  Earth (g = 9.81 m/s²)
  ————————————————————————————————————————————————————————
    Baseball     | Height:     40.6 m | Range:     162.9 m | Time:    5.8 s
    Cannonball   | Height:    167.4 m | Range:     957.6 m | Time:   11.7 s
    Golf Ball    | Height:     62.3 m | Range:     432.2 m | Time:    7.1 s

  Moon (g = 1.62 m/s²)
  ————————————————————————————————————————————————————————
    Baseball     | Height:    246.8 m | Range:     987.4 m | Time:   34.9 s
    ...
```

## Task B: Pendulum Experiment Analyzer (FP)

Analyze real-ish pendulum experiment data to determine gravitational acceleration using pure functions, higher-order functions, and function composition.

**Physics:** A simple pendulum's period is `T = 2π√(L/g)`. By measuring the period and knowing the length, you can solve for `g = 4π²L / T²`. Some trials have bad data (windy rooftop, door drafts) — your pipeline should filter those out.

**What you'll build:**
1. `period()` and `calculate_g()` — pure computation functions
2. `trials_by_location()` — grouping with `reduce` (no mutation!)
3. `average_g()` — statistical aggregation with `reduce`
4. `create_filter()` — higher-order function that returns a filter function
5. `compose()` — function composition to chain operations
6. Demo that shows per-trial results, location breakdown, and filtered analysis

**FP principles in action:**
- **Purity:** Every function takes input, returns output, no side effects
- **Immutability:** `{**dict}` and `[*list]` spreads instead of mutation
- **Higher-order functions:** Functions that take/return functions
- **Composition:** Build complex operations from simple ones

**Expected output:**
```
=======================================================
      PENDULUM EXPERIMENT ANALYSIS
=======================================================

    ID    L (m)     T (s)    g (m/s²)   Location
  ——————————————————————————————————————————————————
     1     1.00    2.0100      9.7716
     2     1.00    2.0050      9.8204
    ...
    13     1.00    2.5000      6.3165 ⚠

  By Location:
  ——————————————————————————————————————————————————
    Lab A      |  7 trials | avg g = 9.7915 m/s² | error: 0.2%
    Lab B      |  6 trials | avg g = 9.7036 m/s² | error: 1.1%
    Rooftop    |  2 trials | avg g = 7.3891 m/s² | error: 24.7%

  Filtered (clean + indoor): 12 trials
    Average g = 9.7807 m/s²
    Accepted  = 9.81 m/s²
    Error     = 0.30%
```

## Phase 2: Extension Tasks

Each side gets 3 parallel TODOs (already in the starter files). The tasks are equivalent so you can compare the experience directly.

| # | What | On Projectile (OOP) | On Pendulum (FP) |
|---|------|---------------------|-------------------|
| EXT 1 | Add new data | Add Jupiter (g = 24.79 m/s²) as a new planet class | Add 4 new Trial entries from a "Basement" lab |
| EXT 2 | Add new operation | Add `mass_kg` property to all projectiles + launch energy (KE = 0.5mv²) | Add `std_deviation_g(trials)` function using reduce |
| EXT 3 | Add analysis | Find optimal launch angle (max range) for each projectile/planet combo | Find the most precise location (lowest std dev) |

**Pay attention to the friction:**
- **EXT 1** tests adding a new *variant*. In OOP this is just a new class. In FP you add data to the list. Both are easy — but notice the difference in how it's done.
- **EXT 2** tests adding a new *operation across all types*. In FP this is just a new function. In OOP you have to modify the abstract base class AND every subclass. This is the **Expression Problem** in action.
- **EXT 3** ties it all together with an analytical feature.

## Running Your Code

```bash
python3 oop/<your_name>.py
python3 functional/<your_name>.py
```

## Hints

### OOP (Task A)
- `from abc import ABC, abstractmethod` for abstract classes
- Use `@property` + `@abstractmethod` together for abstract properties
- `super().__init__(...)` calls the parent constructor
- `math.radians()`, `math.cos()`, `math.sin()` for the trig

### FP (Task B)
- `from functools import reduce` — `reduce(fn, iterable, initial)`
- `{**old_dict, key: value}` creates a new dict (no mutation)
- `[*old_list, item]` creates a new list (no mutation)
- `lambda` for inline functions: `lambda x: x + 1`
- A function returning a function: `def outer(): return lambda x: x`

## Discussion Questions

1. **Understanding:** How quickly could you understand the other group's code? What helped or hindered?
2. **Adding types:** How easy was it to add a new projectile/planet (OOP) vs a new trial type (FP)?
3. **Adding operations:** How easy was it to add a new calculation across all types?
4. **The Expression Problem:** OOP makes it easy to add new *types* but hard to add new *operations*. FP makes it easy to add new *operations* but hard to add new *types*. Did you experience this?
5. **Mixing paradigms:** Did anyone blend OOP and FP in their extension? How did it go?
6. **Real-world trade-off:** When would you reach for OOP vs FP in a real project?

Good luck!
