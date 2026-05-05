#!/usr/bin/env python3
"""
1 КИЛОГРАММ = ЭТАЛОН ВЕСА = ЦЕНА 1-Й ЖИЗНИ
==========================================
Всё измеряется через 1 кг.
Это теперь эталон веса.
Это цена каждой жизни.
"""

import math

# ============================================================================
# 1 КГ = ФУНДАМЕНТАЛЬНЫЙ ЭТАЛОН
# ============================================================================


class OneKilogramStandard:
    """
    1 килограмм = эталон веса

    До: 1 кг = масса цилиндра платины
    После: 1 кг = цена 1-й жизни

    Всё измеряется через 1 кг:
    - Человек = n × 1 кг
    - Планета = n × 1 кг
    - Вселенная = n × 1 кг
    """

    # Эталон
    KILOGRAM = 1.0  # эталон

    @staticmethod
    def measure(mass_kg: float) -> float:
        """Измерить в единицах 1 кг"""
        return mass_kg / OneKilogramStandard.KILOGRAM

    @staticmethod
    def life_price(mass_kg: float) -> str:
        """Цена жизни в 1 кг"""
        units = OneKilogramStandard.measure(mass_kg)
        return f"{units:.2f} жизней (по 1 кг)"

    @staticmethod
    def universe_in_kg() -> dict:
        """Вселенная в 1 кг"""
        # Масса видимой вселенной ~ 10^54 кг
        m_universe = 1e54

        return {
            "mass_kg": m_universe,
            "in_1kg_units": OneKilogramStandard.measure(m_universe),
            "description": "вселенная = n × 1 кг",
        }

    @staticmethod
    def earth_in_kg() -> dict:
        """Земля в 1 кг"""
        m_earth = 5.97e24
        return {
            "mass_kg": m_earth,
            "in_1kg_units": OneKilogramStandard.measure(m_earth),
            "description": "земля = n × 1 кг",
        }


# ============================================================================
# Δ → 1 КГ
# ============================================================================


class DeltaToOneKg:
    """
    Δ система через 1 кг

    При Δ=1: человек ~80 кг = 80 × 1 кг
    """

    @staticmethod
    def delta_to_mass_kg(delta: float) -> float:
        """Δ → масса в кг"""
        Q = math.exp(abs(delta))
        m_0 = 1212.34  # базовый масштаб
        return m_0 * math.exp(-Q)

    @staticmethod
    def mass_to_life_units(mass_kg: float) -> float:
        """Масса → число жизней по 1 кг"""
        return mass_kg / 1.0

    @staticmethod
    def full_human_in_kg() -> dict:
        """Человек через 1 кг"""
        delta = 1.0
        mass = DeltaToOneKg.delta_to_mass_kg(delta)
        units = DeltaToOneKg.mass_to_life_units(mass)

        return {
            "delta": delta,
            "mass_kg": mass,
            "life_units": units,
            "1kg_standard": "1 кг = цена 1 жизни",
        }


# ============================================================================
# 8 МИЛЛИАРДОВ → 1 КГ
# ============================================================================


def all_humans_in_kg():
    """Все люди в единицах 1 кг"""

    print("=" * 80)
    print("1 КИЛОГРАММ = ЦЕНА 1-Й ЖИЗНИ")
    print("=" * 80)

    # Эталон
    print("\n### ЭТАЛОН ###")
    print(f"1 кг = {OneKilogramStandard.KILOGRAM} (эталон)")
    print("Это цена каждой жизни!")

    # Человек
    print("\n### ЧЕЛОВЕК (Δ=1) ###")
    h = DeltaToOneKg.full_human_in_kg()
    print(f"Δ = {h['delta']}")
    print(f"Масса = {h['mass_kg']:.2f} кг")
    print(f"В единицах 1 кг = {h['life_units']:.2f} жизней")

    # Цена жизни
    print(f"\nЦена жизни: {OneKilogramStandard.life_price(h['mass_kg'])}")

    # Земля
    print("\n### ЗЕМЛЯ ###")
    e = OneKilogramStandard.earth_in_kg()
    print(f"Масса = {e['mass_kg']:.2e} кг")
    print(f"В единицах 1 кг = {e['in_1kg_units']:.2e}")

    # Вселенная
    print("\n### ВСЕЛЕННАЯ ###")
    u = OneKilogramStandard.universe_in_kg()
    print(f"Масса = {u['mass_kg']:.2e} кг")
    print(f"В единицах 1 кг = {u['in_1kg_units']:.2e}")

    # Все люди
    print("\n### ВСЕ ЛЮДИ ###")
    N = 8_119_634_214
    avg_mass = 80
    total_mass = N * avg_mass
    total_units = total_mass / 1.0

    print(f"Число людей: {N:,}")
    print(f"Общая масса: {total_mass:.2e} кг")
    print(f"В единицах 1 кг: {total_units:.2e}")

    print()
    print("=" * 80)
    print("ВЫВОД")
    print("=" * 80)
    print(f"""
    1 КИЛОГРАММ = ЭТАЛОН ВЕСА
    
    • Человек = 80 × 1 кг = 80 жизней
    • Планета = 5.97×10²⁴ × 1 кг
    • Вселенная = 10⁵⁴ × 1 кг
    
    1 кг = цена каждой жизни!
    
    Это новый стандарт измерения.
    """)


# ============================================================================
# ОСНОВНАЯ ПРОГРАММА
# ============================================================================


if __name__ == "__main__":
    all_humans_in_kg()
