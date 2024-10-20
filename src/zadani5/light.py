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

# Vytvoření systému
lighting_system = LightingSystem()

# Přidání faktů pro příklad (tyto hodnoty můžete měnit podle potřeby)
lighting_system.add_fact("type", "obytný prostor")
lighting_system.add_fact("area", 25)  # Plocha v m²
lighting_system.add_fact("natural_light", "ano")  # Místnost má přirozené osvětlení
lighting_system.add_fact("preferred_temp", "teplá")  # Preferovaná barevná teplota

# Přidání pravidel pro různé typy místností
lighting_system.add_rule(is_living_room, recommend_living_room_lighting)
lighting_system.add_rule(is_office, recommend_office_lighting)
lighting_system.add_rule(is_cottage, recommend_cottage_lighting)

# Použití pravidel
lighting_system.infer()

# Výpočet počtu světel
calculate_light_count(lighting_system.facts)

# Výpis všech faktů
print("Fakta systému osvětlení:", lighting_system.facts)
