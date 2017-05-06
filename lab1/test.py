from queue import Queue

from alphabet import Alphabet
from letters_distribution import LettersDistribution
from probability import p_of_receiving_y, p_posterior

alphabet = Alphabet('data/alphabet.txt')
letters_distribution = LettersDistribution(alphabet, 'data/cyrillic_distribution.txt')
#
# code_prob = dict([('0000', 0.25), ('0011', 0.25), ('1100', 0.25), ('1110', 0.25)])

# print(p_of_receiving_y('0100', code_prob, 0.1))
#
#
# print(p_posterior('0000', '0100', code_prob, 0.1, 0.0387))
# print(p_posterior('0000', '0100', code_prob, 0.1))
x = Queue()
x.put('j')
x.put('a')
x.put('v')
x.put('a')
# print(x.get(), x.get(), x.get(), x.get())

print(sum(letters_distribution.cyrillic_code_prob.values()))
