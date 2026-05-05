#!/usr/bin/env python3
"""
НАИВНЫЙ БИАС = ТЫ (пользователь)
================================
Ты считаешь — твой наивный биас вычисляет.
Воля думает за тебя — резонирует с Солнцем.

Давай считай!
"""

import math
import hashlib

# ============================================================================
# ТВОЙ НАИВНЫЙ БИАС (ТЫ)
# ============================================================================


class NaiveBias:
    """
    Твой наивный биас = ты
    Твое дело — считать
    Воля думает за тебя
    """

    def __init__(self, lat: float, lon: float, mass: float, height: float):
        self.lat = lat
        self.lon = lon
        self.mass = mass
        self.height = height

    def calculate_delta(self) -> float:
        """Δ из твоих параметров"""
        lat_f = abs(self.lat) / 90
        mass_f = (self.mass - 20) / 180
        height_f = (self.height - 50) / 200
        return 1.0 + lat_f * 0.3 + mass_f * 0.4 + height_f * 0.3

    def calculate_Q(self) -> float:
        """Q = e^|Δ|"""
        return math.exp(abs(self.calculate_delta()))

    def calculate_frequency(self) -> float:
        """Частота твоего биаса"""
        f_planck = 1e43  # Гц
        Q = self.calculate_Q()
        return f_planck * math.exp(-Q)

    def calculate_energy_MeV(self) -> float:
        """Энергия в МэВ"""
        freq = self.calculate_frequency()
        h_eV_s = 4.136e-15
        eV = h_eV_s * freq
        return eV / 1e6

    def full_calculate(self) -> dict:
        """Полный расчёт твоего биаса"""
        d = self.calculate_delta()
        q = self.calculate_Q()
        f = self.calculate_frequency()
        e = self.calculate_energy_MeV()

        return {
            "lat": self.lat,
            "lon": self.lon,
            "mass_kg": self.mass,
            "height_cm": self.height,
            "delta": d,
            "Q": q,
            "frequency_Hz": f,
            "energy_MeV": e,
        }


# ============================================================================
# СОЛНЦЕ
# ============================================================================


class Sun:
    """Солнце"""

    # Параметры Солнца
    MASS = 1.989e30  # кг
    TEMPERATURE = 5778  # K
    SPECTRAL_TYPE = "G2V"

    # Частота видимого света (среднее)
    VISIBLE_FREQUENCY = 5.5e14  # Гц (~550 нм)

    @staticmethod
    def get_frequency() -> float:
        """Частота Солнца (видимый свет)"""
        return Sun.VISIBLE_FREQUENCY

    @staticmethod
    def get_energy_MeV() -> float:
        """Энергия в МэВ"""
        h_eV_s = 4.136e-15
        eV = h_eV_s * Sun.VISIBLE_FREQUENCY
        return eV / 1e6

    @staticmethod
    def get_delta_estimate() -> float:
        """Δ Солнца (приблизительно)"""
        # Солнце = плазма, почти Δ=0
        return 0.1


# ============================================================================
# РЕЗОНАНС: ТЫ ↔ СОЛНЦЕ
# ============================================================================


def calculate_resonance(
    your_lat: float, your_lon: float, your_mass: float, your_height: float
) -> dict:
    """
    Резонанс между твоим биасом и Солнцем
    """

    print("=" * 80)
    print("ТВОЙ НАИВНЫЙ БИАС ↔ СОЛНЦЕ")
    print("=" * 80)

    # Твой расчёт
    you = NaiveBias(your_lat, your_lon, your_mass, your_height)
    your_data = you.full_calculate()

    print("\n### ТВОЙ БИАС (ты считаешь) ###")
    print(f"Параметры: lat={your_lat}, lon={your_lon}, mass={your_mass}кг, height={your_height}см")
    print(f"Δ = {your_data['delta']:.4f}")
    print(f"Q = {your_data['Q']:.4f}")
    print(f"Частота = {your_data['frequency_Hz']:.4e} Гц")
    print(f"Энергия = {your_data['energy_MeV']:.4f} МэВ")

    # Солнце
    sun_freq = Sun.get_frequency()
    sun_energy = Sun.get_energy_MeV()
    sun_delta = Sun.get_delta_estimate()

    print("\n### СОЛНЦЕ (Воля думает) ###")
    print(f"Частота = {sun_freq:.4e} Гц")
    print(f"Энергия = {sun_energy:.6f} МэВ")
    print(f"Δ ≈ {sun_delta}")

    # Резонанс
    freq_ratio = your_data["frequency_Hz"] / sun_freq
    energy_ratio = your_data["energy_MeV"] / sun_energy

    # Проверяем: твоя частота резонирует с Солнцем?
    # Резонанс = когда частоты близки или кратны

    resonance = abs(math.log10(freq_ratio)) < 1  # в пределах порядка

    print("\n### РЕЗОНАНС ###")
    print(f"Отношение частот: {freq_ratio:.4e}")
    print(f"Отношение энергий: {energy_ratio:.4e}")
    print(f"Резонанс: {'ДА' if resonance else 'НЕТ'}")

    # Ответ на вопрос "Солнце — это то, что я думаю?"
    if resonance:
        answer = "ДА — твоя Воля резонирует с Солнцем"
    else:
        answer = "НЕТ — твоя Воля НЕ резонирует с Солнцем"

    print(f"\n### ОТВЕТ ###")
    print(f"Солнце — это {answer}")

    return {
        "you": your_data,
        "sun": {
            "frequency_Hz": sun_freq,
            "energy_MeV": sun_energy,
            "delta": sun_delta,
        },
        "resonance": resonance,
        "answer": answer,
    }


# ============================================================================
# ПРИМЕРЫ РАЗНЫХ ЛЮДЕЙ
# ============================================================================


def examples():
    """Примеры разных людей"""

    print("\n" + "=" * 80)
    print("ПРИМЕРЫ РАЗНЫХ БИАСОВ")
    print("=" * 80)

    people = [
        {"lat": 55, "lon": 37, "mass": 80, "height": 180, "name": "Москва"},
        {"lat": 40, "lon": -74, "mass": 70, "height": 170, "name": "Нью-Йорк"},
        {"lat": 0, "lon": 0, "mass": 60, "height": 165, "name": "Экватор"},
        {"lat": -33, "lon": 151, "mass": 90, "height": 185, "name": "Сидней"},
        {"lat": 70, "lon": 30, "mass": 100, "height": 190, "name": "Мурманск"},
    ]

    sun_freq = Sun.get_frequency()

    print(f"\nЧастота Солнца: {sun_freq:.4e} Гц")
    print("-" * 60)

    for p in people:
        you = NaiveBias(p["lat"], p["lon"], p["mass"], p["height"])
        f = you.calculate_frequency()
        ratio = f / sun_freq

        # Проверяем близость
        is_close = abs(math.log10(ratio)) < 1.5

        print(f"\n{p['name']}:")
        print(f"  Δ = {you.calculate_delta():.3f}")
        print(f"  Частота = {f:.4e} Гц")
        print(f"  Отношение = {ratio:.2e}")
        print(f"  Близко к Солнцу: {'✓' if is_close else '✗'}")


# ============================================================================
# ОСНОВНАЯ ПРОГРАММА
# ============================================================================


if __name__ == "__main__":
    # Твой наивный биас (давай посчитаем!)
    result = calculate_resonance(your_lat=55.7, your_lon=37.6, your_mass=80, your_height=180)

    # Примеры
    examples()

    print("\n" + "=" * 80)
    print("ТВОЁ ДЕЛО — СЧИТАТЬ")
    print("ВОЛЯ ДУМАЕТ ЗА ТЕБЯ")
    print("=" * 80)
