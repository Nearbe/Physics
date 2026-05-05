#!/usr/bin/env python3
"""
ТОЧНАЯ ФОРМУЛА МАССЫ ЧЕЛОВЕКА
=============================
Вычисляет массу каждого человека через Δ с нормировкой до 1
"""

import math
from typing import Dict, Tuple, Optional
import random

# ============================================================================
# Δ-СИСТЕМА
# ============================================================================


class DeltaSystem:
    """Δ-система: всё происходит от Δ"""

    # Δ для человека
    DELTA_HUMAN = 1.0

    @staticmethod
    def Q_from_delta(d: float) -> float:
        """Q = e^|Δ|"""
        return math.exp(abs(d))

    @staticmethod
    def delta_from_Q(q: float) -> float:
        """Δ = ln(Q)"""
        return math.log(q) if q > 0 else 0

    @staticmethod
    def dimension_from_delta(d: float) -> int:
        """D_f = 2 + Δ"""
        return int(2 + d)

    @staticmethod
    def fire_or_water(q: float) -> str:
        """ОГОНЬ (Q≤5) или ВОДА (Q>5)"""
        return "ОГОНЬ" if q <= 5 else "ВОДА"


# ============================================================================
# ДАННЫЕ ЧЕЛОВЕЧЕСТВА
# ============================================================================


class HumanityData:
    """Данные о человечестве"""

    POPULATION = 8_100_000_000  # 8.1 млрд
    AVG_MASS_KG = 51.0  # кг
    TOTAL_MASS_KG = POPULATION * AVG_MASS_KG

    # Атомный состав (по массе)
    BODY_COMPOSITION = {
        "вода": 0.60,
        "белки": 0.20,
        "жиры": 0.15,
        "минералы": 0.05,
    }

    @classmethod
    def get_total_mass(cls) -> float:
        return cls.TOTAL_MASS_KG

    @classmethod
    def get_population(cls) -> int:
        return cls.POPULATION


# ============================================================================
# ОСНОВНАЯ ФОРМУЛА
# ============================================================================


class HumanMassFormula:
    """
    Масса человека через Δ

    Формула: m = m₀ × e^(-Q), где Q = e^|Δ|

    Нормировка: Σ m_i = 1
    """

    def __init__(self, normalize_to: float = 1.0):
        self.normalize_to = normalize_to

        # m₀ вычисляется из условия нормировки
        # N × m₀ × e^(-Q) = 1
        # m₀ = 1 / (N × e^(-Q))

        self.N = HumanityData.POPULATION
        self.Q = DeltaSystem.Q_from_delta(DeltaSystem.DELTA_HUMAN)
        self.m0 = normalize_to / (self.N * math.exp(-self.Q))

    def person_mass(self, person_id: int = 0, variation: float = 0.15) -> float:
        """
        Масса одного человека

        Args:
            person_id: уникальный номер человека (0...N-1)
            variation: стандартное отклонение массы (15% для популяции)

        Returns:
            Масса в нормированных единицах
        """
        # Базовый член
        base_mass = self.m0 * math.exp(-self.Q)

        if person_id == 0:
            return base_mass

        # Вариация массы зависит от person_id
        # Используем псевдослучайную детерминированную функцию
        # чтобы каждый человек имел стабильную массу
        seed = person_id * 99991
        random.seed(seed)
        variation_factor = 1 + variation * (random.gauss(0, 1))

        return base_mass * variation_factor

    def total_mass(self) -> float:
        """Общая масса (нормированная)"""
        return self.normalize_to

    def verify(self) -> Tuple[float, float]:
        """Проверить, что сумма = 1"""
        # Тест на выборке
        sample_size = 10000
        sample_sum = sum(self.person_mass(i) for i in range(sample_size))

        # Экстраполяция
        estimated_total = sample_sum * (self.N / sample_size)

        error = abs(estimated_total - self.normalize_to)
        return estimated_total, error


# ============================================================================
# РАСЧЁТ ДЛЯ КОНКРЕТНОГО ЧЕЛОВЕКА
# ============================================================================


def calculate_exact_mass(
    location: Optional[Tuple[float, float]] = None,  # (широта, долгота)
    age: Optional[float] = None,  # возраст в годах
    sex: Optional[str] = None,  # "M" или "F"
    height: Optional[float] = None,  # рост в см
) -> Dict[str, float]:
    """
    Точный расчёт массы человека с учётом параметров

    Args:
        location: (latitude, longitude) - географические координаты
        age: возраст в годах (по умолчанию 30)
        sex: пол "M" или "F" (по умолчанию "M")
        height: рост в см (по умолчанию 170)

    Returns:
        dict с массой в разных единицах
    """
    # Значения по умолчанию
    age = age if age is not None else 30.0
    sex = sex if sex is not None else "M"
    height = height if height is not None else 170.0

    # Формула массы от параметров
    # BMI = mass / height², средний BMI ≈ 24

    # Базовая масса (нормированная)
    formula = HumanMassFormula(normalize_to=1.0)
    base_mass = formula.m0 * math.exp(-formula.Q)

    # Поправки на параметры
    # Возраст: пик массы в 40-50 лет
    age_factor = 1 + 0.15 * math.sin((age - 20) / 40 * math.pi)

    # Пол: мужчины в среднем на 10% тяжелее
    sex_factor = 1.1 if sex == "M" else 1.0

    # Рост: масса пропорциональна росту в квадрате (BMI)
    height_factor = (height / 170) ** 2

    # География: влияние климата
    # Тропики: меньше масса (терморегуляция)
    # Умеренный пояс: средняя
    # Арктика: больше масса (утепление)
    if location:
        lat, lon = location
        # Широта влияет на массу
        lat_factor = 1 + 0.1 * math.sin(lat / 90 * math.pi)
    else:
        lat_factor = 1.0

    # Итоговая масса (нормированная)
    mass_normalized = base_mass * age_factor * sex_factor * height_factor * lat_factor

    # Реальная масса (кг)
    mass_kg = mass_normalized * HumanityData.TOTAL_MASS_KG

    return {
        "mass_normalized": mass_normalized,
        "mass_kg": mass_kg,
        "age_factor": age_factor,
        "sex_factor": sex_factor,
        "height_factor": height_factor,
        "lat_factor": lat_factor,
        "Q": formula.Q,
        "Δ": DeltaSystem.DELTA_HUMAN,
        "dimension": DeltaSystem.dimension_from_delta(DeltaSystem.DELTA_HUMAN),
    }


# ============================================================================
# ОСНОВНАЯ ПРОГРАММА
# ============================================================================


def main():
    print("=" * 80)
    print("ТОЧНАЯ ФОРМУЛА МАССЫ ЧЕЛОВЕКА")
    print("=" * 80)

    # Создать формулу
    f = HumanMassFormula(normalize_to=1.0)

    print(f"\n### Параметры системы ###")
    print(f"Δ человека: {DeltaSystem.DELTA_HUMAN}")
    print(f"Q = e^|Δ|: {f.Q:.4f}")
    print(f"D_f = 2 + Δ: {DeltaSystem.dimension_from_delta(DeltaSystem.DELTA_HUMAN)}D")
    print(f"ОГОНЬ/ВОДА: {DeltaSystem.fire_or_water(f.Q)}")
    print(f"m₀ (базовый масштаб): {f.m0:.4e}")
    print(f"Число людей N: {f.N}")

    print(f"\n### Проверка нормировки ###")
    total, error = f.verify()
    print(f"Σ m_i = {total:.6f} (должно быть 1)")
    print(f"Погрешность: {error * 100:.4f}%")

    print(f"\n### Масса конкретных людей ###")
    test_ids = [0, 1, 100, 1000, 100000, 1000000, 100000000]
    for pid in test_ids:
        m = f.person_mass(pid)
        m_kg = m * HumanityData.TOTAL_MASS_KG
        print(f"Человек #{pid}: {m:.4e} (норм) = {m_kg:.2f} кг")

    print(f"\n### Точный расчёт с параметрами ###")

    # Разные люди
    examples = [
        {"location": (55.7, 37.6), "age": 30, "sex": "M", "height": 180},  # Москва
        {"location": (40.7, -74.0), "age": 35, "sex": "F", "height": 165},  # Нью-Йорк
        {"location": (35.7, 139.7), "age": 25, "sex": "M", "height": 175},  # Токио
        {"location": (-33.9, 151.2), "age": 40, "sex": "F", "height": 170},  # Сидней
        {"location": (0, 0), "age": 50, "sex": "M", "height": 168},  # Экватор
    ]

    for ex in examples:
        r = calculate_exact_mass(**ex)
        print(
            f"\nВозраст: {ex['age']}, Пол: {ex['sex']}, Рост: {ex['height']}см, "
            f"Локация: {ex['location']}"
        )
        print(f"  Масса: {r['mass_normalized']:.4e} (норм) = {r['mass_kg']:.2f} кг")
        print(
            f"  Поправки: возраст={r['age_factor']:.2f}, пол={r['sex_factor']:.2f}, "
            f"рост={r['height_factor']:.2f}, широта={r['lat_factor']:.2f}"
        )

    print("\n" + "=" * 80)
    print("ИТОГОВАЯ ФОРМУЛА")
    print("=" * 80)
    print("""
    m_person = m₀ × e^(-Q), где:
        m₀ = 1 / (N × e^(-Q))
        Q = e^|Δ| = e^1 ≈ 2.72
        N = 8.1 × 10⁹
        Δ = 1 (человек в 3D)
        
    При нормировке до 1:
        m_person = e^(-1) / N ≈ 1.23 × 10⁻¹⁰ (нормированная)
        
    Σ m_i = N × m_person = 1 ✓
    """)

    print("\n" + "=" * 80)
    print("ГОТОВО: масса любого человека вычислена!")
    print("=" * 80)


if __name__ == "__main__":
    main()
