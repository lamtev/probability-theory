from alphabet import Alphabet
from text_producing import make_messages_text
from decoding import decode, independent_prob_distribution
from information_theory import entropy, k_th_letter_distribution, information
from letters_distribution import LettersDistribution
from plotting import plot_posterior_prob_distr, plot_entropy, plot_information

f = open('data/messages.txt', encoding='utf-8-sig')
messages = []
for line in f:
    messages.append(line.split())
f.close()

q = 0.135
s = 0
messages_number = len(messages)

alphabet = Alphabet('data/alphabet.txt')
distribution = LettersDistribution(alphabet, 'data/cyrillic_distribution.txt')

print('Все символы равновероятны')

decoded_messages1, posterior_distributions1 = \
    decode(messages, alphabet.code_letter, distribution.quiprobable_code_prob, q)
for message in decoded_messages1:
    print(message)
plot_posterior_prob_distr(posterior_distributions1, decoded_messages1, s)

ind_post_prob_distr1 = \
    independent_prob_distribution(messages, alphabet.code_letter, distribution.quiprobable_code_prob, q)

points = [i + 1 for i in range(messages_number)]

entropy1 = entropy(k_th_letter_distribution(ind_post_prob_distr1, s))
plot_entropy(points, entropy1)

info1 = information(k_th_letter_distribution(ind_post_prob_distr1, s), distribution.quiprobable_code_prob)
plot_information(points, info1)

print()
print('Вероятности согласно частоте букв в русском алфавите')
decoded_messages2, posterior_distributions2 = \
    decode(messages, alphabet.code_letter, distribution.cyrillic_code_prob, q)
for message in decoded_messages2:
    print(message)
plot_posterior_prob_distr(posterior_distributions2, decoded_messages2, s)

ind_post_prob_distr2 = \
    independent_prob_distribution(messages, alphabet.code_letter, distribution.cyrillic_code_prob, q)

entropy2 = entropy(k_th_letter_distribution(ind_post_prob_distr2, s))
plot_entropy(points, entropy2)

info2 = information(k_th_letter_distribution(ind_post_prob_distr2, s), distribution.cyrillic_code_prob)
plot_information(points, info2)
