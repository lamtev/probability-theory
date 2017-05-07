from alphabet import Alphabet
from decoding import decode, independent_prob_distribution
from information_theory import entropy, k_th_letter_distribution, information
from letters_distribution import LettersDistribution
from plotting import plot_posterior_prob_distr, plot_entropy, plot_information

f = open('data/messages.txt', encoding='utf-8-sig')
messages = []
for line in f:
    messages.append(line.split())
f.close()

for i in range(1, len(messages)):
    for j in range(len(messages[i])):
        messages[0][j] += messages[i][j]
messages = messages[0]

print(messages)
print(len(messages[0]))

# q = 0.135
# s = 0
# messages_number = len(messages)
#
# alphabet = Alphabet('data/alphabet.txt')
# distribution = LettersDistribution(alphabet, 'data/cyrillic_distribution.txt')
#
# decoded_messages1, posterior_distributions1 = decode(messages, alphabet, distribution.quiprobable_code_prob, q)
# print(decoded_messages1[-1])
#
# plot_posterior_prob_distr(posterior_distributions1, decoded_messages1, s)
#
# decoded_messages2, posterior_distributions2 = decode(messages, alphabet, distribution.cyrillic_code_prob, q)
# print(decoded_messages2[-1])
# plot_posterior_prob_distr(posterior_distributions2, decoded_messages2, s)
#
# ind_post_prob_distr1 = independent_prob_distribution(messages, alphabet, distribution.quiprobable_code_prob, q)
# ind_post_prob_distr2 = independent_prob_distribution(messages, alphabet, distribution.cyrillic_code_prob, q)
#
# entropy1 = entropy(k_th_letter_distribution(ind_post_prob_distr1, s))
# entropy2 = entropy(k_th_letter_distribution(ind_post_prob_distr2, s))
#
# info1 = information(k_th_letter_distribution(ind_post_prob_distr1, s), messages_number)
# info2 = information(k_th_letter_distribution(ind_post_prob_distr2, s), messages_number)
#
# points = [i + 1 for i in range(messages_number)]
#
# plot_entropy(points, entropy1)
# plot_entropy(points, entropy2)
#
# plot_information(points, info1)
# plot_information(points, info2)
