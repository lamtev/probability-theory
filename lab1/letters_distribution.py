from alphabet import Alphabet


class LettersDistribution:
    alphabet: Alphabet
    quiprobable_code_prob: dict = {}
    cyrillic_code_prob: dict = {}

    def __init__(self, alphabet: Alphabet, path_to_file: str):
        self.alphabet = alphabet
        self.make_quiprobable_code_prob()
        self.make_cyrillic_code_prob(path_to_file)

    def make_quiprobable_code_prob(self):
        quiprobable_code_prob_list = []
        codes = self.alphabet.code_letter.keys()
        for code in codes:
            quiprobable_code_prob_list.append((code, 1 / len(codes)))
        self.quiprobable_code_prob = dict(quiprobable_code_prob_list)

    def make_cyrillic_code_prob(self, path_to_file: str):
        f = open(path_to_file, encoding='utf-8-sig')
        cyrillic_distribution_list = []
        for line in f:
            cyrillic_distribution_list.append(line.split())
            p = float(cyrillic_distribution_list[-1][-1]) / 100 * 65 / 87
            cyrillic_distribution_list[-1][-1] = p
        f.close()
        for letter in self.alphabet.letter_code.keys():
            if not contains(cyrillic_distribution_list, letter):
                cyrillic_distribution_list.append((letter, 1 / 87))
        updated = [(self.alphabet.letter_code.get(pair[0]), pair[1]) for pair in cyrillic_distribution_list]
        self.cyrillic_code_prob = dict(updated)


def contains(l: list, x):
    for el in l:
        if el[0] == x:
            return True
    return False
