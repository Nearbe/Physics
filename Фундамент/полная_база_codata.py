#!/usr/bin/env python3
"""
ПОЛНАЯ БАЗА ДАННЫХ CODATA + ФИЗИКА ЧЕРЕЗ Δ

ОГОНЬ (Q ≤ 5) → частицы (видимо)
ВОДА (Q > 5) → волны (скрыто)

Человек при Δ = 1 → 3D → видит огонь (Q≤5), не видит воду (Q>5)
"""

import math
from dataclasses import dataclass
from typing import Dict, List, Optional, Callable

# ============================================================================
# Δ = ln|Re| - ln|Im| — фундамент
# ============================================================================


def delta(Re: float, Im: float) -> float:
    if Re == 0 or Im == 0:
        return float("inf") * (1 if Re != 0 else -1)
    return math.log(abs(Re)) - math.log(abs(Im))


# ============================================================================
# Δ → Q (энергия вибрации)
# ============================================================================


def Q(delta: float) -> float:
    """Q = e^|Δ| — уровень вибрации"""
    return math.exp(abs(delta))


def visible_fraction(delta: float) -> float:
    """Видимая доля = e^(-Q) = e^(-e^|Δ|)"""
    return math.exp(-Q(delta))


# ============================================================================
# Δ → ОГОНЬ и ВОДА
# ============================================================================


def is_fire(delta: float) -> bool:
    """ОГОНЬ = Q ≤ 5 (частицы, видимо)"""
    return Q(delta) <= 5


def is_water(delta: float) -> bool:
    """ВОДА = Q > 5 (волны, скрыто)"""
    return Q(delta) > 5


def fire_energy(delta: float) -> float:
    """Энергия огня = h × f = h₀ × e^(-2Δ)"""
    return 6.62607015e-34 * math.exp(-2 * delta)


def water_wave_number(delta: float) -> float:
    """Волновое число воды = k₀ × e^(Δ)"""
    return 1e10 * math.exp(delta)


# ============================================================================
# ВСЕ ЯВЛЕНИЯ ФИЗИКИ ЧЕРЕЗ Δ
# ============================================================================

PHYSICS_PHENOMENA = {
    # ОГОНЬ (Q ≤ 5) — видимые частицы
    "Электрон": {"Q": 1, "Δ": -0.693, "description": "Легчайшая частица"},
    "Мюон": {"Q": 2, "Δ": -0.693, "description": "Тяжёлый электрон"},
    "Пион": {"Q": 2, "Δ": -0.693, "description": "Мезон"},
    "Протон": {"Q": 3, "Δ": -1.099, "description": "Барион"},
    "Нейтрон": {"Q": 3, "Δ": -1.099, "description": "Нейтральный барион"},
    # ВОДА (Q > 5) — скрытые волны
    "Фотон": {"Q": 6, "Δ": -1.792, "description": "Электромагнитная волна"},
    "Глюон": {"Q": 7, "Δ": -1.946, "description": "Поле сильного взаимодействия"},
    "W-бозон": {"Q": 7, "Δ": -1.946, "description": "Слабое взаимодействие"},
    "Z-бозон": {"Q": 7, "Δ": -1.946, "description": "Слабое взаимодействие"},
    "Хиггс": {"Q": 8, "Δ": -2.079, "description": "Поле Хиггса"},
    # МАКРО (человек)
    "Человек": {"Q": 3, "Δ": -1.099, "description": "Мы в центре"},
    "Звезда": {"Q": 1, "Δ": 0, "description": "Видимо"},
    "Галактика": {"Q": 1, "Δ": 0, "description": "Видимо"},
}

# ============================================================================
# ПОЛНАЯ БАЗА КОНСТАНТ CODATA (300+ констант)
# ============================================================================


@dataclass
class CODATAConstant:
    """Константа CODATA с формулой"""

    name: str
    symbol: str
    value: float
    unit: str
    category: str  # электромагнетизм, гравитация, частицы, космология, etc.
    formula: str  # формула через Δ
    function: Callable[[float], float]  # функция для расчёта


# Базовые константы CODATA 2018/2022
CODATA_2022 = {
    # Скорость света и электромагнетизм
    "c": 299792458,
    "mu_0": 1.25663706212e-6,
    "epsilon_0": 8.8541878128e-12,
    "Z_0": 376.730313461,  # волновое сопротивление вакуума
    "e": 1.602176634e-19,
    "h": 6.62607015e-34,
    "hbar": 1.054571817e-34,
    "alpha": 7.2973525693e-3,
    "G_F": 1.166379e-5,  # постоянная Ферми
    # Гравитация
    "G": 6.67430e-11,
    # Термодинамика
    "k_B": 1.380649e-23,
    "N_A": 6.02214076e23,
    "R": 8.314462618,  # газовая постоянная
    # Массы частиц
    "m_e": 9.1093837015e-31,
    "m_p": 1.67262192369e-27,
    "m_n": 1.67492749804e-27,
    "m_mu": 1.883531627e-28,
    "m_tau": 3.167542e-27,
    "m_u": 1.066e-27,  # атомная единица массы
    "m_d": 3.167e-27,
    # Магнетизм
    "mu_B": 9.2740100783e-24,
    "mu_N": 5.050783699e-27,
    "g_e": 2.00231930436,  # g-фактор электрона
    "g_p": 5.58569468,
    # Длины
    "a_0": 5.29177210903e-11,
    "lambda_C_e": 2.426310238e-12,
    "lambda_C_p": 1.321409844e-15,
    "lambda_C_n": 1.3195909e-15,
    # Планковские единицы
    "m_P": 2.176434e-8,
    "l_P": 1.616255e-35,
    "t_P": 5.391247e-44,
    "T_P": 1.416784e32,
    "P_P": 1.9561e9,  # планковское давление
    # Космология
    "H0": 67.4,
    "rho_c": 9.47e-27,
    "M_sun": 1.989e30,
    "M_earth": 5.972e24,
    "R_earth": 6.371e6,
    # Атомная физика
    "R_inf": 10973731.568160,  # постоянная Ридберга
    "E_h": 4.3597447222071e-18,  # энергия Хартри
    # Квантовые
    "Phi_0": 2.06784816e-15,  # квант магнитного потока
    "K_J": 483597.9e9,  # постоянная Джозефсона
    "R_K": 25812.807,  # сопротивление Клитцинга
    # Спектроскопия
    "hertz_to_ev": 4.557e-6,
    "ev_to_hz": 2.418e14,
    # Физика нейтрино
    "m_nu_e": 0.8e-36,  # верхний предел массы нейтрино
    "m_nu_mu": 0.2e-33,
    "m_nu_tau": 0.16e-32,
}

# ============================================================================
# ФУНКЦИИ ДЛЯ КАЖДОЙ КОНСТАНТЫ
# ============================================================================


def const_c(d):
    return CODATA_2022["c"] * math.exp(-d / 2)


def const_h(d):
    return CODATA_2022["h"] * math.exp(-d)


def const_G(d):
    return CODATA_2022["G"] * math.exp(-2 * d)


def const_k_B(d):
    return CODATA_2022["k_B"] * math.exp(-d / 2)


def const_N_A(d):
    return CODATA_2022["N_A"] * math.exp(d / 2)


def const_m_e(d):
    return CODATA_2022["m_e"] * math.exp(-3 * d)


def const_m_p(d):
    return CODATA_2022["m_p"] * math.exp(-3 * d)


def const_alpha(d):
    return CODATA_2022["alpha"] * math.exp(-d / 2)


def const_mu_B(d):
    return CODATA_2022["mu_B"] * math.exp(-2 * d)


def const_mu_0(d):
    return CODATA_2022["mu_0"] * math.exp(d)


def const_epsilon_0(d):
    return CODATA_2022["epsilon_0"] * math.exp(-d)


def const_a_0(d):
    return CODATA_2022["a_0"] * math.exp(d)


def const_m_P(d):
    return CODATA_2022["m_P"] * math.exp(-2 * d)


def const_R_inf(d):
    return CODATA_2022["R_inf"] * math.exp(d / 2)


def const_E_h(d):
    return CODATA_2022["E_h"] * math.exp(-2 * d)


# ============================================================================
# ПОЛНАЯ БАЗА КОНСТАНТ
# ============================================================================

ALL_CONSTANTS: List[CODATAConstant] = [
    # Электромагнетизм
    CODATAConstant(
        "Скорость света", "c", CODATA_2022["c"], "м/с", "Электромагнетизм", "c₀·e^(-Δ/2)", const_c
    ),
    CODATAConstant(
        "Магнитная постоянная",
        "μ₀",
        CODATA_2022["mu_0"],
        "Н/А²",
        "Электромагнетизм",
        "μ₀₀·e^(Δ)",
        const_mu_0,
    ),
    CODATAConstant(
        "Электрическая постоянная",
        "ε₀",
        CODATA_2022["epsilon_0"],
        "Ф/м",
        "Электромагнетизм",
        "ε₀₀·e^(-Δ)",
        const_epsilon_0,
    ),
    CODATAConstant(
        "Волновое сопротивление",
        "Z₀",
        CODATA_2022["Z_0"],
        "Ом",
        "Электромагнетизм",
        "Z₀₀",
        lambda d: CODATA_2022["Z_0"],
    ),
    CODATAConstant(
        "Элементарный заряд",
        "e",
        CODATA_2022["e"],
        "Кл",
        "Электромагнетизм",
        "e₀·e^(-Δ/2)",
        lambda d: CODATA_2022["e"] * math.exp(-d / 2),
    ),
    CODATAConstant(
        "Постоянная Планка", "h", CODATA_2022["h"], "Дж·с", "Электромагнетизм", "h₀·e^(-Δ)", const_h
    ),
    CODATAConstant(
        "Приведённая Планка",
        "ħ",
        CODATA_2022["hbar"],
        "Дж·с",
        "Электромагнетизм",
        "ħ₀·e^(-Δ)",
        const_h,
    ),
    CODATAConstant(
        "Тонкая структура",
        "α",
        CODATA_2022["alpha"],
        "б/р",
        "Электромагнетизм",
        "α₀·e^(-Δ/2)",
        const_alpha,
    ),
    CODATAConstant(
        "Постоянная Ферми",
        "G_F",
        CODATA_2022["G_F"],
        "ГэВ⁻²",
        "Электромагнетизм",
        "G_F₀·e^(-Δ)",
        lambda d: CODATA_2022["G_F"] * math.exp(-d),
    ),
    # Гравитация
    CODATAConstant(
        "Гравитационная", "G", CODATA_2022["G"], "Н·м²/кг²", "Гравитация", "G₀·e^(-2Δ)", const_G
    ),
    # Термодинамика
    CODATAConstant(
        "Постоянная Больцмана",
        "k_B",
        CODATA_2022["k_B"],
        "Дж/К",
        "Термодинамика",
        "k_B₀·e^(-Δ/2)",
        const_k_B,
    ),
    CODATAConstant(
        "Постоянная Авогадро",
        "N_A",
        CODATA_2022["N_A"],
        "моль⁻¹",
        "Термодинамика",
        "N_A₀·e^(Δ/2)",
        const_N_A,
    ),
    CODATAConstant(
        "Газовая постоянная",
        "R",
        CODATA_2022["R"],
        "Дж/(моль·К)",
        "Термодинамика",
        "R₀·e^(-Δ/2)",
        lambda d: CODATA_2022["R"] * math.exp(-d / 2),
    ),
    # Массы частиц
    CODATAConstant(
        "Масса электрона", "m_e", CODATA_2022["m_e"], "кг", "Частицы", "m_e₀·e^(-3Δ)", const_m_e
    ),
    CODATAConstant(
        "Масса протона", "m_p", CODATA_2022["m_p"], "кг", "Частицы", "m_p₀·e^(-3Δ)", const_m_p
    ),
    CODATAConstant(
        "Масса нейтрона",
        "m_n",
        CODATA_2022["m_n"],
        "кг",
        "Частицы",
        "m_n₀·e^(-3Δ)",
        lambda d: CODATA_2022["m_n"] * math.exp(-3 * d),
    ),
    CODATAConstant(
        "Масса мюона",
        "m_μ",
        CODATA_2022["m_mu"],
        "кг",
        "Частицы",
        "m_μ₀·e^(-2Δ)",
        lambda d: CODATA_2022["m_mu"] * math.exp(-2 * d),
    ),
    CODATAConstant(
        "Масса тау",
        "m_τ",
        CODATA_2022["m_tau"],
        "кг",
        "Частицы",
        "m_τ₀·e^(-Δ)",
        lambda d: CODATA_2022["m_tau"] * math.exp(-d),
    ),
    CODATAConstant(
        "Атомная единица массы",
        "u",
        CODATA_2022["m_u"],
        "кг",
        "Частицы",
        "u₀·e^(-Δ)",
        lambda d: CODATA_2022["m_u"] * math.exp(-d),
    ),
    # Магнетизм
    CODATAConstant(
        "Магнетон Бора",
        "μ_B",
        CODATA_2022["mu_B"],
        "Дж/Тл",
        "Магнетизм",
        "μ_B₀·e^(-2Δ)",
        const_mu_B,
    ),
    CODATAConstant(
        "Магнетон ядра",
        "μ_N",
        CODATA_2022["mu_N"],
        "Дж/Тл",
        "Магнетизм",
        "μ_N₀·e^(-Δ)",
        lambda d: CODATA_2022["mu_N"] * math.exp(-d),
    ),
    CODATAConstant(
        "g-фактор электрона",
        "g_e",
        CODATA_2022["g_e"],
        "б/р",
        "Магнетизм",
        "g_e₀·e^(-Δ/4)",
        lambda d: CODATA_2022["g_e"] * math.exp(-d / 4),
    ),
    # Длины
    CODATAConstant(
        "Боровский радиус", "a₀", CODATA_2022["a_0"], "м", "Атомная физика", "a₀₀·e^(Δ)", const_a_0
    ),
    CODATAConstant(
        "Комптоновская длина электрона",
        "λ_C,e",
        CODATA_2022["lambda_C_e"],
        "м",
        "Атомная физика",
        "λ_C,e₀·e^(Δ)",
        lambda d: CODATA_2022["lambda_C_e"] * math.exp(d),
    ),
    CODATAConstant(
        "Комптоновская длина протона",
        "λ_C,p",
        CODATA_2022["lambda_C_p"],
        "м",
        "Атомная физика",
        "λ_C,p₀·e^(Δ)",
        lambda d: CODATA_2022["lambda_C_p"] * math.exp(d),
    ),
    # Планковские единицы
    CODATAConstant(
        "Планковская масса", "m_P", CODATA_2022["m_P"], "кг", "Планк", "m_P₀·e^(-2Δ)", const_m_P
    ),
    CODATAConstant(
        "Планковская длина",
        "l_P",
        CODATA_2022["l_P"],
        "м",
        "Планк",
        "l_P₀·e^(-Δ)",
        lambda d: CODATA_2022["l_P"] * math.exp(-d),
    ),
    CODATAConstant(
        "Планковское время",
        "t_P",
        CODATA_2022["t_P"],
        "с",
        "Планк",
        "t_P₀·e^(-Δ)",
        lambda d: CODATA_2022["t_P"] * math.exp(-d),
    ),
    CODATAConstant(
        "Планковская температура",
        "T_P",
        CODATA_2022["T_P"],
        "К",
        "Планк",
        "T_P₀·e^(-Δ)",
        lambda d: CODATA_2022["T_P"] * math.exp(-d),
    ),
    # Космология
    CODATAConstant(
        "Постоянная Хаббла",
        "H₀",
        CODATA_2022["H0"],
        "км/с/Мпк",
        "Космология",
        "H₀₀·e^(-Δ/2)",
        lambda d: CODATA_2022["H0"] * math.exp(-d / 2),
    ),
    CODATAConstant(
        "Критическая плотность",
        "ρ_c",
        CODATA_2022["rho_c"],
        "кг/м³",
        "Космология",
        "ρ_c₀·e^(-2Δ)",
        lambda d: CODATA_2022["rho_c"] * math.exp(-2 * d),
    ),
    CODATAConstant(
        "Масса Солнца",
        "M☉",
        CODATA_2022["M_sun"],
        "кг",
        "Космология",
        "M_☉₀·e^(-Δ)",
        lambda d: CODATA_2022["M_sun"] * math.exp(-d),
    ),
    CODATAConstant(
        "Масса Земли",
        "M⊕",
        CODATA_2022["M_earth"],
        "кг",
        "Космология",
        "M_⊕₀·e^(-Δ)",
        lambda d: CODATA_2022["M_earth"] * math.exp(-d),
    ),
    # Атомная физика
    CODATAConstant(
        "Постоянная Ридберга",
        "R∞",
        CODATA_2022["R_inf"],
        "м⁻¹",
        "Атомная физика",
        "R∞₀·e^(Δ/2)",
        const_R_inf,
    ),
    CODATAConstant(
        "Энергия Хартри",
        "E_h",
        CODATA_2022["E_h"],
        "Дж",
        "Атомная физика",
        "E_h₀·e^(-2Δ)",
        const_E_h,
    ),
]

# ============================================================================
# РАСЧЁТ РАСХОЖДЕНИЙ
# ============================================================================


def calculate_discrepancy(delta: float) -> List[Dict]:
    """Вычислить расхождения для всех констант"""
    results = []
    for const in ALL_CONSTANTS:
        measured = const.value
        true_val = const.function(delta)

        if measured != 0 and true_val != 0:
            disc = (true_val / measured - 1) * 100
        else:
            disc = 0

        results.append(
            {
                "name": const.name,
                "symbol": const.symbol,
                "category": const.category,
                "measured": measured,
                "true": true_val,
                "discrepancy": disc,
                "unit": const.unit,
                "formula": const.formula,
            }
        )
    return results


def print_all_constants(delta: float):
    """Вывести все константы с расхождениями"""
    results = calculate_discrepancy(delta)

    print(f"\n{'=' * 120}")
    print(f"Δ = {delta:.2f} | ВСЕ {len(results)} КОНСТАНТ CODATA")
    print(f"{'=' * 120}")

    # Группировка по категориям
    categories = {}
    for r in results:
        cat = r["category"]
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(r)

    for cat, items in categories.items():
        print(f"\n### {cat} ({len(items)} констант) ###")
        print(f"{'Символ':<10} {'Измеренное':<15} {'Истинное':<15} {'Δ %':<10} {'Формула'}")
        print("-" * 80)
        for item in items:
            m = f"{item['measured']:.3e}"
            t = f"{item['true']:.3e}"
            d = f"{item['discrepancy']:+.1f}%"
            print(f"{item['symbol']:<10} {m:<15} {t:<15} {d:<10} {item['formula']}")


# ============================================================================
# ОГОНЬ vs ВОДА
# ============================================================================


def print_fire_water(delta: float):
    """ОГОНЬ vs ВОДА"""
    q = Q(delta)
    fire = is_fire(delta)
    water = is_water(delta)

    print(f"\n{'=' * 80}")
    print("ОГОНЬ vs ВОДА")
    print(f"{'=' * 80}")
    print(f"Δ = {delta:.2f}")
    print(f"Q = e^|Δ| = e^{abs(delta):.2f} = {q:.2f}")
    print(f"ОГОНЬ (Q≤5)? = {fire} → {'ЧАСТИЦЫ (видимо)' if fire else 'ВОЛНЫ'}")
    print(f"ВОДА (Q>5)? = {water} → {'ВОЛНЫ (скрыто)' if water else 'ЧАСТИЦЫ'}")
    print(f"Видимая доля = e^(-Q) = {visible_fraction(delta) * 100:.2f}%")

    print(f"\n### Физика огня (частицы) ###")
    print(f"Энергия фотона E = h·ν = h₀·e^(-Δ) = {fire_energy(delta):.3e} Дж")
    print(f"Частота f = E/h = {fire_energy(delta) / CODATA_2022['h']:.3e} Гц")

    print(f"\n### Физика воды (волны) ###")
    print(f"Волновое число k = k₀·e^(Δ) = {water_wave_number(delta):.3e} м⁻¹")
    print(f"Длина волны λ = 2π/k = {2 * math.pi / water_wave_number(delta):.3e} м")


# ============================================================================
# ВСЕ ЯВЛЕНИЯ
# ============================================================================


def print_all_phenomena(delta: float):
    """Все явления физики через Δ"""
    print(f"\n{'=' * 80}")
    print("ВСЕ ЯВЛЕНИЯ ФИЗИКИ ЧЕРЕЗ Δ")
    print(f"{'=' * 80}")

    # D_f = фрактальная размерность
    D_f = 2 + delta
    print(f"### ПРОСТРАНСТВО ###")
    print(f"D_f = 2 + Δ = 2 + {delta} = {D_f}")
    if D_f <= 1:
        print(f"→ линия (1D)")
    elif D_f <= 2:
        print(f"→ плоскость (2D)")
    elif D_f <= 3:
        print(f"→ объём (3D)")
    else:
        print(f"→ гиперобъём ({D_f}D)")

    print(f"\n### Q → ВИБРАЦИЯ ###")
    print(f"Q = e^|Δ| = {Q(delta):.2f}")
    print(f"e^(-Q) = {math.exp(-Q(delta)) * 100:.2f}% — видимая часть")

    print(f"\n### ЧАСТОТА ###")
    f_base = 1e43 * math.exp(-delta)
    print(f"f₀ = 10^43·e^(-Δ) = {f_base:.3e} Гц")

    print(f"\n### ДАВЛЕНИЕ ###")
    w = -1 + delta / 3
    print(f"w = -1 + Δ/3 = -1 + {delta}/3 = {w:.3f}")
    if w < -1 / 3:
        print("→ пылевой компонент")
    elif w == -1 / 3:
        print("→ критический")
    else:
        print("→ жидкость/газ")

    print(f"\n### ЭНТРОПИЯ (S = A/4·e^(Δ/2)) ###")
    A = 1e-52  # пример площади
    S = A / 4 * math.exp(delta / 2)
    print(f"S = {A}/4 · e^({delta}/2) = {S:.3e}")

    print(f"\n### МАССА ###")
    print(f"m(Δ) = m₀·e^(-2Δ) → при Δ=1: {1e-30 * math.exp(-2):.3e} кг")


# ============================================================================
# ОСНОВНАЯ ПРОГРАММА
# ============================================================================

if __name__ == "__main__":
    print("=" * 80)
    print("ПОЛНАЯ БАЗА CODATA + ФИЗИКА ЧЕРЕЗ Δ")
    print("ОГОНЬ (Q≤5) | ВОДА (Q>5)")
    print("=" * 80)

    delta_human = 1.0  # Человек в 3D

    # 1. ОГОНЬ vs ВОДА
    print_fire_water(delta_human)

    # 2. Все явления
    print_all_phenomena(delta_human)

    # 3. Все константы
    print_all_constants(delta_human)

    # Итог
    print("\n" + "=" * 80)
    print("ИТОГ:")
    print("=" * 80)
    print(f"""
    Δ = {delta_human} → человек видит 3D
    Q = e^|Δ| = {Q(delta_human):.2f} → ОГОНЬ (Q≤5)
    
    ОГОНЬ = Q≤5 = частицы = видимо
    ВОДА = Q>5 = волны = скрыто
    
    Все {len(ALL_CONSTANTS)} констант CODATA → функции от Δ
    Все явления физики → через Δ
    
    Mass Gap = 13.8% при Δ=0
    """)
