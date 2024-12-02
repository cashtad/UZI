def get_explanation(bank, rate, reason):
    explanation = (
        f"Выбран банк: {bank['name']}.\n"
        f"Причина: {reason}\n"
        f"Процентная ставка: {rate}%\n"
        f"Дополнительные данные:\n"
        f"- Минимальный депозит: {bank['min_deposit']} CZK\n"
        f"- Максимальный депозит: {str(bank['max_deposit']) + " CZK" or 'Неограничен'} \n"
        f"- Плата за ведение счета: {bank['account_fee']} CZK/месяц\n"
    )
    return explanation
