#!/usr/bin/env python3
"""
IME ФУНДАМЕНТ — ЧАСТЬ 1/10: БАЗОВЫЕ КОНСТАНТЫ И Δ-СИСТЕМА
==========================================================

Δ = ln|Re| - ln|Im|  — единственная переменная
K_OBS = 1.138  — поправка наблюдателя
Q = e^|Δ|  — энергия вибрации

Всё выводится из Δ.
"""

from __future__ import annotations

import math
import hashlib
import json
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Callable, Tuple

# ============================================================================
# МОДУЛЬ 0: КОНСТАНТЫ И КОЭФФИЦИЕНТЫ
# ============================================================================


# ------------------------------------------------------------------
# K_OBS — поправка наблюдателя (антропоморфная калибровка)
# ------------------------------------------------------------------
# 2 руки × 10 пальцев = 20 → 10% базовая + 3.8% космологическая
# Итого: 13.8% → K_OBS = 1.138
# ------------------------------------------------------------------

K_OBS: float = 1.138

# ------------------------------------------------------------------
# CODATA 2018 — измеренные значения (занижены на 13.8%)
# ------------------------------------------------------------------

CODATA_MEASURED: Dict[str, float] = {
    # Электромагнитные
    "c": 299_792_458.0,
    "mu_0": 1.256_637_062_12e-6,
    "epsilon_0": 8.854_187_812_8e-12,
    "e": 1.602_176_634e-19,
    "h": 6.626_070_15e-34,
    "hbar": 1.054_571_817e-34,
    "alpha": 7.297_352_569_3e-3,
    # Гравитация
    "G": 6.674_30e-11,
    # Термодинамика
    "k_B": 1.380_649e-23,
    "N_A": 6.022_140_76e23,
    # Массы
    "m_e": 9.109_383_701_5e-31,
    "m_p": 1.672_621_923_69e-27,
    "m_n": 1.674_927_498_04e-27,
    "m_mu": 1.883_531_627e-28,
    "m_tau": 3.167_542e-27,
    "m_W": 8.038_1e-25,
    "m_Z": 9.118_4e-25,
    "m_H": 2.124_5e-25,
    # Магнетизм
    "mu_B": 9.274_010_078_3e-24,
    "mu_N": 5.050_783_699e-27,
    # Длины
    "a_0": 5.291_772_109_03e-11,
    "lambda_C_e": 2.426_310_238e-12,
    "lambda_C_p": 1.321_409_844e-15,
    # Планковские
    "m_P": 2.176_434e-8,
    "l_P": 1.616_255e-35,
    "t_P": 5.391_247e-44,
    "T_P": 1.416_784e32,
    # Космология
    "H0": 67.4,
    "rho_c": 9.47e-27,
    "M_sun": 1.989e30,
    "M_earth": 5.972e24,
    # Энергия
    "eV": 1.602_176_634e-19,
    "GeV": 1.602_176_634e-10,
}


# ------------------------------------------------------------------
# ИСТИННЫЕ константы (с поправкой K_OBS)
# ------------------------------------------------------------------

CODATA_TRUE: Dict[str, float] = {k: v * K_OBS for k, v in CODATA_MEASURED.items()}


# ------------------------------------------------------------------
# Константы с описанием
# ------------------------------------------------------------------


@dataclass(frozen=True)
class ConstantInfo:
    """Описание одной физической константы."""

    name: str
    symbol: str
    measured: float
    true_value: float
    unit: str
    description: str
    delta_formula: str


CONSTANTS_INFO: List[ConstantInfo] = [
    ConstantInfo(
        "Скорость света",
        "c",
        CODATA_MEASURED["c"],
        CODATA_TRUE["c"],
        "м/с",
        "Фундаментальная скорость",
        "c₀ × e^(-Δ/2)",
    ),
    ConstantInfo(
        "Постоянная Планка",
        "h",
        CODATA_MEASURED["h"],
        CODATA_TRUE["h"],
        "Дж·с",
        "Квант действия",
        "h₀ × e^(-Δ)",
    ),
    ConstantInfo(
        "Приведённая постоянная Планка",
        "ħ",
        CODATA_MEASURED["hbar"],
        CODATA_TRUE["hbar"],
        "Дж·с",
        "ħ = h / 2π",
        "hbar₀ × e^(-Δ)",
    ),
    ConstantInfo(
        "Гравитационная постоянная",
        "G",
        CODATA_MEASURED["G"],
        CODATA_TRUE["G"],
        "Н·м²/кг²",
        "Связь массы и расстояния",
        "G₀ × e^(-2Δ)",
    ),
    ConstantInfo(
        "Постоянная Больцмана",
        "k_B",
        CODATA_MEASURED["k_B"],
        CODATA_TRUE["k_B"],
        "Дж/К",
        "Связь энергии и температуры",
        "k_B₀ × e^(-Δ/2)",
    ),
    ConstantInfo(
        "Постоянная Авогадро",
        "N_A",
        CODATA_MEASURED["N_A"],
        CODATA_TRUE["N_A"],
        "моль⁻¹",
        "Число частиц в моле",
        "N_A₀ × e^(Δ/2)",
    ),
    ConstantInfo(
        "Элементарный заряд",
        "e",
        CODATA_MEASURED["e"],
        CODATA_TRUE["e"],
        "Кл",
        "Элементарный заряд",
        "e₀ × (1 - e^(-2|Δ|)) / 2",
    ),
    ConstantInfo(
        "Масса электрона",
        "m_e",
        CODATA_MEASURED["m_e"],
        CODATA_TRUE["m_e"],
        "кг",
        "Легчайшая частица",
        "m_e₀ × e^(-3Δ)",
    ),
    ConstantInfo(
        "Масса протона",
        "m_p",
        CODATA_MEASURED["m_p"],
        CODATA_TRUE["m_p"],
        "кг",
        "Барион",
        "m_p₀ × e^(-3Δ)",
    ),
    ConstantInfo(
        "Масса нейтрона",
        "m_n",
        CODATA_MEASURED["m_n"],
        CODATA_TRUE["m_n"],
        "кг",
        "Нейтрон",
        "m_n₀ × e^(-3Δ)",
    ),
    ConstantInfo(
        "Постоянная тонкой структуры",
        "α",
        CODATA_MEASURED["alpha"],
        CODATA_TRUE["alpha"],
        "б/р",
        "Электромагнитная связь",
        "α₀ × e^(-Δ/2)",
    ),
    ConstantInfo(
        "Магнетон Бора",
        "μ_B",
        CODATA_MEASURED["mu_B"],
        CODATA_TRUE["mu_B"],
        "Дж/Тл",
        "Магнитный момент",
        "μ_B₀ × e^(-2Δ)",
    ),
    ConstantInfo(
        "Магнитная постоянная",
        "μ₀",
        CODATA_MEASURED["mu_0"],
        CODATA_TRUE["mu_0"],
        "Н/А²",
        "Вакуумная проницаемость",
        "μ₀₀ × e^(Δ)",
    ),
    ConstantInfo(
        "Электрическая постоянная",
        "ε₀",
        CODATA_MEASURED["epsilon_0"],
        CODATA_TRUE["epsilon_0"],
        "Ф/м",
        "Вакуумная диэлектричность",
        "ε₀₀ × e^(-Δ)",
    ),
    ConstantInfo(
        "Боровский радиус",
        "a₀",
        CODATA_MEASURED["a_0"],
        CODATA_TRUE["a_0"],
        "м",
        "Размер атома водорода",
        "a₀₀ × e^(Δ)",
    ),
    ConstantInfo(
        "Планковская масса",
        "m_P",
        CODATA_MEASURED["m_P"],
        CODATA_TRUE["m_P"],
        "кг",
        "Минимальная масса",
        "m_P₀ × e^(-2Δ)",
    ),
    ConstantInfo(
        "Планковская длина",
        "l_P",
        CODATA_MEASURED["l_P"],
        CODATA_TRUE["l_P"],
        "м",
        "Минимальная длина",
        "l_P₀ × e^(-Δ)",
    ),
    ConstantInfo(
        "Планковское время",
        "t_P",
        CODATA_MEASURED["t_P"],
        CODATA_TRUE["t_P"],
        "с",
        "Минимальное время",
        "t_P₀ × e^(-Δ)",
    ),
    ConstantInfo(
        "Планковская температура",
        "T_P",
        CODATA_MEASURED["T_P"],
        CODATA_TRUE["T_P"],
        "К",
        "Максимальная температура",
        "T_P₀ × e^(Δ/2)",
    ),
]


# ============================================================================
# МОДУЛЬ 1: Δ-СИСТЕМА — ОСНОВНЫЕ ФОРМУЛЫ
# ============================================================================


# ------------------------------------------------------------------
# Δ = ln|Re| - ln|Im|
# ------------------------------------------------------------------


def delta_from_Re_Im(Re: float, Im: float) -> float:
    """
    Вычислить Δ = ln|Re| - ln|Im|.

    Возвращает:
        +inf  если Im → 0, Re ≠ 0  (сингулярность)
        -inf  если Re → 0, Im ≠ 0  (тёмная энергия)
        nan   если Re = 0 и Im = 0  (истинная неопределённость)
    """
    abs_Re = abs(Re)
    abs_Im = abs(Im)

    if abs_Im == 0.0:
        if abs_Re == 0.0:
            return float("nan")
        return float("inf")

    if abs_Re == 0.0:
        return float("-inf")

    return math.log(abs_Re) - math.log(abs_Im)


# ------------------------------------------------------------------
# Δ из фазы θ: Δ = ln|cot(θ)|
# ------------------------------------------------------------------


def delta_from_phase(theta: float) -> float:
    """Δ = ln|cot(θ)| — зависит только от фазы, не от амплитуды."""
    cos_t = abs(math.cos(theta))
    sin_t = abs(math.sin(theta))

    if sin_t == 0.0:
        return float("inf")
    if cos_t == 0.0:
        return float("-inf")

    return math.log(cos_t) - math.log(sin_t)


# ------------------------------------------------------------------
# Δ из пикселя (SVD-shortcut): Δ(X) = log2(X+1) - log2(256-X)
# ------------------------------------------------------------------


def delta_from_pixel(X: int | float) -> float:
    """
    Δ(X) = log2(X+1) - log2(256-X),  X ∈ [0, 255].

    X=0 → Δ = -8
    X=255 → Δ = +8
    X=128 → Δ = 0
    """
    X = max(0, min(255, X))
    return math.log2(X + 1.0) - math.log2(256.0 - X)


# ------------------------------------------------------------------
# Q = e^|Δ| — энергия вибрации
# ------------------------------------------------------------------


def Q(delta: float) -> float:
    """Q = e^|Δ| — структурная сложность / энергия вибрации."""
    return math.exp(abs(delta))


# ------------------------------------------------------------------
# Обратные формулы: Re, Im из M и Δ
# ------------------------------------------------------------------


def Re_from_M_delta(M: float, delta: float) -> float:
    """Re = √M · e^(Δ/2) / √(e^Δ + e^(-Δ))"""
    if M <= 0:
        return 0.0
    exp_d = math.exp(delta)
    exp_neg_d = math.exp(-delta)
    return math.sqrt(M) * math.exp(delta / 2) / math.sqrt(exp_d + exp_neg_d)


def Im_from_M_delta(M: float, delta: float) -> float:
    """Im = √M · e^(-Δ/2) / √(e^Δ + e^(-Δ))"""
    if M <= 0:
        return 0.0
    exp_d = math.exp(delta)
    exp_neg_d = math.exp(-delta)
    return math.sqrt(M) * math.exp(-delta / 2) / math.sqrt(exp_d + exp_neg_d)


# ------------------------------------------------------------------
# Обратные формулы: Δ из M и Re (или Im)
# ------------------------------------------------------------------


def delta_from_M_Re(M: float, Re: float) -> float:
    """Δ = ln(Re² / (M - Re²)) = ln(Re²/Im²)"""
    Im_sq = M - Re * Re
    if Im_sq <= 0 or Re == 0:
        return float("-inf")
    return math.log(Re * Re / Im_sq)


# ============================================================================
# МОДУЛЬ 2: Δ → ВСЕ КОНСТАНТЫ (формулы через Δ)
# ============================================================================


def c(delta: float) -> float:
    """c(Δ) = c₀ × e^(-Δ/2) — скорость света зависит от информационной плотности."""
    return CODATA_MEASURED["c"] * math.exp(-delta / 2)


def h(delta: float) -> float:
    """h(Δ) = h₀ × e^(-Δ) — постоянная Планка."""
    return CODATA_MEASURED["h"] * math.exp(-delta)


def hbar(delta: float) -> float:
    """ħ(Δ) = h(Δ) / 2π."""
    return h(delta) / (2 * math.pi)


def G(delta: float) -> float:
    """G(Δ) = G₀ × e^(-2Δ) — гравитационная постоянная."""
    return CODATA_MEASURED["G"] * math.exp(-2 * delta)


def k_B(delta: float) -> float:
    """k_B(Δ) = k_B₀ × e^(-Δ/2) — постоянная Больцмана."""
    return CODATA_MEASURED["k_B"] * math.exp(-delta / 2)


def N_A(delta: float) -> float:
    """N_A(Δ) = N_A₀ × e^(Δ/2) — число Авогадро."""
    return CODATA_MEASURED["N_A"] * math.exp(delta / 2)


def e_charge(delta: float) -> float:
    """e(Δ) = e₀ × (1 - e^(-2|Δ|)) / 2 — элементарный заряд."""
    if delta == 0:
        return CODATA_MEASURED["e"] * 0.5
    return CODATA_MEASURED["e"] * (1 - math.exp(-2 * abs(delta))) / 2 * (1 if delta > 0 else -1)


def m_e(delta: float) -> float:
    """m_e(Δ) = m_e₀ × e^(-3Δ) — масса электрона."""
    return CODATA_MEASURED["m_e"] * math.exp(-3 * delta)


def m_p(delta: float) -> float:
    """m_p(Δ) = m_p₀ × e^(-3Δ) — масса протона."""
    return CODATA_MEASURED["m_p"] * math.exp(-3 * delta)


def m_n(delta: float) -> float:
    """m_n(Δ) = m_n₀ × e^(-3Δ) — масса нейтрона."""
    return CODATA_MEASURED["m_n"] * math.exp(-3 * delta)


def m_mu(delta: float) -> float:
    """m_μ(Δ) = m_μ₀ × e^(-3Δ) — масса мюона."""
    return CODATA_MEASURED["m_mu"] * math.exp(-3 * delta)


def m_tau(delta: float) -> float:
    """m_τ(Δ) = m_τ₀ × e^(-3Δ) — масса тау."""
    return CODATA_MEASURED["m_tau"] * math.exp(-3 * delta)


def m_W(delta: float) -> float:
    """m_W(Δ) = m_W₀ × e^(-3Δ) — масса W-бозона."""
    return CODATA_MEASURED["m_W"] * math.exp(-3 * delta)


def m_Z(delta: float) -> float:
    """m_Z(Δ) = m_Z₀ × e^(-3Δ) — масса Z-бозона."""
    return CODATA_MEASURED["m_Z"] * math.exp(-3 * delta)


def m_H(delta: float) -> float:
    """m_H(Δ) = m_H₀ × e^(-3Δ) — масса бозона Хиггса."""
    return CODATA_MEASURED["m_H"] * math.exp(-3 * delta)


def alpha(delta: float) -> float:
    """α(Δ) = α₀ × e^(-Δ/2) — постоянная тонкой структуры."""
    return CODATA_MEASURED["alpha"] * math.exp(-delta / 2)


def mu_B(delta: float) -> float:
    """μ_B(Δ) = μ_B₀ × e^(-2Δ) — магнетон Бора."""
    return CODATA_MEASURED["mu_B"] * math.exp(-2 * delta)


def mu_N(delta: float) -> float:
    """μ_N(Δ) = μ_N₀ × e^(-2Δ) — ядерный магнетон."""
    return CODATA_MEASURED["mu_N"] * math.exp(-2 * delta)


def mu_0(delta: float) -> float:
    """μ₀(Δ) = μ₀₀ × e^(Δ) — магнитная постоянная."""
    return CODATA_MEASURED["mu_0"] * math.exp(delta)


def epsilon_0(delta: float) -> float:
    """ε₀(Δ) = ε₀₀ × e^(-Δ) — электрическая постоянная."""
    return CODATA_MEASURED["epsilon_0"] * math.exp(-delta)


def a_0(delta: float) -> float:
    """a₀(Δ) = a₀₀ × e^(Δ) — боровский радиус."""
    return CODATA_MEASURED["a_0"] * math.exp(delta)


def m_P(delta: float) -> float:
    """m_P(Δ) = m_P₀ × e^(-2Δ) — планковская масса."""
    return CODATA_MEASURED["m_P"] * math.exp(-2 * delta)


def l_P(delta: float) -> float:
    """l_P(Δ) = l_P₀ × e^(-Δ) — планковская длина."""
    return CODATA_MEASURED["l_P"] * math.exp(-delta)


def t_P(delta: float) -> float:
    """t_P(Δ) = t_P₀ × e^(-Δ) — планковское время."""
    return CODATA_MEASURED["t_P"] * math.exp(-delta)


def T_P(delta: float) -> float:
    """T_P(Δ) = T_P₀ × e^(Δ/2) — планковская температура."""
    return CODATA_MEASURED["T_P"] * math.exp(delta / 2)


def H0(delta: float) -> float:
    """H(Δ) = H₀ × e^(-Δ/2) — постоянная Хаббла."""
    return CODATA_MEASURED["H0"] * math.exp(-delta / 2)


def rho_c(delta: float) -> float:
    """ρ_c(Δ) = ρ_c₀ × e^(-3Δ) — критическая плотность."""
    return CODATA_MEASURED["rho_c"] * math.exp(-3 * delta)


# ============================================================================
# МОДУЛЬ 3: ФИЗИЧЕСКИЕ ЯВЛЕНИЯ ЧЕРЕЗ Δ
# ============================================================================


# ------------------------------------------------------------------
# Базовая частота
# ------------------------------------------------------------------

PLANCK_FREQ: float = 1.854e43  # базовая частота Primary Will (Гц)


def f_base(delta: float) -> float:
    """f₀(Δ) = 10^43 × e^(-Δ) — базовая частота осцилляции."""
    return 1e43 * math.exp(-delta)


def f_planck(delta: float) -> float:
    """f₀(Δ) = f_P × e^(-Δ) — базовая частота (планковская)."""
    return PLANCK_FREQ * math.exp(-delta)


# ------------------------------------------------------------------
# Энергия и масса
# ------------------------------------------------------------------


def E_from_delta(delta: float) -> float:
    """E = h × f = h₀ × e^(-2Δ) — энергия."""
    return h(delta) * f_base(delta)


def M_from_delta(delta: float) -> float:
    """M = E/c² = M₀ × e^(-2Δ) — масса."""
    return E_from_delta(delta) / c(delta) ** 2


def p_from_delta(delta: float) -> float:
    """p = h/λ = p₀ × e^(-Δ) — импульс."""
    return h(delta) * f_base(delta) / c(delta)


# ------------------------------------------------------------------
# Волновой вектор и длина волны
# ------------------------------------------------------------------


def k_wave(delta: float) -> float:
    """k = 2π/λ = k₀ × e^(Δ) — волновой вектор (Q > 5, волны)."""
    return 2 * math.pi * f_base(delta) / c(delta) * math.exp(delta)


def wavelength(delta: float) -> float:
    """λ = h/p = λ₀ × e^(Δ) — длина волны (Q > 5, волны)."""
    return h(delta) / p_from_delta(delta) * math.exp(delta)


# ------------------------------------------------------------------
# Фазовая скорость
# ------------------------------------------------------------------


def phase_velocity(delta: float) -> float:
    """v = ω/k = c/e^(2Δ) — фазовая скорость."""
    return c(delta) / math.exp(2 * delta)


# ============================================================================
# МОДУЛЬ 4: Q-СТРУКТУРА — 10 СЛОЁВ ПО 10%
# ============================================================================


@dataclass(frozen=True)
class QLayer:
    """Один слой Q-структуры."""

    layer: int
    Q: float
    visible_fraction: float
    percent: float
    physics: str


def get_Q_layers() -> List[QLayer]:
    """10 слоёв Q = e^|Δ| — каждый 10% Вселенной."""
    layers = []
    physics_map = {
        1: "Макро (галактики)",
        2: "Звёзды",
        3: "Планеты",
        4: "Жизнь",
        5: "Человек",
        6: "Клетки",
        7: "Молекулы",
        8: "Атомы",
        9: "Частицы",
        10: "Струны",
    }
    for q in range(1, 11):
        layers.append(
            QLayer(
                layer=q,
                Q=float(q),
                visible_fraction=math.exp(-q),
                percent=math.exp(-q) * 100,
                physics=physics_map[q],
            )
        )
    return layers


# ============================================================================
# МОДУЛЬ 5: ВИДИМАЯ / СКРЫТАЯ ДОЛЯ
# ===================================================================
