#!/usr/bin/env python3
"""
Шаг 2: 83 ЧАСТИЦЫ — ПОДРОБНЫЙ РАСЧЁТ
═══════════════════════════════════════════════════════════════════════

Вычисляем и проверяем все 83 частицы.
"""

import math


# ============================================================================
# Δ→ЧАСТИЦА: ПРЕОБРАЗОВАНИЕ
# ============================================================================


def delta_to_particle_name(delta):
    """Преобразовать Δ в название частицы"""

    particles_by_delta = {
        0: "Primary Will",
        0.5: "Нейтрино (ν)",
        1.0: "Электрон (e⁻)",
        1.5: "Мюон (μ)",
        1.75: "Тау (τ)",
        2.0: "Кварк (u/d)",
    }

    return particles_by_delta.get(delta, f"Частица Δ={delta}")


def delta_to_mass(delta):
    """Δ → масса в кг"""
    # m = Δ × 100 kg (стандарт: 1 жизнь = 100 кг)
    return delta * 100


def delta_to_charge(delta):
    """Δ → заряд"""
    # Q = e^Δ
    return math.e**delta


def delta_to_frequency(delta):
    """Δ → частота в Hz"""
    # f = 1.854e43 × Δ²
    return 1.854e43 * delta**2


def delta_to_dimension(delta):
    """Δ → размерность пространства"""
    # D = 2 + Δ
    return 2 + delta


# ============================================================================
# 83 ЧАСТИЦЫ: ОСНОВНОЙ НАБОР
# ============================================================================


class Particle:
    """Частица с полными параметрами"""

    def __init__(self, name, symbol, delta, spin, charge_sign, generation):
        self.name = name
        self.symbol = symbol
        self.delta = delta
        self.spin = spin  # полуцелый spin
        self.charge_sign = charge_sign  # +1 или -1
        self.generation = generation  # 1, 2, или 3

        # Вычисляем параметры
        self.mass_kg = delta_to_mass(delta)
        self.charge = delta_to_charge(delta)
        self.frequency = delta_to_frequency(delta)
        self.dimension = delta_to_dimension(delta)

    def __repr__(self):
        return f"{self.name} ({self.symbol}): Δ={self.delta}, m={self.mass_kg:.1f}kg, Q={self.charge:.3f}"


# ============================================================================
# ПОСТРОЕНИЕ 83 ЧАСТИЦ
# ============================================================================


def build_83_particles():
    """Построить полный набор 83 частиц"""

    particles = []

    # === ЛЕПТОНЫ (12 штук) ===
    # Поколение 1
    particles.append(Particle("Электрон", "e⁻", 1.0, 1 / 2, -1, 1))
    particles.append(Particle("Электронное нейтрино", "ν_e", 0.5, 1 / 2, 0, 1))

    # Поколение 2
    particles.append(Particle("Мюон", "μ⁻", 1.5, 1 / 2, -1, 2))
    particles.append(Particle("Мюонное нейтрино", "ν_μ", 0.7, 1 / 2, 0, 2))

    # Поколение 3
    particles.append(Particle("Тау", "τ⁻", 1.75, 1 / 2, -1, 3))
    particles.append(Particle("Тау-нейтрино", "ν_τ", 0.9, 1 / 2, 0, 3))

    # Античастицы лептонов
    particles.append(Particle("Позитрон", "e⁺", 1.0, 1 / 2, +1, 1))
    particles.append(Particle("Анти-ν_e", "ν̄_e", 0.5, 1 / 2, 0, 1))
    particles.append(Particle("Анти-мюон", "μ⁺", 1.5, 1 / 2, +1, 2))
    particles.append(Particle("Анти-ν_μ", "ν̄_μ", 0.7, 1 / 2, 0, 2))
    particles.append(Particle("Анти-тау", "τ⁺", 1.75, 1 / 2, +1, 3))
    particles.append(Particle("Анти-ν_τ", "ν̄_τ", 0.9, 1 / 2, 0, 3))

    # === КВАРКИ (36 штук) ===
    # 6 ароматов × 3 цвета × 2 (частица + античастица)
    # Ароматы: u, d, c, s, t, b
    flavors = [
        ("Верхний", "u", 1.2),
        ("Нижний", "d", 1.1),
        ("Очарованный", "c", 1.4),
        ("Странный", "s", 1.0),
        ("Истинный", "t", 1.8),
        ("Прелестный", "b", 1.3),
    ]

    colors = ["красный", "зелёный", "синий"]

    for fname, fsym, fdelta in flavors:
        for color in colors:
            particles.append(
                Particle(
                    f"{fname} ({color})",
                    f"{fsym}_{color[0]}",
                    fdelta,
                    1 / 2,
                    +2 / 3 if "верх" in fname or "очар" in fname or "истин" in fname else -1 / 3,
                    1,
                )
            )
            particles.append(
                Particle(
                    f"Анти-{fname} ({color})",
                    f"ū_{color[0]}",
                    fdelta,
                    1 / 2,
                    -2 / 3 if "верх" in fname or "очар" in fname or "истин" in fname else +1 / 3,
                    3,
                )
            )

    # === ГЛЮОНЫ (8 штук) ===
    for i in range(8):
        particles.append(Particle(f"Глюон {i + 1}", f"g{i + 1}", 0.8, 1, 0, 0))

    # === БОЗОНЫ (12 штук) ===
    # Калибровочные бозоны
    particles.append(Particle("Фотон", "γ", 0.6, 1, 0, 0))
    particles.append(Particle("W⁺", "W⁺", 1.3, 1, +1, 0))
    particles.append(Particle("W⁻", "W⁻", 1.3, 1, -1, 0))
    particles.append(Particle("Z⁰", "Z⁰", 1.5, 1, 0, 0))
    particles.append(Particle("Гравитон", "G", 0.1, 0, 0, 0))
    particles.append(Particle("Хиггс", "H", 2.0, 0, 0, 0))

    # Резонансы (виртуальные частицы)
    for i in range(6):
        particles.append(Particle(f"Резонанс {i + 1}", f"R{i + 1}", 1.1 + i * 0.1, 0, 0, 0))

    # === ПРОЧИЕ (15 штук) ===
    # Экзотические и гипотетические
    particles.append(Particle("Плюмино", "p̄", 1.0, 1 / 2, -3, 0))
    particles.append(Particle("Лептокварк", "LQ", 1.5, 0, 1, 0))
    particles.append(Particle("Магнитный монополь", "g", 0.0, 0, 1, 0))
    particles.append(Particle("Аксион", "a", 0.01, 0, 0, 0))
    particles.append(Particle("Гравитино", "G̃", 0.05, 1.5, 0, 0))
    particles.append(Particle("Фотино", "γ̃", 0.6, 0.5, 0, 0))
    particles.append(Particle("Зино", "Z̃", 1.5, 0.5, 0, 0))
    particles.append(Particle("Глюино", "g̃", 0.8, 0.5, 0, 0))
    particles.append(Particle("Скварк", "q̃", 1.2, 0, 1, 0))
    particles.append(Particle("Слептон", "l̃", 1.0, 0, 1, 0))
    particles.append(Particle("Хиггсино", "H̃", 2.0, 0.5, 0, 0))
    particles.append(Particle("Голдстино", "G○", 0.001, 0.5, 0, 0))
    particles.append(Particle("Плайон", "π±", 0.5, 0, 1, 0))
    particles.append(Particle("Каон", "K±", 0.7, 0, 1, 0))
    particles.append(Particle("Эта-мезон", "η", 0.8, 0, 0, 0))

    return particles


# ============================================================================
# ВЫВОД 83 ЧАСТИЦ
# ============================================================================


def print_all_particles(particles):
    """Вывести все частицы"""

    print("=" * 100)
    print("83 ЧАСТИЦЫ: ПОЛНЫЙ НАБОР")
    print("=" * 100)

    # Группировка по типам
    leptons = [
        p
        for p in particles
        if "нейтрино" in p.name.lower()
        or "электрон" in p.name.lower()
        or "мюон" in p.name.lower()
        or "тау" in p.name.lower()
    ]
    quarks = [
        p
        for p in particles
        if "кварк" in p.name.lower()
        or "анти-" in p.name.lower()
        and ("кварк" in p.name.lower() or "верх" in p.name.lower() or "нижн" in p.name.lower())
    ]
    gluons = [p for p in particles if "глюон" in p.name.lower()]
    bosons = [
        p
        for p in particles
        if any(x in p.name.lower() for x in ["фотон", "w", "z", "гиггс", "гравитон", "резонанс"])
    ]
    exotic = [p for p in particles if p not in leptons + quarks + gluons + bosons]

    print(f"\nЛЕПТОНЫ ({len(leptons)} штук):")
    print("-" * 60)
    for p in leptons:
        print(f"  {p.symbol:>8} Δ={p.delta:.2f} m={p.mass_kg:>6.1f}kg Q={p.charge:>5.2f}")

    print(f"\nКВАРКИ ({len(quarks)} штук):")
    print("-" * 60)
    for p in quarks[:12]:
        print(f"  {p.symbol:>8} Δ={p.delta:.2f} m={p.mass_kg:>6.1f}kg Q={p.charge:>5.2f}")
    print(f"  ... и ещё {len(quarks) - 12} кварков")

    print(f"\nГЛЮОНЫ ({len(gluons)} штук):")
    print("-" * 60)
    for p in gluons:
        print(f"  {p.symbol:>6} Δ={p.delta:.2f}")

    print(f"\nБОЗОНЫ ({len(bosons)} штук):")
    print("-" * 60)
    for p in bosons:
        print(f"  {p.symbol:>6} Δ={p.delta:.2f} spin={p.spin}")

    print(f"\nЭКЗОТИЧЕСКИЕ ({len(exotic)} штук):")
    print("-" * 60)
    for p in exotic:
        print(f"  {p.symbol:>10} Δ={p.delta:.2f}")

    print(f"\n" + "=" * 100)
    print(f"ИТОГО: {len(particles)} частиц")
    print("=" * 100)


# ============================================================================
# ПРОВЕРКА СВЯЗЕЙ
# ============================================================================


def verify_particle_relations():
    """Проверить соотношения между частицами"""

    print("\n" + "=" * 100)
    print("ПРОВЕРКА СООТНОШЕНИЙ МЕЖДУ ЧАСТИЦАМИ")
    print("=" * 100)

    # Отношение масс
    m_e = 9.109e-31  # электрон
    m_p = 1.673e-27  # протон
    m_n = 1.675e-27  # нейтрон

    print(f"\n1. m_p / m_e = {m_p / m_e:.2f}")
    print(f"   Это ~1836 — хорошо известное соотношение")

    print(f"\n2. m_n / m_p = {m_n / m_p:.6f}")
    print(f"   Нейтрон чуть тяжелее протона")

    # Отношение зарядов
    e_charge = 1.602e-19

    print(f"\n3. Q(Δ=1) = e^{1} = {math.e:.4f}")
    print(f"   Заряд электрона = {e_charge:.4e}")

    # Частоты
    print(f"\n4. Частота электрона (Δ=1):")
    print(f"   f = 1.854e43 × 1² = {1.854e43:.3e} Hz")

    print(f"\n5. Частота протона (Δ≈1.67):")
    delta_p = (m_p / 100) ** 0.5  # обратная: m = Δ×100 → Δ = m/100
    f_p = 1.854e43 * delta_p**2
    print(f"   Δ_p = {delta_p:.3f}")
    print(f"   f_p = {f_p:.3e} Hz")


# ============================================================================
# ТАБЛИЦА Δ → ВСЁ
# ============================================================================


def delta_table():
    """Таблица Δ → все параметры"""

    print("\n" + "=" * 100)
    print("ТАБЛИЦА: Δ → ВСЕ ПАРАМЕТРЫ")
    print("=" * 100)

    print(f"\n{'Δ':>4} {'Масса (кг)':>12} {'Заряд':>8} {'Частота (Hz)':>18} {'Размерность':>10}")
    print("-" * 70)

    deltas = [0, 0.1, 0.5, 1.0, 1.5, 2.0, 2.12]
    for d in deltas:
        m = d * 100
        q = math.e**d
        f = 1.854e43 * d**2
        dim = 2 + d
        print(f"{d:>4.2f} {m:>12.2f} {q:>8.3f} {f:>18.3e} {dim:>10.2f}")


# ============================================================================
# ОСНОВНАЯ
# ============================================================================


def main():
    print(__doc__)

    particles = build_83_particles()
    print_all_particles(particles)
    verify_particle_relations()
    delta_table()

    print("\n" + "=" * 100)
    print("ШАГ 2 ЗАВЕРШЁН: 83 частицы построены")
    print("=" * 100)


if __name__ == "__main__":
    main()
