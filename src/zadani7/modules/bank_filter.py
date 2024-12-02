def filter_banks_by_basic_conditions(banks, deposit):
    return [bank for bank in banks if deposit >= bank["min_deposit"] and
            (bank["max_deposit"] is None or deposit <= bank["max_deposit"])]