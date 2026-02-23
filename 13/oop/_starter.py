"""
Task A: Projectile Motion Simulator (OOP with SOLID Principles)
===============================================================

Simulate projectile trajectories across different planets using
Object-Oriented Programming and SOLID principles.

Physics refresher:
  - In a vacuum, the only force is gravity: F = mg (downward)
  - Euler method: update velocity and position each time step
      v_new = v_old + a * dt
      p_new = p_old + v * dt
  - Initial velocity from speed + angle:
      vx = speed * cos(angle)
      vy = speed * sin(angle)

Run with: python <your_name>.py
"""

from abc import ABC, abstractmethod
import math


# ── Provided: Vector2D (immutable) ─────────────────────────
# All operations return NEW vectors — nothing is mutated.

class Vector2D:
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x

    @property
    def y(self) -> float:
        return self._y

    def add(self, other: "Vector2D") -> "Vector2D":
        return Vector2D(self._x + other.x, self._y + other.y)

    def scale(self, scalar: float) -> "Vector2D":
        return Vector2D(self._x * scalar, self._y * scalar)

    def magnitude(self) -> float:
        return math.sqrt(self._x ** 2 + self._y ** 2)

    def __repr__(self) -> str:
        return f"({self._x:.2f}, {self._y:.2f})"


# ============================================================
# TODO 1: Projectile (Abstract Base Class)
#
# Create an abstract class with:
#   - __init__(launch_speed: float, launch_angle_deg: float)
#     Store speed, angle, and compute initial_velocity as a
#     Vector2D using the trig formulas above.
#   - Abstract property: name -> str
#   - Properties: launch_speed, launch_angle, initial_velocity
#
# SOLID (DIP): Other code depends on this abstraction,
#              not on concrete projectile types.
# ============================================================



# ============================================================
# TODO 2: Concrete Projectile classes
#
# Create three classes that inherit from Projectile.
# Each hardcodes a typical launch configuration:
#
#   Baseball:    speed=40 m/s,   angle=45°
#   Cannonball:  speed=100 m/s,  angle=35°
#   GolfBall:    speed=70 m/s,   angle=30°
#
# Each class only needs __init__ (calling super) and the
# name property. That's it — the parent does the heavy lifting.
#
# SOLID (OCP): Adding a new projectile = adding a new class.
#              No existing code changes.
# SOLID (LSP): Any subclass works wherever Projectile is expected.
# ============================================================



# ============================================================
# TODO 3: GravityModel (Abstract) + Planet classes
#
# Abstract GravityModel with:
#   - Abstract properties: name -> str, g -> float
#   - Concrete method: acceleration() -> Vector2D
#     Returns Vector2D(0, -self.g)
#
# Then create three planet classes:
#   Earth:  g = 9.81 m/s²
#   Moon:   g = 1.62 m/s²
#   Mars:   g = 3.72 m/s²
#
# SOLID (OCP): New planet = new class, nothing else changes.
# SOLID (DIP): Simulator depends on GravityModel, not Earth/Moon/etc.
# ============================================================



# ============================================================
# TODO 4: Simulator class
#
# __init__(gravity_model: GravityModel, dt: float = 0.01)
#
# simulate(projectile: Projectile) -> list of (time, Vector2D):
#   Start at pos=(0,0), vel=projectile.initial_velocity
#   Each step:
#     vel = vel.add(acceleration.scale(dt))
#     pos = pos.add(vel.scale(dt))
#     t += dt
#   Stop when pos.y < 0 (hit the ground)
#   Return the full trajectory as [(t, pos), ...]
#
# summarize(projectile, trajectory) -> dict:
#   Return {"name", "max_height_m", "range_m", "flight_time_s"}
#
# SOLID (SRP): Simulator does ONE thing — runs simulations.
#              It doesn't know what a Baseball or Earth is.
# ============================================================



# ============================================================
# TODO 5: Demo
#
# 1. Create one of each projectile (Baseball, Cannonball, GolfBall)
# 2. Create one of each planet (Earth, Moon, Mars)
# 3. For each planet, simulate every projectile
# 4. Print a formatted results table like:
#
#   Earth (g = 9.81 m/s²)
#   ——————————————————————————————————————————————————
#     Baseball     | Height:   40.8 m | Range:  163.1 m | Time:  5.8 s
#     Cannonball   | Height:  168.0 m | Range:  919.7 m | Time: 11.7 s
#     Golf Ball    | Height:   62.5 m | Range:  432.8 m | Time:  7.1 s
# ============================================================

def demo():
    pass


if __name__ == "__main__":
    demo()
