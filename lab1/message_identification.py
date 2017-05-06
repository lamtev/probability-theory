from operator import itemgetter
from queue import Queue

import matplotlib.pyplot as plt

from alphabet import Alphabet
from letters_distribution import LettersDistribution
from probability import p_posterior

f = open('data/messages.txt', encoding='utf-8-sig')

messages = []
for line in f:
    messages.append(line.split())
f.close()

alphabet = Alphabet('data/alphabet.txt')
alphas = alphabet.code_letter.keys()
distribution = LettersDistribution(alphabet, 'data/cyrillic_distribution.txt')
code_prob = distribution.quiprobable_code_prob
# code_prob = distribution.cyrillic_code_prob
code_probs = Queue(208)
for i in range(208):
    code_probs.put(code_prob)
real_messages = []
posterior_distributions = []
for message in messages:
    real_message = []
    posterior_distributions.append([])
    for letter in message:
        local_posterior_distribution = []
        code_prob = code_probs.get()
        for alpha in alphas:
            local_posterior_distribution.append((alpha, p_posterior(alpha, letter, code_prob, 0.135)))
        posterior_distributions[-1].append(
            [(local_posterior_distribution.index(pair) + 1, pair[1]) for pair in local_posterior_distribution]
        )
        real_message.append(alphabet.code_letter.get(max(local_posterior_distribution, key=itemgetter(1))[0]))
        code_probs.put(dict(local_posterior_distribution))

    real_messages.append(real_message)
for real_message in real_messages:
    real_message = ''.join(real_message)
    print(real_message)

letterNumber = 0
for i in range(len(posterior_distributions)):
    axes = plt.figure(figsize=(13, 8)).gca()

    axes.plot([pair[0] for pair in posterior_distributions[i][letterNumber]],
              [pair[1] for pair in posterior_distributions[i][letterNumber]], linewidth=1.5)

    axes.set_xlabel('$N$', fontsize=20, labelpad=20)
    axes.set_ylabel('$P$', fontsize=20, labelpad=20)
    axes.tick_params(labelsize=15, pad=10)
    axes.set_xlim([1, 87])
    plt.title('Апостериорное распределение вероятностей для {s}-й буквы ({a}) после {n}-й посылки'
              .format(a=real_messages[-1][letterNumber], n=i + 1, s=letterNumber + 1), fontsize=20)
    plt.tight_layout()
    plt.show()
