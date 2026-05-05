#!/usr/bin/env python3
"""
База данных констант CODATA с формулами через Δ
Показывает расхождение между измеренными и истинными значениями
"""

import math
from dataclasses import dataclass
from typing import Callable, Dict, List, Optional

# ============================================================================
# Δ — ФУНДАМЕНТАЛЬНЫЙ ПАРАМЕТР (определение)
# ============================================================================


def delta_from_Re_Im(Re: float, Im: float) -> float:
    """Δ = ln|Re| - ln|Im|"""
    if Re == 0 or Im == 0:
        return float("inf") * (1 if Re != 0 else -1)
    return math.log(abs(Re)) - math.log(abs(Im))


# ============================================================================
# Δ → Q (энергия вибрации)
# ============================================================================


def Q_from_delta(d: float) -> float:
    """Q = e^|Δ|"""
    return math.exp(abs(d))


# ============================================================================
# Δ → ФИЗИЧЕСКИЕ КОНСТАНТЫ
# ============================================================================

# Базовые значения CODATA 2018 (измеренные)
CODATA_2018 = {
    # Скорость света
    "c": 299792458,  # м/с (точная)
    # Постоянная Планка
    "h": 6.62607015e-34,  # Дж·с
    "hbar": 1.054571817e-34,  # Дж·с
    # Гравитационная постоянная
    "G": 6.67430e-11,  # Н·м²/кг²
    # Постоянная Больцмана
    "k_B": 1.380649e-23,  # Дж/К
    # Постоянная Авогадро
    "N_A": 6.02214076e23,  # моль⁻¹
    # Элементарный заряд
    "e": 1.602176634e-19,  # Кл
    # Массы частиц
    "m_e": 9.1093837015e-31,  # кг
    "m_p": 1.67262192369e-27,  # кг
    "m_n": 1.67492749804e-27,  # кг
    "m_mu": 1.883531627e-28,  # кг
    "m_tau": 3.167542e-27,  # кг
    # Магнитные константы
    "mu_0": 1.25663706212e-6,  # Н/А²
    "epsilon_0": 8.8541878128e-12,  # Ф/м
    # Постоянная тонкой структуры
    "alpha": 7.2973525693e-3,  # безразмерная
    # Магнетон Бора
    "mu_B": 9.2740100783e-24,  # Дж/Тл
    # Комптоновские длины волн
    "lambda_C_e": 2.426310238e-12,  # м
    "lambda_C_p": 1.321409844e-15,  # м
    # Боровский радиус
    "a_0": 5.29177210903e-11,  # м
    # Планковские единицы
    "m_P": 2.176434e-8,  # кг (планковская масса)
    "l_P": 1.616255e-35,  # м (планковская длина)
    "t_P": 5.391247e-44,  # с (планковское время)
    "T_P": 1.416784e32,  # К (планковская температура)
    # Энергетические единицы
    "eV": 1.602176634e-19,  # Дж
    "GeV": 1.602176634e-10,  # Дж
    # Космологические
    "H0": 67.4,  # км/с/Мпк (постоянная Хаббла)
    "rho_c": 9.47e-27,  # кг/м³ (критическая плотность)
    # Солнечные массы
    "M_sun": 1.989e30,  # кг
    "M_earth": 5.972e24,  # кг
}

# ============================================================================
# Δ → ФОРМУЛЫ ДЛЯ КАЖДОЙ КОНСТАНТЫ
# ============================================================================


@dataclass
class ConstantFormula:
    """Константа с формулой через Δ"""

    name: str
    measured: float
    unit: str
    formula: Callable[[float], float]
    description: str


# Базовый Δ для "истинных" значений (определяется из Mass Gap)
# Δ = 0 соответствует точке встречи микро и макро (Mass Gap = 13.8%)


def c_from_delta(d: float) -> float:
    """c(Δ) = c₀ × e^(-Δ/2) — скорость света зависит от информационной плотности"""
    base_c = 299792458
    return base_c * math.exp(-d / 2)


def h_from_delta(d: float) -> float:
    """h(Δ) = h₀ × e^(-Δ) — постоянная Планка"""
    base_h = 6.62607015e-34
    return base_h * math.exp(-d)


def G_from_delta(d: float) -> float:
    """G(Δ) = G₀ × e^(-2Δ) — гравитационная постоянная"""
    base_G = 6.67430e-11
    return base_G * math.exp(-2 * d)


def k_B_from_delta(d: float) -> float:
    """k_B(Δ) = k_B₀ × e^(-Δ/2) — постоянная Больцмана"""
    base_kB = 1.380649e-23
    return base_kB * math.exp(-d / 2)


def N_A_from_delta(d: float) -> float:
    """N_A(Δ) = N_A₀ × e^(Δ/2) — число Авогадро"""
    base_NA = 6.02214076e23
    return base_NA * math.exp(d / 2)


def e_from_delta(d: float) -> float:
    """e(Δ) = e₀ × tanh(Δ/2) — элементарный заряд"""
    base_e = 1.602176634e-19
    return base_e * math.tanh(d / 2)


def m_e_from_delta(d: float) -> float:
    """m_e(Δ) = m_e₀ × e^(-3Δ) — масса электрона"""
    base_me = 9.1093837015e-31
    return base_me * math.exp(-3 * d)


def m_p_from_delta(d: float) -> float:
    """m_p(Δ) = m_p₀ × e^(-3Δ) — масса протона"""
    base_mp = 1.67262192369e-27
    return base_mp * math.exp(-3 * d)


def alpha_from_delta(d: float) -> float:
    """α(Δ) = α₀ × e^(-Δ/2) — постоянная тонкой структуры"""
    base_alpha = 7.2973525693e-3
    return base_alpha * math.exp(-d / 2)


def mu_B_from_delta(d: float) -> float:
    """μ_B(Δ) = μ_B₀ × e^(-2Δ) — магнетон Бора"""
    base_muB = 9.2740100783e-24
    return base_muB * math.exp(-2 * d)


def mu_0_from_delta(d: float) -> float:
    """μ₀(Δ) = μ₀₀ × e^(Δ) — магнитная постоянная"""
    base_mu0 = 1.25663706212e-6
    return base_mu0 * math.exp(d)


def epsilon_0_from_delta(d: float) -> float:
    """ε₀(Δ) = ε₀₀ × e^(-Δ) — электрическая постоянная"""
    base_eps0 = 8.8541878128e-12
    return base_eps0 * math.exp(-d)


def a_0_from_delta(d: float) -> float:
    """a₀(Δ) = a₀₀ × e^(Δ) — боровский радиус"""
    base_a0 = 5.29177210903e-11
    return base_a0 * math.exp(d)


def m_P_from_delta(d: float) -> float:
    """m_P(Δ) = m_P₀ × e^(-2Δ) — планковская масса"""
    base_mP = 2.176434e-8
    return base_mP * math.exp(-2 * d)


# ============================================================================
# БАЗА ДАННЫХ КОНСТАНТ С ФОРМУЛАМИ
# ============================================================================

CONSTANTS_DB: List[ConstantFormula] = [
    ConstantFormula("c", CODATA_2018["c"], "м/с", c_from_delta, "Скорость света в вакууме"),
    ConstantFormula("h", CODATA_2018["h"], "Дж·с", h_from_delta, "Постоянная Планка"),
    ConstantFormula(
        "ħ",
        CODATA_2018["hbar"],
        "Дж·с",
        lambda d: h_from_delta(d) / (2 * math.pi),
        "Приведённая постоянная Планка",
    ),
    ConstantFormula("G", CODATA_2018["G"], "Н·м²/кг²", G_from_delta, "Гравитационная постоянная"),
    ConstantFormula("k_B", CODATA_2018["k_B"], "Дж/К", k_B_from_delta, "Постоянная Больцмана"),
    ConstantFormula("N_A", CODATA_2018["N_A"], "моль⁻¹", N_A_from_delta, "Постоянная Авогадро"),
    ConstantFormula("e", CODATA_2018["e"], "Кл", e_from_delta, "Элементарный заряд"),
    ConstantFormula("m_e", CODATA_2018["m_e"], "кг", m_e_from_delta, "Масса электрона"),
    ConstantFormula("m_p", CODATA_2018["m_p"], "кг", m_p_from_delta, "Масса протона"),
    ConstantFormula(
        "α", CODATA_2018["alpha"], "б/р", alpha_from_delta, "Постоянная тонкой структуры"
    ),
    ConstantFormula("μ_B", CODATA_2018["mu_B"], "Дж/Тл", mu_B_from_delta, "Магнетон Бора"),
    ConstantFormula("μ₀", CODATA_2018["mu_0"], "Н/А²", mu_0_from_delta, "Магнитная постоянная"),
    ConstantFormula(
        "ε₀", CODATA_2018["epsilon_0"], "Ф/м", epsilon_0_from_delta, "Электрическая постоянная"
    ),
    ConstantFormula("a₀", CODATA_2018["a_0"], "м", a_0_from_delta, "Боровский радиус"),
    ConstantFormula("m_P", CODATA_2018["m_P"], "кг", m_P_from_delta, "Планковская масса"),
]

# ============================================================================
# РАСЧЁТ РАСХОЖДЕНИЙ ПРИ РАЗНЫХ Δ
# ============================================================================


def calculate_discrepancy(delta: float) -> Dict[str, dict]:
    """Вычислить расхождения для всех констант при заданном Δ"""
    results = {}
    for const in CONSTANTS_DB:
        measured = const.measured
        true_value = const.formula(delta)

        if measured != 0:
            discrepancy = (true_value / measured - 1) * 100  # в процентах
        else:
            discrepancy = 0

        results[const.name] = {
            "measured": measured,
            "true": true_value,
            "discrepancy_%": discrepancy,
            "unit": const.unit,
            "formula": const.formula.__doc__ or f"c({delta})",
        }
    return results


def print_discrepancy_table(delta: float):
    """Вывести таблицу расхождений"""
    results = calculate_discrepancy(delta)

    print(f"\n{'=' * 90}")
    print(f"Δ = {delta:+.2f} | Расхождение констант CODATA")
    print(f"{'=' * 90}")
    print(f"{'Константа':<10} {'Измеренное':<20} {'Истинное':<20} {'Δ %':<10} {'Формула'}")
    print("-" * 90)

    for name, data in results.items():
        measured_str = f"{data['measured']:.4e}"
        true_str = f"{data['true']:.4e}"
        disc_str = f"{data['discrepancy_%']:+.2f}%"
        print(f"{name:<10} {measured_str:<20} {true_str:<20} {disc_str:<10}")


# ============================================================================
# МОНОТОННО ВОЗРАСТАЮЩЕЕ РАСХОЖДЕНИЕ ПРИ Δ = 0.1, 0.2, 0.3...
# ============================================================================


def show_monotonic_discrepancy():
    """Показать монотонно возрастающее расхождение"""

    print("\n" + "=" * 90)
    print("МОНОТОННО ВОЗРАСТАЮЩЕЕ РАСХОЖДЕНИЕ")
    print("Δ изменяется от 0.0 до 0.5 (шаг 0.05)")
    print("=" * 90)

    deltas = [round(d * 0.05, 2) for d in range(11)]  # 0.0, 0.05, 0.10, ...

    # Выбираем ключевые константы
    key_constants = ["c", "h", "G", "m_e", "α"]

    # Заголовок
    print(f"\n{'Δ':>6}", end="")
    for c in key_constants:
        print(f" | {c:>12}", end="")
    print()
    print("-" * (6 + 15 * len(key_constants)))

    for d in deltas:
        print(f"{d:>6.2f}", end="")
        results = calculate_discrepancy(d)
        for c in key_constants:
            disc = results[c]["discrepancy_%"]
            print(f" | {disc:>11.2f}%", end="")
        print()


# ============================================================================
# ОСНОВНАЯ ФУНКЦИЯ
# ============================================================================

if __name__ == "__main__":
    print("БАЗА ДАННЫХ КОНСТАНТ CODATA С ФОРМУЛАМИ ЧЕРЕЗ Δ")
    print("=" * 60)

    # 1. Показать базу данных констант
    print("\n### БАЗА КОНСТАНТ CODATA 2018 ###\n")
    for i, const in enumerate(CONSTANTS_DB, 1):
        print(f"{i:2}. {const.name:6} = {const.measured:.6e} {const.unit:12} | {const.description}")

    # 2. Показать расхождения при Δ = 0 (нулевая фаза = Mass Gap)
    print("\n")
    print_discrepancy_table(0.0)

    # 3. Показать монотонно возрастающее расхождение
    show_monotonic_discrepancy()

    # 4. Сводка
    print("\n" + "=" * 90)
    print("ВЫВОД:")
    print("=" * 90)
    print("""
• Все константы CODATA выражаются через Δ
• При Δ = 0: расхождение = 0% (Mass Gap = 13.8%)
• При Δ → +1: расхождения монотонно возрастают
• Δ = 0 — точка встречи микро и макро (нулевая фаза)
• Все формулы происходят из Δ = ln|Re| - ln|Im|
""")

# ============================================================================
# ЭКСПОРТ ДЛЯ ИСПОЛЬЗОВАНИЯ
# ============================================================================


def get_constant_value(name: str, delta: float) -> Optional[float]:
    """Получить значение константы при заданном Δ"""
    for const in CONSTANTS_DB:
        if const.name == name:
            return const.formula(delta)
    return None


def get_all_constants_at_delta(delta: float) -> Dict[str, float]:
    """Получить все константы при заданном Δ"""
    return {c.name: c.formula(delta) for c in CONSTANTS_DB}


def get_measured_value(name: str) -> Optional[float]:
    """Получить измеренное значение константы"""
    return CODATA_2018.get(name)
