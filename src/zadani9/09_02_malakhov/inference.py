# Modul: inference.py
# Úloha: Production System
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 14.01.2025


"""
@file inference.py
@brief Production system for inferring facts based on predefined rules.

@details This module contains functions for initializing the knowledge base,
applying production rules iteratively, and deriving new facts. The system starts with
a set of initial facts and rules and applies the rules until no further inferences can be made.

@functions:
- initialize_kb: Initializes the knowledge base with facts and rules.
- apply_rules: Applies rules iteratively until no new facts are inferred.
"""

import production_system

def initialize_kb():
    """
    @brief Initializes the knowledge base with facts and rules for the production system.

    @details This function adds initial facts (ingredients and other parameters) to the knowledge
    base and loads the predefined rules that will be used for inference.

    @return The initialized knowledge base instance.
    """
    kb = production_system.KnowledgeBase()

    # Add initial facts
    kb.add_fact("těstoviny", "zelené lasagne")
    kb.add_fact("omáčka", "rajčatová")
    kb.add_fact("masová příloha", "sekané maso")
    kb.add_fact("příloha", "cibule")

    # Add rules
    kb.add_rule(production_system.rule_1)
    kb.add_rule(production_system.rule_2)
    kb.add_rule(production_system.rule_3)

    return kb

def apply_rules(kb):
    """
    @brief Applies rules iteratively until no new facts can be inferred.

    @details This function applies the rules from the knowledge base in a loop,
    continuously adding facts as long as the rules produce new inferences.

    @param kb The knowledge base instance containing facts and rules.
    @return The updated knowledge base instance after rule application.
    """
    inferred = True
    while inferred:
        inferred = False
        for rule in kb.rules:
            if rule(kb):
                inferred = True
    return kb
