class KnowledgeBase:
    """Stores facts and rules for the production system."""
    def __init__(self):
        self.facts = {}
        self.rules = []

    def add_fact(self, key, value):
        """Adds a fact to the knowledge base."""
        self.facts[key] = value

    def add_rule(self, rule):
        """Adds a rule to the knowledge base."""
        self.rules.append(rule)

    def get_fact(self, key):
        """Gets the value of a fact."""
        return self.facts.get(key)




def rule_1(kb):
    """if omáčka = rajčatová then barva omáčky = červená"""
    if kb.get_fact("omáčka") == "rajčatová" and "barva omáčky" not in kb.facts:
        kb.add_fact("barva omáčky", "červená")
        return True
    return False


def rule_2(kb):
    """if masová příloha = sekané maso and příloha = cibule and barva omáčky = červená then omáčka = boloňská"""
    if (
        kb.get_fact("masová příloha") == "sekané maso"
        and kb.get_fact("příloha") == "cibule"
        and kb.get_fact("barva omáčky") == "červená"
        and kb.get_fact("omáčka") == "rajčatová"
    ):
        kb.add_fact("omáčka", "boloňská")
        return True
    return False


def rule_3(kb):
    """if těstoviny = zelené lasagne and omáčka = boloňská then pokrm = lasagne verde"""
    if (
        kb.get_fact("těstoviny") == "zelené lasagne"
        and kb.get_fact("omáčka") == "boloňská"
        and "pokrm" not in kb.facts
    ):
        kb.add_fact("pokrm", "lasagne verde")
        return True
    return False

def rule_4(kb):
    """if testoviny = spagety and omacka = bolonska then pokrm = bolonske spagety"""
    if (
        kb.get_fact("těstoviny") == "špagety"
        and kb.get_fact("omáčka") == "boloňská"
        and "pokrm" not in kb.facts
    ):
        kb.add_fact("pokrm", "boloňské špagety")
        return True
    return False

def rule_5(kb):
    """if testoviny = spagety and omacka = neapolska then pokrm = neapolske spagety"""
    if (
        kb.get_fact("těstoviny") == "špagety"
        and kb.get_fact("omáčka") == "neapolská"
        and "pokrm" not in kb.facts
    ):
        kb.add_fact("pokrm", "neapolské špagety")
        return True
    return False