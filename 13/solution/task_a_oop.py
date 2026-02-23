"""
Task A: Projectile Motion Simulator (OOP with SOLID Principles)
===============================================================

Simulate projectile trajectories across different planets using
Object-Oriented Programming and SOLID principles.

Run with: python task_a_oop.py
"""

from abc import ABC, abstractmethod
import math


# ── Provided: Vector2D (immutable) ─────────────────────────

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


# ── TODO 1: Projectile ABC ────────────────────────────────

class Projectile(ABC):
    def __init__(self, launch_speed: float, launch_angle_deg: float):
        self._launch_speed = launch_speed
        self._launch_angle = launch_angle_deg
        angle_rad = math.radians(launch_angle_deg)
        self._initial_velocity = Vector2D(
            launch_speed * math.cos(angle_rad),
            launch_speed * math.sin(angle_rad),
        )

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    def launch_speed(self) -> float:
        return self._launch_speed

    @property
    def launch_angle(self) -> float:
        return self._launch_angle

    @property
    def initial_velocity(self) -> Vector2D:
        return self._initial_velocity


# ── TODO 2: Concrete Projectiles ──────────────────────────

class Baseball(Projectile):
    def __init__(self):
        super().__init__(launch_speed=40.0, launch_angle_deg=45.0)

    @property
    def name(self) -> str:
        return "Baseball"


class Cannonball(Projectile):
    def __init__(self):
        super().__init__(launch_speed=100.0, launch_angle_deg=35.0)

    @property
    def name(self) -> str:
        return "Cannonball"


class GolfBall(Projectile):
    def __init__(self):
        super().__init__(launch_speed=70.0, launch_angle_deg=30.0)

    @property
    def name(self) -> str:
        return "Golf Ball"


# ── TODO 3: GravityModel ABC + Planets ────────────────────

class GravityModel(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def g(self) -> float:
        pass

    def acceleration(self) -> Vector2D:
        return Vector2D(0, -self.g)


class Earth(GravityModel):
    @property
    def name(self) -> str:
        return "Earth"

    @property
    def g(self) -> float:
        return 9.81


class Moon(GravityModel):
    @property
    def name(self) -> str:
        return "Moon"

    @property
    def g(self) -> float:
        return 1.62


class Mars(GravityModel):
    @property
    def name(self) -> str:
        return "Mars"

    @property
    def g(self) -> float:
        return 3.72


# ── TODO 4: Simulator ─────────────────────────────────────

class Simulator:
    def __init__(self, gravity_model: GravityModel, dt: float = 0.01):
        self._gravity = gravity_model
        self._dt = dt

    def simulate(self, projectile: Projectile) -> list:
        pos = Vector2D(0.0, 0.0)
        vel = projectile.initial_velocity
        acc = self._gravity.acceleration()
        t = 0.0
        trajectory = [(t, pos)]

        while pos.y >= 0 or t < self._dt:
            vel = vel.add(acc.scale(self._dt))
            pos = pos.add(vel.scale(self._dt))
            t += self._dt
            trajectory.append((t, pos))

            if t > 10000:
                break

        return trajectory

    @staticmethod
    def summarize(projectile: Projectile, trajectory: list) -> dict:
        max_height = max(p.y for _, p in trajectory)
        range_x = trajectory[-1][1].x
        flight_time = trajectory[-1][0]
        return {
            "name": projectile.name,
            "max_height_m": max_height,
            "range_m": range_x,
            "flight_time_s": flight_time,
        }


# ── TODO 5: Demo ──────────────────────────────────────────

def demo():
    projectiles = [Baseball(), Cannonball(), GolfBall()]
    planets = [Earth(), Moon(), Mars()]

    print("=" * 62)
    print("         PROJECTILE MOTION SIMULATOR")
    print("=" * 62)

    for planet in planets:
        sim = Simulator(planet)
        print(f"\n  {planet.name} (g = {planet.g} m/s²)")
        print(f"  {'—' * 56}")

        for proj in projectiles:
            trajectory = sim.simulate(proj)
            result = Simulator.summarize(proj, trajectory)
            print(
                f"    {result['name']:12s} | "
                f"Height: {result['max_height_m']:8.1f} m | "
                f"Range: {result['range_m']:9.1f} m | "
                f"Time: {result['flight_time_s']:6.1f} s"
            )

    print(f"\n{'=' * 62}")


if __name__ == "__main__":
    demo()
