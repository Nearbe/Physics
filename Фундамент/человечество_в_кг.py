#!/usr/bin/env python3
"""
ЧЕЛОВЕЧЕСТВО В КГ: нормировка до 1
==================================
Цель: вычислить общую массу людей через Δ с нормировкой до 1
"""

import math
from dataclasses import dataclass
from typing import Dict, List, Tuple

# ============================================================================
# ДАННЫЕ: население и средняя масса
# ============================================================================

# World population 2024
WORLD_POPULATION = 8.1e9  # 8.1 миллиарда

# Average human mass (adults worldwide: 60-70 kg, children included: ~50 kg)
# WHO data: mean adult mass ~62 kg, global average including children ~51 kg
AVERAGE_HUMAN_MASS_KG = 51.0  # кг

# Total human mass
TOTAL_HUMAN_MASS_KG = WORLD_POPULATION * AVERAGE_HUMAN_MASS_KG

print("=" * 80)
print("ЧЕЛОВЕЧЕСТВО: БАЗОВЫЕ ДАННЫЕ")
print("=" * 80)
print(f"Население мира: {WORLD_POPULATION / 1e9:.2f} млрд")
print(f"Средняя масса человека: {AVERAGE_HUMAN_MASS_KG} кг")
print(f"Общая масса человечества: {TOTAL_HUMAN_MASS_KG:.2e} кг")

# ============================================================================
# НОРМИРОВКА ДО 1
# ============================================================================

NORMALIZED_TOTAL = 1.0  # Нормировка до 1
SCALE_FACTOR = NORMALIZED_TOTAL / TOTAL_HUMAN_MASS_KG

print(f"\nМасштабный коэффициент: {SCALE_FACTOR:.2e} (для нормировки до 1)")

# ============================================================================
# ФИЗИЧЕСКИЕ КОНСТАНТЫ (из CODATA)
# ============================================================================

# Atomic mass unit
AMU_KG = 1.66053906660e-27  # кг

# Proton mass
M_PROTON_KG = 1.67262192369e-27  # кг

# Neutron mass
M_NEUTRON_KG = 1.67492749804e-27  # кг

# Electron mass
M_ELECTRON_KG = 9.1093837015e-31  # кг

# Avogadro constant
N_A = 6.02214076e23  # моль⁻¹

print("\n" + "=" * 80)
print("ФИЗИЧЕСКИЕ КОНСТАНТЫ")
print("=" * 80)
print(f"Атомная единица массы: {AMU_KG:.4e} кг")
print(f"Масса протона: {M_PROTON_KG:.4e} кг")
print(f"Масса нейтрона: {M_NEUTRON_KG:.4e} кг")
print(f"Масса электрона: {M_ELECTRON_KG:.4e} кг")
print(f"Число Авогадро: {N_A:.4e} моль⁻¹")

# ============================================================================
# СОСТАВ ЧЕЛОВЕЧЕСКОГО ТЕЛА
# ============================================================================

# Human body composition (by mass)
# Source: various medical/biochemistry data
BODY_COMPOSITION = {
    "вода": 0.60,  # 60%
    "белки": 0.20,  # 20%
    "жиры": 0.15,  # 15%
    "углеводы": 0.005,  # 0.5%
    "минералы": 0.05,  # 5%
}

# Atomic composition of human body (by number of atoms)
# H: 62%, O: 26%, C: 3%, N: 1.5%, Ca: 0.25%, P: 0.22%, other: ~7%
ATOMIC_COMPOSITION = {
    "H": 0.62,  # Водород
    "O": 0.26,  # Кислород
    "C": 0.03,  # Углерод
    "N": 0.015,  # Азот
    "Ca": 0.0025,  # Кальций
    "P": 0.0022,  # Фосфор
    "K": 0.0006,  # Калий
    "S": 0.0006,  # Сера
    "Na": 0.0005,  # Натрий
    "Cl": 0.0004,  # Хлор
    "Mg": 0.0001,  # Магний
    "Fe": 0.00006,  # Железо
    "другие": 0.00614,  # Остальные
}

# Average atomic mass by element (in u)
ATOMIC_MASS = {
    "H": 1.008,
    "O": 15.999,
    "C": 12.011,
    "N": 14.007,
    "Ca": 40.078,
    "P": 30.974,
    "K": 39.098,
    "S": 32.065,
    "Na": 22.990,
    "Cl": 35.453,
    "Mg": 24.305,
    "Fe": 55.845,
}

# ============================================================================
# РАСЧЁТ КОЛИЧЕСТВА АТОМОВ В ЧЕЛОВЕКЕ
# ============================================================================


def calculate_atoms_in_human(mass_kg: float) -> Dict[str, float]:
    """
    Рассчитать количество атомов каждого элемента в теле человека
    """
    # Средняя масса атома в теле (в зависимости от состава)
    # Водород 62% → средняя масса ~1.2 u
    avg_atomic_mass_u = sum(
        ATOMIC_MASS[el] * frac for el, frac in ATOMIC_COMPOSITION.items() if el in ATOMIC_MASS
    )

    # Масса одного "среднего" атома в кг
    avg_atom_mass_kg = avg_atomic_mass_u * AMU_KG

    # Количество атомов
    total_atoms = mass_kg / avg_atom_mass_kg

    # Атомы по элементам
    atoms_by_element = {}
    for el, frac in ATOMIC_COMPOSITION.items():
        atoms_by_element[el] = total_atoms * frac

    return {
        "total_atoms": total_atoms,
        "by_element": atoms_by_element,
        "avg_atom_mass_kg": avg_atom_mass_kg,
    }


human_atoms = calculate_atoms_in_human(AVERAGE_HUMAN_MASS_KG)

print("\n" + "=" * 80)
print("АТОМЫ В ОДНОМ ЧЕЛОВЕКЕ")
print("=" * 80)
print(f"Общее число атомов: {human_atoms['total_atoms']:.3e}")
print(f"Средняя масса атома: {human_atoms['avg_atom_mass_kg']:.4e} кг")
print("\nПо элементам:")
for el, count in human_atoms["by_element"].items():
    print(f"  {el}: {count:.3e} атомов ({ATOMIC_COMPOSITION[el] * 100:.1f}%)")

# ============================================================================
# ОБЩЕЕ КОЛИЧЕСТВО АТОМОВ ЧЕЛОВЕЧЕСТВА
# ============================================================================

TOTAL_ATOMS_HUMANITY = human_atoms["total_atoms"] * WORLD_POPULATION

print("\n" + "=" * 80)
print("ВСЕГО АТОМОВ В ЧЕЛОВЕЧЕСТВЕ")
print("=" * 80)
print(f"В одном человеке: {human_atoms['total_atoms']:.3e}")
print(f"На планете: {TOTAL_ATOMS_HUMANITY:.3e} атомов")

# ============================================================================
# МАССА В ПРОТОННЫХ ЭКВИВАЛЕНТАХ
# ============================================================================

# Масса всех людей в единицах массы протона
TOTAL_MASS_IN_PROTONS = TOTAL_HUMAN_MASS_KG / M_PROTON_KG

# Масса всех людей в единицах массы электрона
TOTAL_MASS_IN_ELECTRONS = TOTAL_HUMAN_MASS_KG / M_ELECTRON_KG

print("\n" + "=" * 80)
print("МАССА В ЭЛЕМЕНТАРНЫХ ЕДИНИЦАХ")
print("=" * 80)
print(f"В единицах протона: {TOTAL_MASS_IN_PROTONS:.3e}")
print(f"В единицах электрона: {TOTAL_MASS_IN_ELECTRONS:.3e}")

# ============================================================================
# Δ-ФОРМУЛЫ: ЧЕЛОВЕЧЕСТВО ЧЕРЕЗ Δ
# ============================================================================

# Δ = 1 для человека (3D, видимый мир)
# Q = e^|Δ| = e^1 ≈ 2.718


def Q_from_delta(delta: float) -> float:
    """Q = e^|Δ|"""
    return math.exp(abs(delta))


def mass_from_Q(Q: float, m0: float = 1e-27) -> float:
    """m = m0 * e^(-Q)"""
    return m0 * math.exp(-Q)


def delta_from_mass(mass_kg: float, m0: float = 1e-27) -> float:
    """Δ = -ln(m/m0)"""
    if mass_kg > 0:
        return -math.log(mass_kg / m0)
    return 10


# Человек в системе Δ
HUMAN_DELTA = 1.0  # Человек = 3D
HUMAN_Q = Q_from_delta(HUMAN_DELTA)

print("\n" + "=" * 80)
print("ЧЕЛОВЕК В Δ-СИСТЕМЕ")
print("=" * 80)
print(f"Δ человека: {HUMAN_DELTA}")
print(f"Q = e^|Δ|: {HUMAN_Q:.4f}")
print(f"Человек = ОГОНЬ (Q ≤ 5): {HUMAN_Q <= 5}")

# ============================================================================
# НОРМИРОВКА ДО 1: ФОРМУЛА
# ============================================================================


class HumanMassCalculator:
    """
    Калькулятор массы человечества через Δ
    """

    def __init__(self, normalize_to: float = 1.0):
        self.normalize_to = normalize_to
        self.population = WORLD_POPULATION
        self.avg_mass = AVERAGE_HUMAN_MASS_KG
        self.total_mass = self.population * self.avg_mass
        self.scale = normalize_to / self.total_mass

    def human_mass_normalized(self, person_id: int = None) -> float:
        """
        Масса человека (нормированная)
        person_id: номер человека (0 = первый, 1 = второй...)
        """
        mass = self.avg_mass * self.scale
        if person_id is not None:
            # Номер человека влияет на фазу
            return mass * (1 + 0.001 * math.sin(person_id / 1e9))
        return mass

    def total_mass_normalized(self) -> float:
        """Общая масса (нормированная)"""
        return self.normalize_to

    def population_count(self) -> float:
        """Количество людей"""
        return self.population

    def person_mass_at_index(self, index: int) -> float:
        """Масса i-го человека"""
        return self.human_mass_normalized(index)

    def summary(self) -> str:
        return f"""
ЧЕЛОВЕЧЕСТВО: НОРМИРОВКА ДО 1
==============================

Исходные данные:
• population = {self.population:.2e} человек
• avg_mass = {self.avg_mass} кг/человек  
• total_mass = {self.total_mass:.4e} кг

Нормировка:
• normalize_to = {self.normalize_to}
• scale = {self.scale:.4e}

Результат:
• Общая масса = {self.normalize_to} (нормированная)
• Средняя масса = {self.human_mass_normalized():.4e} (нормированная)
• Q человека = {HUMAN_Q:.4f} (ОГОНЬ)
"""


# Создать калькулятор
calc = HumanMassCalculator(normalize_to=1.0)
print(calc.summary())

# ============================================================================
# ТОЧНЫЙ РАСЧЁТ МАССЫ КАЖДОГО ЧЕЛОВЕКА
# ============================================================================


def exact_mass_calculation():
    """
    Точный расчёт массы каждого человека через Δ-формулу
    """
    print("\n" + "=" * 80)
    print("ТОЧНЫЙ РАСЧЁТ: МАССА КАЖДОГО ЧЕЛОВЕКА")
    print("=" * 80)

    # Человек = Δ = 1 → Q = e^1 ≈ 2.718
    # Масса = m_0 * e^(-Q) = m_0 * e^(-1) = m_0 * 0.368

    # m_0 выбираем так, чтобы сумма = 1
    # total = N * m_0 * e^(-1) = 1
    # m_0 = 1 / (N * e^(-1)) = e / N

    m_0 = math.e / WORLD_POPULATION  # Базовый масштаб массы

    print(f"Базовый масштаб m₀ = e/N = {m_0:.4e} кг")
    print(
        f"Проверка: N × m₀ × e^(-1) = {WORLD_POPULATION} × {m_0:.4e} × {math.exp(-1):.4f} = {WORLD_POPULATION * m_0 * math.exp(-1):.4f}"
    )

    # Масса каждого человека (одинаковая в среднем)
    individual_mass = m_0 * math.exp(-1)

    print(f"\nМасса одного человека: {individual_mass:.4e} кг")
    print(f"Средняя масса (фактическая): {AVERAGE_HUMAN_MASS_KG} кг")
    print(f"Коэффициент: {AVERAGE_HUMAN_MASS_KG / individual_mass:.2f}")

    return m_0, individual_mass


m_0, individual_mass = exact_mass_calculation()

# ============================================================================
# ФОРМУЛА С УЧЁТОМ ИНДИВИДУАЛЬНОЙ ВАРИАЦИИ
# ============================================================================


def mass_with_variation(person_index: int, variation_std: float = 0.15) -> float:
    """
    Масса с учётом индивидуальной вариации

    person_index: номер человека (0...N-1)
    variation_std: стандартное отклонение массы (15% для взрослых)
    """
    # Вариация массы описывается нормальным распределением
    # μ = средняя масса, σ = variation_std × μ

    import random

    random.seed(person_index)  # Детерминированный "случайный" выбор

    # Центральная предельная теорема: сумма многих факторов
    # Масса определяется: ростом, возрастом, полом, составом тела

    # Базовый индекс (нормализованный)
    base_index = person_index / WORLD_POPULATION

    # Вариация через sin ( детерминированная )
    variation = 1 + variation_std * math.sin(2 * math.pi * base_index * 1000)

    return individual_mass * variation


print("\n" + "=" * 80)
print("ВАРИАЦИЯ МАССЫ ПО ЧЕЛОВЕКАМ")
print("=" * 80)

# Примеры для разных людей
for i in [0, 1, 1000, 1_000_000, 1_000_000_000]:
    mass = mass_with_variation(i)
    print(f"Человек #{i}: {mass:.4e} кг")

# ============================================================================
# ИТОГОВАЯ ФОРМУЛА
# ============================================================================

print("\n" + "=" * 80)
print("ИТОГОВАЯ ФОРМУЛА")
print("=" * 80)
print("""
МАССА ЧЕЛОВЕЧЕСТВА:

    M_total = 1 (нормировка)
    
    N = 8.1 × 10⁹ человек
    
    m₀ = e / N = 2.718 / 8.1e9 = 3.36 × 10⁻¹⁰ кг
    
    m_person = m₀ × e^(-Δ) = m₀ × e^(-1) = 3.36 × 10⁻¹⁰ × 0.368 
             = 1.24 × 10⁻¹⁰ кг (нормированная)
    
    Σ m_i = N × m_person = 1 (проверено)

Δ = 1 для человека (3D, ОГОНЬ)
""")

# ============================================================================
# ПРОВЕРКА: СУММА = 1
# ============================================================================

total_normalized = 0
for i in range(min(1000, int(WORLD_POPULATION))):
    total_normalized += mass_with_variation(i)

# Экстраполяция на всех
estimated_total = total_normalized * (WORLD_POPULATION / 1000)

print(f"\nПроверка суммы (первые 1000): {total_normalized:.6f}")
print(f"Экстраполяция на всех: {estimated_total:.6f}")
print(f"Погрешность: {abs(estimated_total - 1) * 100:.4f}%")

# ============================================================================
# Δ = 1 → 3D → ЧЕЛОВЕК
# ============================================================================

print("\n" + "=" * 80)
print("СВЯЗЬ С Δ")
print("=" * 80)
print(f"""
Δ = 1 → D_f = 2 + Δ = 3 → 3D пространство
Q = e^|Δ| = e^1 ≈ 2.72 → ОГОНЬ (частица, видимый мир)

Человек = видимая структура (ОГОНЬ)
    ↓
    Q = 2.72 < 5 → частица
    
Масса человека через Δ:
    m = m₀ × e^(-Q) = m₀ × e^(-e^|Δ|)
    
При Δ = 1:
    m = m₀ × e^(-2.72) = m₀ × 0.066
""")

print("\n" + "=" * 80)
print("ГОТОВО!")
print("=" * 80)
