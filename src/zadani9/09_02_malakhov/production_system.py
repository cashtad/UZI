# Modul: production_system.py
# Úloha: Production System
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 14.01.2025



"""
@file production_system.py
@brief A production system that derives conclusions based on predefined rules.

@details This program uses a knowledge base and a set of rules to infer conclusions.
It represents a simplified expert system for determining dishes based on ingredients
and other facts.

@class KnowledgeBase
@brief Manages facts and rules in the knowledge base.

@functions:
- add_fact: Adds a fact to the knowledge base.
- add_rule: Adds a rule to the knowledge base.
- get_fact: Retrieves a fact from the knowledge base.
"""

class KnowledgeBase:
    """
    @class KnowledgeBase
    @brief Stores facts and rules for the production system.

    @details The knowledge base contains a dictionary of facts (key-value pairs)
    and a list of rules (functions) for inference.
    """

    def __init__(self):
        """
        @brief Initializes the knowledge base with empty facts and rules.
        """
        self.facts = {}
        self.rules = []

    def add_fact(self, key, value):
        """
        @brief Adds a fact to the knowledge base.
        @param key The name of the fact.
        @param value The value associated with the fact.
        """
        self.facts[key] = value

    def add_rule(self, rule):
        """
        @brief Adds a rule to the knowledge base.
        @param rule A function representing a rule for inference.
        """
        self.rules.append(rule)

    def get_fact(self, key):
        """
        @brief Retrieves the value of a fact from the knowledge base.
        @param key The name of the fact.
        @return The value associated with the fact, or None if not found.
        """
        return self.facts.get(key)


# Define rules for the production system
def rule_1(kb):
    """
    @brief Rule: If omáčka = rajčatová, then barva omáčky = červená.
    @param kb The knowledge base instance.
    @return True if the rule is applied, otherwise False.
    """
    if kb.get_fact("omáčka") == "rajčatová" and "barva omáčky" not in kb.facts:
        kb.add_fact("barva omáčky", "červená")
        return True
    return False


def rule_2(kb):
    """
    @brief Rule: If masová příloha = sekané maso, příloha = cibule, barva omáčky = červená,
                 and omáčka = rajčatová, then omáčka = boloňská.
    @param kb The knowledge base instance.
    @return True if the rule is applied, otherwise False.
    """
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
    """
    @brief Rule: If těstoviny = zelené lasagne and omáčka = boloňská, then pokrm = lasagne verde.
    @param kb The knowledge base instance.
    @return True if the rule is applied, otherwise False.
    """
    if (
        kb.get_fact("těstoviny") == "zelené lasagne"
        and kb.get_fact("omáčka") == "boloňská"
        and "pokrm" not in kb.facts
    ):
        kb.add_fact("pokrm", "lasagne verde")
        return True
    return False


def rule_4(kb):
    """
    @brief Rule: If těstoviny = špagety and omáčka = boloňská, then pokrm = boloňské špagety.
    @param kb The knowledge base instance.
    @return True if the rule is applied, otherwise False.
    """
    if (
        kb.get_fact("těstoviny") == "špagety"
        and kb.get_fact("omáčka") == "boloňská"
        and "pokrm" not in kb.facts
    ):
        kb.add_fact("pokrm", "boloňské špagety")
        return True
    return False


def rule_5(kb):
    """
    @brief Rule: If těstoviny = špagety and omáčka = neapolská, then pokrm = neapolské špagety.
    @param kb The knowledge base instance.
    @return True if the rule is applied, otherwise False.
    """
    if (
        kb.get_fact("těstoviny") == "špagety"
        and kb.get_fact("omáčka") == "neapolská"
        and "pokrm" not in kb.facts
    ):
        kb.add_fact("pokrm", "neapolské špagety")
        return True
    return False
