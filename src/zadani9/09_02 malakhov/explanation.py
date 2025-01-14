def display_and_or_graph():
    """Displays a textual AND-OR graph."""
    print("AND-OR Graph:")
    print("  Goal: pokrm = lasagne verde")
    print("    AND -> těstoviny = zelené lasagne")
    print("    AND -> omáčka = boloňská")
    print("      AND -> masová příloha = sekané maso")
    print("      AND -> příloha = cibule")
    print("      AND -> barva omáčky = červená")
    print("        OR -> omáčka = rajčatová")


def display_explanation(kb):
    # Check if goal is achieved
    if kb.get_fact("pokrm") == "lasagne verde":
        print("\nGoal achieved: pokrm = lasagne verde")
    else:
        print("\nGoal not achieved.")

    # Display inferred facts
    print("\nInferred facts:")
    for fact, value in kb.facts.items():
        print(f"{fact} = {value}")
