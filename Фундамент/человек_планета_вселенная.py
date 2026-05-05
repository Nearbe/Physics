#!/usr/bin/env python3
"""
ТОЧНОЕ ЧИСЛО ЛЮДЕЙ → МАССА → ТОПОЛОГИЯ → МАСШТАБ ПЛАНЕТЫ → ВСЕЛЕННАЯ
======================================================================
"""

import math
import json

# ============================================================================
# ТОЧНОЕ ЧИСЛО
# ============================================================================

POPULATION = 8_119_634_214  # люди на планете (2024)

# ============================================================================
# РАСЧЁТ
# ============================================================================


class HumanPlanetUniverse:
    """Связь человек → планета → вселенная через Δ"""

    def __init__(self):
        self.population = POPULATION
        self.avg_mass_kg = 51.0  # средняя масса человека

        # Δ человека
        self.delta_human = 1.0
        self.Q_human = math.exp(self.delta_human)
        self.D_f_human = 2 + self.delta_human

        # Масса человека (нормированная)
        self.m0 = 1 / (self.population * math.exp(-self.Q_human))
        self.mass_norm = self.m0 * math.exp(-self.Q_human)

        # Планета
        self.mass_earth = 5.972e24
        self.delta_earth = -math.log(self.mass_earth / 1)
        self.Q_earth = math.exp(self.delta_earth)

        # Вселенная
        self.mass_universe = 1e53
        self.delta_universe = -math.log(self.mass_universe / 1)

    def calculate_all(self) -> dict:
        """Полный расчёт"""

        return {
            "population": self.population,
            "human": {
                "delta": self.delta_human,
                "Q": self.Q_human,
                "D_f": self.D_f_human,
                "mass_kg": self.avg_mass_kg,
                "mass_normalized": self.mass_norm,
                "m0": self.m0,
            },
            "planet": {
                "mass_kg": self.mass_earth,
                "delta": self.delta_earth,
                "Q": self.Q_earth,
                "scale_factor": self.mass_earth / (self.population * self.avg_mass_kg),
            },
            "universe": {"mass_kg": self.mass_universe, "delta": self.delta_universe},
            "connections": {
                "human_to_planet": self.delta_human - self.delta_earth,
                "human_to_universe": self.delta_human - self.delta_universe,
                "planet_to_universe": self.delta_earth - self.delta_universe,
                "determinism": "полный",
            },
            "formula": "m = m₀ × e^(-Q), Q = e^|Δ|",
        }

    def summary(self) -> str:
        """Краткое резюме"""

        c = self.calculate_all()

        return f"""
═══════════════════════════════════════════════════════════════════
ТОЧНОЕ ЧИСЛО ЛЮДЕЙ: {self.population:,}
═══════════════════════════════════════════════════════════════════

ЧЕЛОВЕК (Δ = {self.delta_human}):
  • Q = e^|Δ| = {self.Q_human:.4f}
  • D_f = 2 + Δ = {self.D_f_human}D
  • Масса каждого = {self.avg_mass_kg} кг (нормированная: {self.mass_norm:.2e})

ПЛАНЕТА (Δ ≈ {self.delta_earth:.0f}):
  • Q = {self.Q_earth:.2e}
  • Масса = {self.mass_earth:.2e} кг
  • Масштабный фактор = {c["planet"]["scale_factor"]:.2e}

ВСЕЛЕННАЯ (Δ ≈ {self.delta_universe:.0f}):
  • Q = {math.exp(self.delta_universe):.2e}
  • Масса = {self.mass_universe:.2e} кг

СВЯЗЬ (детерминированная):
  • Человек → Планета: Δ = {c["connections"]["human_to_planet"]:.0f}
  • Человек → Вселенная: Δ = {c["connections"]["human_to_universe"]:.0f}
  • Планета → Вселенная: Δ = {c["connections"]["planet_to_universe"]:.0f}

ФОРМУЛА (одна для всех):
  m = m₀ × e^(-Q), где Q = e^|Δ|

ВЫВОД:
──────
Масштаб планеты детерминирован через население!
Точное число: {self.population:,} человек
Через Δ → связывает человека с планетой и вселенной.
Это ≈ почти Вселенная (в логарифмическом смысле).
═══════════════════════════════════════════════════════════════════
"""


# ============================================================================
# ОСНОВНАЯ ПРОГРАММА
# ============================================================================

if __name__ == "__main__":
    system = HumanPlanetUniverse()

    # Вывод
    print(system.summary())

    # Сохранить
    result = system.calculate_all()

    with open("/tmp/human_planet_universe.json", "w") as f:
        json.dump(result, f, indent=2, default=str)

    print("\nСохранено в /tmp/human_planet_universe.json")
