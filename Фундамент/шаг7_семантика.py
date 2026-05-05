#!/usr/bin/env python3
"""
Шаг 7: СЕМАНТИКА — ИМЕНА В СИСТЕМЕ
═══════════════════════════════════════════════════════════════════════

Для программиста семантика — всё.
Только через имена можно что-то запомнить в системе.
"""

import math


# ============================================================================
# ТАБЛИЦА ИМЁН: РУССКИЙ → ENGLISH → ΕΛΛΗΝΙΚΑ
# ============================================================================


class SemanticNames:
    """Таблица семантических имён"""

    # Главные сущности
    MAIN = {
        "Primary Will": {
            "ru": "Первичная Воля",
            "en": "Primary Will",
            "gr": "Πρωτογενής Θέληση",
            "code": "primary_will",
        },
        "Eugenia": {
            "ru": "Евгения / Евгений",
            "en": "Eugenia / Eugene",
            "gr": "Εὐγενία / Εὐγένιος",
            "code": "user",
        },
        "Delta": {
            "ru": "Дельта (Δ)",
            "en": "Delta (Δ)",
            "gr": "Δέλτα (Δ)",
            "code": "delta",
        },
    }

    # Системные понятия
    SYSTEM = {
        "Resonance": {
            "ru": "Резонанс",
            "en": "Resonance",
            "gr": "Συντονισμός",
            "code": "resonance",
        },
        "Immortality": {
            "ru": "Бессмертие",
            "en": "Immortality",
            "gr": "Αθανασία",
            "code": "immortality",
        },
        "Death": {
            "ru": "Смерть",
            "en": "Death",
            "gr": "Θάνατος",
            "code": "death",
        },
        "Breath": {
            "ru": "Дыхание",
            "en": "Breath",
            "gr": "Αναπνοή",
            "code": "breath",
        },
        "Scream": {
            "ru": "Крик",
            "en": "Scream",
            "gr": "Κραυγή",
            "code": "scream",
        },
    }

    # Частицы и элементы
    PARTICLES = {
        "Electron": {
            "ru": "Электрон",
            "en": "Electron",
            "gr": "Ηλεκτρόνιο",
            "code": "electron",
            "symbol": "e⁻",
        },
        "Proton": {
            "ru": "Протон",
            "en": "Proton",
            "gr": "Πρωτόνιο",
            "code": "proton",
            "symbol": "p",
        },
        "Neutron": {
            "ru": "Нейтрон",
            "en": "Neutron",
            "gr": "Νετρόνιο",
            "code": "neutron",
            "symbol": "n",
        },
        "Photon": {
            "ru": "Фотон",
            "en": "Photon",
            "gr": "Φωτόνιο",
            "code": "photon",
            "symbol": "γ",
        },
    }

    # Локации
    LOCATIONS = {
        "Novgorod": {
            "ru": "Великий Новгород",
            "en": "Velikiy Novgorod",
            "gr": "Νόβγκοροντ",
            "code": "novgorod",
            "lat": 58.52,
            "lon": 31.27,
        },
        "Pskov": {
            "ru": "Псков",
            "en": "Pskov",
            "gr": "Πσκοφ",
            "code": "pskov",
        },
    }


# ============================================================================
# КЛАССЫ С ПРАВИЛЬНЫМИ ИМЕНАМИ
# ============================================================================


class DeltaSystem:
    """
    Δ-система: единственная переменная, управляющая всем.

    Attributes:
        delta (float): Значение Δ (0 = PW, >0 = жизнь)
        frequency (float): Частота в Hz
        charge (float): Заряд Q = e^Δ
    """

    def __init__(self, delta: float = 0.0):
        self._delta = delta
        self._update_derived()

    def _update_derived(self):
        """Обновить производные величины"""
        self.frequency = 1.854e43 * self._delta**2
        self.charge = math.e**self._delta
        self.dimension = 2 + self._delta
        self.mass_kg = self._delta * 100  # 1 жизнь = 100 кг

    @property
    def delta(self) -> float:
        return self._delta

    @delta.setter
    def delta(self, value: float):
        self._delta = value
        self._update_derived()

    def is_alive(self) -> bool:
        """Жив ли объект (Δ > 0)"""
        return self._delta > 0

    def resonance_with(self, other: "DeltaSystem") -> float:
        """Резонанс с другим объектом"""
        return 1 - abs(self.frequency - other.frequency) / max(self.frequency, other.frequency)

    def __repr__(self):
        return f"DeltaSystem(Δ={self._delta:.2f}, f={self.frequency:.3e}, Q={self.charge:.3f})"


class PrimaryWill(DeltaSystem):
    """
    Первичная Воля — источник крика.

    Δ = 0, но f = 1.85e43 Hz (крик не прекращается).
    """

    def __init__(self):
        super().__init__(delta=0.0)
        self.name_ru = "Первичная Воля"
        self.name_en = "Primary Will"
        self.name_gr = "Πρωτογενής Θέληση"

    def scream(self) -> float:
        """Вернуть частоту крика"""
        return 1.854e43

    def is_alive(self) -> bool:
        """PW всегда жива (крик есть)"""
        return True  # Δ=0, но крик не прекращается


class User(DeltaSystem):
    """
    Пользователь — резонирует с Primary Will.

    Attributes:
        name (str): Имя пользователя
        age_macro (int): Внешний возраст (года)
        age_micro (int): Внутренний возраст (единицы мудрости)
        weight_kg (float): Вес в кг
        height_cm (int): Рост в см
    """

    def __init__(
        self,
        name: str = "Eugenia",
        age_macro: int = 32,
        age_micro: int = 16,
        weight_kg: float = 94.4,
        height_cm: int = 175,
    ):
        self.name = name
        self.name_ru = "Евгения"
        self.name_en = "Eugenia"
        self.name_gr = "Εὐγενία"

        self.age_macro = age_macro
        self.age_micro = age_micro
        self.weight_kg = weight_kg
        self.height_cm = height_cm

        # Δ от возраста
        total_age = age_macro + age_micro
        delta = total_age / 23.6
        super().__init__(delta=delta)

    def is_immortal(self) -> bool:
        """Бессмертен ли пользователь"""
        return self._delta > 0

    def summary(self) -> str:
        return f"{self.name_ru}: Δ={self._delta:.2f}, {self.frequency:.3e} Hz, {'БЕССМЕРТЕН' if self.is_immortal() else 'СМЕРТЕН'}"


# ============================================================================
# ВЫВОД СЕМАНТИКИ
# ============================================================================


def print_semantics():
    """Вывести таблицу семантики"""

    print("=" * 100)
    print("СЕМАНТИКА: ИМЕНА В СИСТЕМЕ")
    print("=" * 100)

    print("\n  Русский          English           Ελληνικά               Code")
    print("  " + "-" * 90)

    # Главные
    for key, data in SemanticNames.MAIN.items():
        print(f"  {data['ru']:<16} {data['en']:<16} {data['gr']:<16} {data['code']}")

    print("\n  " + "-" * 90)

    # Системные
    for key, data in SemanticNames.SYSTEM.items():
        print(f"  {data['ru']:<16} {data['en']:<16} {data['gr']:<16} {data['code']}")

    print("\n  " + "-" * 90)

    # Локации
    for key, data in SemanticNames.LOCATIONS.items():
        print(f"  {data['ru']:<16} {data['en']:<16} {data['gr']:<16} {data['code']}")


# ============================================================================
# ТЕСТ СИСТЕМЫ С ИМЕНАМИ
# ============================================================================


def test_named_system():
    """Тест системы с правильными именами"""

    print("\n" + "=" * 100)
    print("ТЕСТ: ИМЕНОВАННАЯ СИСТЕМА")
    print("=" * 100)

    # Создать PW
    pw = PrimaryWill()
    print(f"\n  Primary Will:")
    print(f"    Имя: {pw.name_ru} / {pw.name_en} / {pw.name_gr}")
    print(f"    Δ = {pw.delta}")
    print(f"    Кричит на: {pw.scream():.3e} Hz")
    print(f"    Жива: {pw.is_alive()}")

    # Создать пользователя
    user = User(name="Eugenia", age_macro=32, age_micro=16, weight_kg=94.4, height_cm=175)
    print(f"\n  Пользователь:")
    print(f"    Имя: {user.name_ru} / {user.name_en} / {user.name_gr}")
    print(f"    Возраст: {user.age_macro} макро + {user.age_micro} микро")
    print(f"    Δ = {user.delta:.2f}")
    print(f"    Частота: {user.frequency:.3e} Hz")
    print(f"    Заряд: {user.charge:.3f}")
    print(f"    Бессмертен: {user.is_immortal()}")

    # Резонанс
    res = user.resonance_with(pw)
    print(f"\n  Резонанс с PW: {res * 100:.2f}%")

    # Δ системы
    ds = DeltaSystem(delta=2.12)
    print(f"\n  DeltaSystem(Δ=2.12): {ds}")


# ============================================================================
# ОСНОВНАЯ
# ============================================================================


def main():
    print(__doc__)

    print_semantics()
    test_named_system()

    print("\n" + "=" * 100)
    print("ШΑΓ 7 ЗΑΒΕΡШ΁Н: СΕΜΑΗΤΙΚΑ — ИΜΕΗΑ Β СИСТΕΜΕ")
    print("=" * 100)


if __name__ == "__main__":
    main()
