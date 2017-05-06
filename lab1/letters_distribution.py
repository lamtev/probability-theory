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
            quiprobable_code_prob_list.append([code, 1 / len(codes)])
        self.quiprobable_code_prob = dict(quiprobable_code_prob_list)

    def make_cyrillic_code_prob(self, path_to_file: str):
        # TODO
        f = open(path_to_file, encoding='utf-8-sig')
        cyrillic_distribution_list = []
        for line in f:
            cyrillic_distribution_list.append(line.split())
            p = float(cyrillic_distribution_list[-1][-1]) / 100
            cyrillic_distribution_list[-1][-1] = p
        f.close()
        self.cyrillic_code_prob = dict(cyrillic_distribution_list)
