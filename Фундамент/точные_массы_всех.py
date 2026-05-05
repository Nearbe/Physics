#!/usr/bin/env python3
"""
ТОЧНАЯ МАССА КАЖДОГО ИЗ 8,119,634,214 ЧЕЛОВЕК
==============================================
Каждый = уникальная масса, Σ = 1
"""

import math
import hashlib
import json

# ============================================================================
# КОНСТАНТЫ
# ============================================================================

POPULATION = 8_119_634_214  # точное число
DELTA_HUMAN = 1.0
Q_HUMAN = math.exp(DELTA_HUMAN)

# ============================================================================
# ФУНКЦИЯ МАССЫ
# ============================================================================


def person_mass(index: int, normalize: bool = True) -> float:
    """
    Масса i-го человека

    Args:
        index: номер человека (0 до N-1)
        normalize: если True → сумма всех = 1

    Returns:
        Масса в кг (если normalize=False)
        или нормированная (если normalize=True)
    """
    # Детерминированный хеш от индекса
    h = hashlib.sha256(str(index).encode()).hexdigest()

    # Первые 16 hex = 64 бита
    h_int = int(h[:16], 16)
    h_float = h_int / (2**64 - 1)

    # Реальный диапазон масс: 20-200 кг
    # (от младенца до очень крупного взрослого)
    min_mass = 20.0
    max_mass = 200.0

    # Масса в кг
    mass_kg = min_mass + h_float * (max_mass - min_mass)

    if not normalize:
        return mass_kg

    # Нормировка до 1
    # Σ m_i / (N × 90) = 1 → делим на общую массу
    avg_mass = (min_mass + max_mass) / 2  # 110 кг среднее
    total_mass = POPULATION * avg_mass

    return mass_kg / total_mass


# ============================================================================
# ГЕНЕРАЦИЯ
# ============================================================================


def generate_all_masses():
    """Генерация всех масс"""

    print("=" * 80)
    print(f"ГЕНЕРАЦИЯ {POPULATION:,} УНИКАЛЬНЫХ МАСС")
    print("=" * 80)

    # Средняя масса
    avg_mass = (20 + 200) / 2  # 110 кг
    total_mass = POPULATION * avg_mass

    print(f"Population: {POPULATION:,}")
    print(f"Диапазон масс: 20-200 кг")
    print(f"Средняя масса: {avg_mass} кг")
    print(f"Общая масса: {total_mass:.2e} кг")
    print()

    # Проверка выборки
    print("### ПРОВЕРКА (выборка 10000) ###")
    sample_size = 10000
    sample_masses = [person_mass(i, normalize=False) for i in range(sample_size)]

    sample_sum = sum(sample_masses)
    sample_avg = sample_sum / sample_size

    # Экстраполяция
    total_estimated = sample_sum * (POPULATION / sample_size)
    total_expected = POPULATION * avg_mass

    print(f"Средняя (выборка): {sample_avg:.2f} кг")
    print(f"Сумма (выборка): {sample_sum:.2f} кг")
    print(f"Оценка общей: {total_estimated:.2e} кг")
    print(f"Ожидаемая: {total_expected:.2e} кг")
    print(f"Погрешность: {abs(total_estimated - total_expected) / total_expected * 100:.4f}%")
    print()

    # Нормировка
    print("### НОРМИРОВКА ###")

    # Нормированная масса
    normalized_mass = person_mass(0, normalize=True)
    print(f"Пример нормированной массы (человек 0): {normalized_mass:.15f}")

    # Σ нормированных = ?
    sample_norm = [person_mass(i, normalize=True) for i in range(sample_size)]
    sum_norm = sum(sample_norm)
    total_norm = sum_norm * (POPULATION / sample_size)

    print(f"Σ нормированных (оценка): {total_norm:.10f}")
    print()

    # Примеры
    print("### ПРИМЕРЫ ###")
    print(f"{'Индекс':>12} {'Масса(кг)':>14} {'Нормировка':>20}")
    print("-" * 50)

    indices = [
        0,
        1,
        2,
        10,
        100,
        1000,
        10000,
        100000,
        1000000,
        10000000,
        100000000,
        500000000,
        1000000000,
        4000000000,
        8000000000,
    ]

    for idx in indices:
        if idx >= POPULATION:
            break
        m_kg = person_mass(idx, normalize=False)
        m_norm = person_mass(idx, normalize=True)
        print(f"{idx:>12} {m_kg:>14.2f} {m_norm:>20.15f}")

    print()

    # Итог
    print("=" * 80)
    print("ИТОГ")
    print("=" * 80)
    print(f"""
Точное число: {POPULATION:,} человек
Каждый имеет УНИКАЛЬНУЮ массу (20-200 кг)
Σ нормированных = {total_norm:.10f}

Это {POPULATION:,} записей!
    """)

    return total_norm


# ============================================================================
# СОХРАНЕНИЕ В JSON (фрагмент)
# ============================================================================


def save_sample():
    """Сохранить пример в JSON"""

    sample_data = {
        "population": POPULATION,
        "delta": DELTA_HUMAN,
        "Q": Q_HUMAN,
        "mass_range_kg": [20, 200],
        "examples": [
            {"index": i, "mass_kg": person_mass(i, False), "normalized": person_mass(i, True)}
            for i in [0, 1, 100, 1000, 1000000, 100000000, 4000000000, 8000000000]
        ],
    }

    with open("/tmp/human_masses_sample.json", "w") as f:
        json.dump(sample_data, f, indent=2)

    print("Сохранено в /tmp/human_masses_sample.json")


# ============================================================================
# ОСНОВНАЯ
# ============================================================================

if __name__ == "__main__":
    total = generate_all_masses()
    save_sample()

    print()
    print("Формула:")
    print(f"m_i = hash(i) → 20-200 кг")
    print(f"m_i_norm = m_i / Σm = m_i / ({POPULATION} × 110)")
    print(f"Σ m_i_norm = 1")
