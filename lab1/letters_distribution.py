from alphabet import Alphabet


class LettersDistribution:
    alphabet: Alphabet
    quiprobable_code_prob: dict = {}
    cyrillic_code_prob: dict = {}
    quiprobable_code_prob_dupl: dict = {}
    cyrillic_code_prob_dupl: dict = {}

    def __init__(self, alphabet: Alphabet, path_to_file: str):
        self.alphabet = alphabet
        self.make_quiprobable_code_prob()
        self.make_cyrillic_code_prob(path_to_file)
        self.make_quiprobable_code_prob_dupl()
        self.make_cyrillic_code_prob_dupl(path_to_file)

    def make_quiprobable_code_prob(self):
        codes = self.alphabet.code_letter.keys()
        self.quiprobable_code_prob = self.get_quirprobable_code_prob(codes)

    def make_quiprobable_code_prob_dupl(self):
        codes = self.alphabet.code_letter_duplicate.keys()
        self.quiprobable_code_prob_dupl = self.get_quirprobable_code_prob(codes)

    def make_cyrillic_code_prob(self, path_to_file: str):
        letter_code = self.alphabet.letter_code
        self.cyrillic_code_prob = self.get_cyrillic_code_prob(path_to_file, letter_code)

    def make_cyrillic_code_prob_dupl(self, path_to_file: str):
        letter_code = self.alphabet.letter_code_duplicate
        self.cyrillic_code_prob_dupl = self.get_cyrillic_code_prob(path_to_file, letter_code)

    @staticmethod
    def get_quirprobable_code_prob(codes: list):
        quiprobable_code_prob_list = []
        for code in codes:
            quiprobable_code_prob_list.append((code, 1 / len(codes)))
        return dict(quiprobable_code_prob_list)

    @staticmethod
    def get_cyrillic_code_prob(path_to_file: str, letter_code: dict):
        f = open(path_to_file, encoding='utf-8-sig')
        cyrillic_distribution_list = []
        for line in f:
            cyrillic_distribution_list.append(line.split())
            p = float(cyrillic_distribution_list[-1][-1]) / 100 * 65 / 87
            cyrillic_distribution_list[-1][-1] = p
        f.close()
        for letter in letter_code.keys():
            if not contains(cyrillic_distribution_list, letter):
                cyrillic_distribution_list.append((letter, 1 / 87))
        updated = [(letter_code.get(pair[0]), pair[1]) for pair in cyrillic_distribution_list]
        return dict(updated)


def contains(l: list, x):
    for el in l:
        if el[0] == x:
            return True
    return False
