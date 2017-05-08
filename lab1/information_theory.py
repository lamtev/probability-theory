from math import log2


def entropy(posterior_probabilities: list) -> list:
    res = []
    for x in posterior_probabilities:
        s = 0
        for pi in x:
            if pi == 0:
                pr = 1e-12
            else:
                pr = pi
            s += pr * log2(pr)
        res.append(-s)
    return res


def information(posterior_probabilities: list, code_prob: dict) -> list:
    entrx = entropy([list(code_prob.values())])[0]
    return [entrx - x for x in entropy(posterior_probabilities)]


def k_th_letter_distribution(distribution: list, k: int) -> list:
    return [p[k] for p in [[[x[1] for x in y] for y in z] for z in distribution]]
