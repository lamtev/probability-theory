from alphabet import Alphabet
from decoding import decode, independent_prob_distribution
from information_theory import entropy, k_th_letter_distribution, information
from letters_distribution import LettersDistribution
from plotting import plot_posterior_prob_distr

f = open('data/messages.txt', encoding='utf-8-sig')
messages = []
for line in f:
    messages.append(line.split())
f.close()

for i in range(1, len(messages)):
    for j in range(len(messages[i])):
        messages[0][j] += messages[i][j]
x = messages[0]
messages = [x]

q = 0.135
s = 0

alphabet = Alphabet('data/alphabet.txt')
distribution = LettersDistribution(alphabet, 'data/cyrillic_distribution.txt')

print('Все символы равновероятны')

decoded_messages1, posterior_distributions1 = \
    decode(messages, alphabet.code_letter_duplicate, distribution.quiprobable_code_prob_dupl, q)
print(decoded_messages1[-1])

plot_posterior_prob_distr(posterior_distributions1, decoded_messages1, s)

ind_post_prob_distr1 = \
    independent_prob_distribution(messages, alphabet.code_letter_duplicate, distribution.quiprobable_code_prob_dupl, q)

entropy1 = entropy(k_th_letter_distribution(ind_post_prob_distr1, s))[0]
print('Условная энтропия: ', entropy1)

info1 = information(k_th_letter_distribution(ind_post_prob_distr1, s), distribution.quiprobable_code_prob_dupl)[0]
print('Среднее количество информации: ', info1)


print()
print('Вероятности согласно частоте букв в русском алфавите')
decoded_messages2, posterior_distributions2 = \
    decode(messages, alphabet.code_letter_duplicate, distribution.cyrillic_code_prob_dupl, q)

print(decoded_messages2[-1])
plot_posterior_prob_distr(posterior_distributions2, decoded_messages2, s)

ind_post_prob_distr2 = \
    independent_prob_distribution(messages, alphabet.code_letter_duplicate, distribution.cyrillic_code_prob_dupl, q)

entropy2 = entropy(k_th_letter_distribution(ind_post_prob_distr2, s))[0]
print('Условная энтропия: ', entropy2)

info2 = information(k_th_letter_distribution(ind_post_prob_distr2, s), distribution.cyrillic_code_prob_dupl)[0]
print('Среднее количество информации: ', info2)
