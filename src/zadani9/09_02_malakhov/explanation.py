# Modul: explanation.py
# Úloha: Production System
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 14.01.2025

"""
@file explanation.py
@brief Provides functions for displaying the goal and inferred facts in a production system.

@details This module contains functions that display the AND-OR graph and explain the
inferred facts in the production system. The AND-OR graph visualizes the logical structure
of the system, and the explanation function checks if the goal has been achieved and
displays the facts that were inferred through rule application.

@functions:
- display_and_or_graph: Displays a textual representation of the AND-OR graph for the goal.
- display_explanation: Displays the result of the inference process and the inferred facts.
"""

def display_and_or_graph():
    """
    @brief Displays a textual AND-OR graph for the goal of achieving "lasagne verde".

    @details The AND-OR graph shows the logical steps required to achieve the goal, starting
    with the goal and breaking it down into its necessary conditions using AND and OR operations.

    @output Prints the AND-OR graph to the console.
    """
    print("AND-OR Graph:")
    print("  Goal: pokrm = lasagne verde")
    print("    AND -> těstoviny = zelené lasagne")
    print("    AND -> omáčka = boloňská")
    print("      AND -> masová příloha = sekané maso")
    print("      AND -> příloha = cibule")
    print("      AND -> barva omáčky = červená")
    print("        OR -> omáčka = rajčatová")

def display_explanation(kb):
    """
    @brief Displays the explanation of the inference process and the goal status.

    @details This function checks whether the goal has been achieved ("pokrm = lasagne verde")
    and displays all the inferred facts from the knowledge base.

    @param kb The knowledge base instance containing inferred facts.
    @output Prints the goal status and the list of inferred facts.
    """
    # Check if goal is achieved
    if kb.get_fact("pokrm") == "lasagne verde":
        print("\nGoal achieved: pokrm = lasagne verde")
    else:
        print("\nGoal not achieved.")

    # Display inferred facts
    print("\nInferred facts:")
    for fact, value in kb.facts.items():
        print(f"{fact} = {value}")
