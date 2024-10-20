# Autor: Leonid Malakhov
# Tento program je jednoduchý pravidlově orientovaný systém pro návrh osvětlení.
# Uživatel může zadat typ místnosti (obytný prostor, kancelář, chata), plochu místnosti,
# zda má místnost přirozené osvětlení, a preferovanou barevnou teplotu.
# Program vypočítá doporučenou úroveň osvětlení a počet potřebných svítidel na základě těchto informací.
# Cílem programu je usnadnit návrh osvětlení pro různé typy prostorů.

# Programová instrukce pro uživatele:
# 1. Zadejte typ místnosti (např. "obytný prostor", "kancelář", "chata").
# 2. Zadejte plochu místnosti v m².
# 3. Odpovězte, zda místnost má přirozené osvětlení (ano/ne).
# 4. Zadejte preferovanou barevnou teplotu (např. "teplá", "neutrální", "studená").
# Program poté poskytne doporučení ohledně osvětlení a vypočítá počet potřebných světel.

class LightingSystem:
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, key, value):
        """Přidat fakt do systému"""
        self.facts[key] = value

    def add_rule(self, condition, action):
        """Přidat pravidlo do systému"""
        self.rules.append((condition, action))

    def infer(self):
        """Mechanismus závěrů pro aplikaci pravidel"""
        for condition, action in self.rules:
            if condition(self.facts):
                action(self.facts)

# Podmínky (funkce pro ověření faktů)
def is_living_room(facts):
    """Ověřit, zda se jedná o obytný prostor"""
    return facts["type"] == "obytný prostor"

def is_office(facts):
    """Ověřit, zda se jedná o kancelář"""
    return facts["type"] == "kancelář"

def is_cottage(facts):
    """Ověřit, zda se jedná o chatu"""
    return facts["type"] == "chata"

def has_natural_light(facts):
    """Ověřit, zda má místnost přirozené osvětlení"""
    return facts.get("natural_light", "ne") == "ano"

# Akce (funkce poskytující doporučení pro osvětlení)
def recommend_living_room_lighting(facts):
    """Doporučit osvětlení pro obytný prostor"""
    facts["recommended_lux"] = 300  # Doporučená úroveň osvětlení pro obytný prostor
    facts["recommended_temp"] = "teplá" if has_natural_light(facts) else "neutrální"
    print(f"Doporučená úroveň osvětlení pro obytný prostor: {facts['recommended_lux']} luxů")
    print(f"Doporučená barevná teplota: {facts['recommended_temp']}")

def recommend_office_lighting(facts):
    """Doporučit osvětlení pro kancelář"""
    facts["recommended_lux"] = 500  # Doporučená úroveň osvětlení pro kancelář
    facts["recommended_temp"] = "neutrální" if has_natural_light(facts) else "studená"
    print(f"Doporučená úroveň osvětlení pro kancelář: {facts['recommended_lux']} luxů")
    print(f"Doporučená barevná teplota: {facts['recommended_temp']}")

def recommend_cottage_lighting(facts):
    """Doporučit osvětlení pro chatu"""
    facts["recommended_lux"] = 200  # Doporučená úroveň osvětlení pro chatu
    facts["recommended_temp"] = "teplá"  # Pro chatu je preferována teplá barevná teplota
    print(f"Doporučená úroveň osvětlení pro chatu: {facts['recommended_lux']} luxů")
    print(f"Doporučená barevná teplota: {facts['recommended_temp']}")

# Funkce pro výpočet počtu světel
def calculate_light_count(facts):
    """Vypočítat potřebný počet světel"""
    area = facts["area"]  # Plocha místnosti v m²
    lux_needed = facts["recommended_lux"]  # Doporučené osvětlení v luxech
    light_power_per_unit = 800  # Výkon jednoho svítidla v lumenech
    lux_to_lumen_factor = 1.5  # Převodní koeficient lux -> lumen na m²
    total_lumens_needed = area * lux_needed * lux_to_lumen_factor  # Celkový potřebný výkon osvětlení
    light_count = total_lumens_needed / light_power_per_unit  # Počet světel
    facts["light_count"] = int(round(light_count))  # Zaokrouhlení počtu světel
    print(f"Požadovaný počet světel: {facts['light_count']}")

# Hlavní programová část, kde se zadají vstupní data uživatelem
print("Vítejte v programu pro návrh osvětlení.")
print("Postupujte podle instrukcí a zadejte požadované informace.\n")

# Uživatelský vstup
room_type = input("Zadejte typ místnosti (obytný prostor, kancelář, chata): ").strip().lower()
area = float(input("Zadejte plochu místnosti v m²: "))
natural_light = input("Má místnost přirozené osvětlení? (ano/ne): ").strip().lower()
preferred_temp = input("Zadejte preferovanou barevnou teplotu (teplá, neutrální, studená): ").strip().lower()

# Vytvoření systému
lighting_system = LightingSystem()

# Přidání faktů z uživatelského vstupu
lighting_system.add_fact("type", room_type)
lighting_system.add_fact("area", area)  # Plocha v m²
lighting_system.add_fact("natural_light", natural_light)  # Přirozené osvětlení (ano/ne)
lighting_system.add_fact("preferred_temp", preferred_temp)  # Preferovaná barevná teplota

# Přidání pravidel pro různé typy místností
lighting_system.add_rule(is_living_room, recommend_living_room_lighting)
lighting_system.add_rule(is_office, recommend_office_lighting)
lighting_system.add_rule(is_cottage, recommend_cottage_lighting)

# Použití pravidel
lighting_system.infer()

# Výpočet počtu světel
calculate_light_count(lighting_system.facts)

# Výpis všech faktů
print("\nFakta systému osvětlení:", lighting_system.facts)
