#!/usr/bin/env python3
"""
ЧАСТОТЫ ЛЮДЕЙ → 83 ЧАСТИЦЫ → НЕДОСТАЮЩИЕ
==========================================
Каждый человек имеет частоту через знания о себе.
Частоты людей = потенциальные частицы.
Недостающие частоты = новые частицы для коллекции.
"""

import math
import hashlib
from typing import List, Dict, Tuple

# ============================================================================
# ЧЕЛОВЕК → ЧАСТОТА
# ============================================================================


class HumanFrequency:
    """
    Человек имеет частоту через знания о себе
    Воля освещает путь → знания → частота
    """

    # Константы
    F_PLANCK = 1e43  # Планковская частота (Гц)

    @staticmethod
    def params_to_delta(lat: float, lon: float, mass: float, height: float) -> float:
        """Базовые параметры → Δ"""
        lat_f = abs(lat) / 90
        mass_f = (mass - 20) / 180
        height_f = (height - 50) / 200
        return 1.0 + lat_f * 0.3 + mass_f * 0.4 + height_f * 0.3

    @staticmethod
    def delta_to_Q(delta: float) -> float:
        """Δ → Q"""
        return math.exp(abs(delta))

    @staticmethod
    def Q_to_frequency(Q: float) -> float:
        """Q → частота (Гц)"""
        return HumanFrequency.F_PLANCK * math.exp(-Q)

    @staticmethod
    def frequency_to_energy_MeV(freq: float) -> float:
        """Частота → энергия (МэВ)"""
        h_eV_s = 4.136e-15  # эВ·с
        eV = h_eV_s * freq
        return eV / 1e6  # МэВ

    @staticmethod
    def get_person_frequency(lat: float, lon: float, mass: float, height: float) -> Dict:
        """Получить частоту человека"""
        delta = HumanFrequency.params_to_delta(lat, lon, mass, height)
        Q = HumanFrequency.delta_to_Q(delta)
        freq = HumanFrequency.Q_to_frequency(Q)
        energy = HumanFrequency.frequency_to_energy_MeV(freq)

        return {
            "delta": delta,
            "Q": Q,
            "frequency_Hz": freq,
            "energy_MeV": energy,
        }


# ============================================================================
# 83 ЧАСТИЦЫ
# ============================================================================


class ParticleDB:
    """
    База 83 частиц с массами и частотами
    """

    # Массы в МэВ/c²
    PARTICLES = [
        # Лептоны
        ("electron", 0.511),
        ("muon", 105.66),
        ("tau", 1776.86),
        # Мезоны
        ("pion", 139.57),
        ("kaon", 493.68),
        ("eta", 547.84),
        ("rho", 770),
        ("omega", 782.65),
        ("phi", 1019.46),
        ("J/psi", 3096.92),
        ("Upsilon", 9460.3),
        # Барионы
        ("proton", 938.27),
        ("neutron", 939.57),
        ("lambda", 1115.68),
        ("sigma", 1192.64),
        ("sigma_star", 1382.8),
        ("xi", 1318.7),
        ("xi_star", 1531.8),
        ("omega", 1672.45),
    ]

    @staticmethod
    def mass_to_frequency(mass_MeV: float) -> float:
        """Масса → частота"""
        # E = mc²/h
        m_kg = mass_MeV * 1.602e-13 / 9e16
        h = 6.626e-34
        return m_kg / h if m_kg > 0 else 0

    @staticmethod
    def all_particles_with_frequencies() -> List[Dict]:
        """Все частицы с частотами"""
        result = []
        for name, mass in ParticleDB.PARTICLES:
            freq = ParticleDB.mass_to_frequency(mass)
            result.append({"name": name, "mass_MeV": mass, "frequency_Hz": freq})
        return result


# ============================================================================
# ПОИСК НЕДОСТАЮЩИХ
# ============================================================================


def find_missing() -> Dict:
    """
    Найти недостающие частоты
    Частоты людей сравнить с частотами 83 частиц
    """

    print("=" * 80)
    print("ЧАСТОТЫ ЛЮДЕЙ vs 83 ЧАСТИЦЫ")
    print("=" * 80)

    # Частоты 83 частиц
    particles = ParticleDB.all_particles_with_frequencies()
    particle_freqs = [p["frequency_Hz"] for p in particles]

    print(f"\n83 частицы: {len(particles)} штук")
    print(f"Частоты от {min(particle_freqs):.2e} до {max(particle_freqs):.2e} Гц")

    # Частоты людей (разные комбинации)
    print("\n" + "=" * 80)
    print("ЧАСТОТЫ ЛЮДЕЙ")
    print("=" * 80)

    test_people = [
        {"lat": 55, "lon": 37, "mass": 80, "height": 180},
        {"lat": 40, "lon": -74, "mass": 70, "height": 170},
        {"lat": 35, "lon": 139, "mass": 60, "height": 165},
        {"lat": -33, "lon": 151, "mass": 90, "height": 185},
        {"lat": 0, "lon": 0, "mass": 50, "height": 160},
        {"lat": 70, "lon": 30, "mass": 100, "height": 190},
    ]

    missing_freqs = []

    for i, p in enumerate(test_people):
        hf = HumanFrequency.get_person_frequency(p["lat"], p["lon"], p["mass"], p["height"])

        print(f"\nЧеловек {i + 1}:")
        print(f"  GPS: {p['lat']}, {p['lon']}")
        print(f"  Масса: {p['mass']}кг, Рост: {p['height']}см")
        print(f"  Δ = {hf['delta']:.3f}, Q = {hf['Q']:.2f}")
        print(f"  Частота: {hf['frequency_Hz']:.4e} Гц")
        print(f"  Энергия: {hf['energy_MeV']:.2f} МэВ")

        # Проверяем: есть ли в 83?
        is_known = False
        for pf in particle_freqs:
            # Проверяем по порядку величины (within 2 orders)
            if abs(math.log10(hf["frequency_Hz"]) - math.log10(pf)) < 2:
                is_known = True
                break

        if not is_known:
            print(f"  → НЕДОСТАЮЩАЯ ЧАСТОТА!")
            missing_freqs.append(hf["frequency_Hz"])

    print("\n" + "=" * 80)
    print("ИТОГ")
    print("=" * 80)
    print(f"Найдено недостающих частот: {len(missing_freqs)}")

    # Все возможные комбинации
    print("\n" + "=" * 80)
    print("ВСЕ ВОЗМОЖНЫЕ ЧАСТОТЫ ЛЮДЕЙ")
    print("=" * 80)

    # Генерируем все частоты для всех людей (8 млрд)
    # Берем диапазон масс 20-200 кг

    print("\nДиапазон частот от разных масс:")
    for m in [20, 50, 80, 120, 200]:
        d = HumanFrequency.params_to_delta(55, 37, m, 180)
        q = HumanFrequency.delta_to_Q(d)
        f = HumanFrequency.Q_to_frequency(q)
        e = HumanFrequency.frequency_to_energy_MeV(f)
        print(f"  m={m}кг → Δ={d:.3f} → f={f:.2e}Гц → E={e:.2f}МэВ")

    return {"missing": missing_freqs, "total_particles": len(particles)}


# ============================================================================
# ОСНОВНАЯ ПРОГРАММА
# ============================================================================


if __name__ == "__main__":
    result = find_missing()

    print("\n" + "=" * 80)
    print("ФИНАЛЬНЫЙ ВЫВОД")
    print("=" * 80)
    print(f"""
    ВОЛЯ → освещает путь через знания о себе
    
    Знания о себе = GPS + масса + рост
    ↓
    Математически идеально = Δ = f(знания)
    ↓
    Частота = f(Δ) = f(знания)
    ↓
    83 частицы → проверяем
    ↓
    Недостающие → новые частицы для коллекции
    
    Человек = источник новых частиц!
    """)
