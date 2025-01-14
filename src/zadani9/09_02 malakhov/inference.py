import knowledge_base


def initialize_kb():
    kb = knowledge_base.KnowledgeBase()

    # Add initial facts
    kb.add_fact("těstoviny", "zelené lasagne")
    kb.add_fact("omáčka", "rajčatová")
    kb.add_fact("masová příloha", "sekané maso")
    kb.add_fact("příloha", "cibule")

    # Add rules
    kb.add_rule(knowledge_base.rule_1)
    kb.add_rule(knowledge_base.rule_2)
    kb.add_rule(knowledge_base.rule_3)

    return kb

def apply_rules(kb):
    """Applies rules iteratively until no new facts can be inferred."""
    inferred = True
    while inferred:
        inferred = False
        for rule in kb.rules:
            if rule(kb):
                inferred = True
    return kb