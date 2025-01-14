# Modul: main.py
# Úloha: Production System
# Autor: Leonid Malakhov
# E-mail: malakhov@students.zcu.cz
# Datum: 14.01.2025

import explanation
import inference

if __name__ == "__main__":
    # Display AND-OR graph
    explanation.display_and_or_graph()

    # Initialize knowledge base
    kb = inference.initialize_kb()


    # Apply rules
    kb = inference.apply_rules(kb)

    explanation.display_explanation(kb)
