def obfuscate_credit_card_number(number):
    return number[:4] + "*" * 8 + number[-4:]


def obfuscate_credit_card_cvv(cvv):
    return "*" * len(cvv)
