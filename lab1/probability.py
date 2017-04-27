def p_of_receiving_y_if_x_was_sent(y: str, x: str, q: float) -> float:
    y_int = int(y, 2)
    x_int = int(x, 2)
    number_of_symbols = len(y)
    number_of_q = str(bin(y_int ^ x_int)).count('1')
    return q ** number_of_q * (1 - q) ** (number_of_symbols - number_of_q)


def p_of_receiving_y(y: str, code_prob: dict, q: float) -> float:
    prob = 0
    for code in code_prob.keys():
        prob += code_prob.get(code) * p_of_receiving_y_if_x_was_sent(y, code, q)
    return prob


def p_posterior(x: str, y: str, code_prob: dict, q: float, p_y: float = 0) -> float:
    if p_y is 0:
        p_y = p_of_receiving_y(y, code_prob, q)

    return p_of_receiving_y_if_x_was_sent(y, x, q) * code_prob.get(x) / p_y
