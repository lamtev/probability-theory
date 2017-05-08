from alphabet import Alphabet
from letters_distribution import LettersDistribution

alphabet = Alphabet('data/alphabet.txt')

print(alphabet.code_letter_duplicate)

distr = LettersDistribution(alphabet, 'data/cyrillic_distribution.txt')

print(sum(distr.quiprobable_code_prob_dupl.values()))
print(sum(distr.cyrillic_code_prob_dupl.values()))

print(sum(distr.quiprobable_code_prob.values()))
print(sum(distr.cyrillic_code_prob.values()))
