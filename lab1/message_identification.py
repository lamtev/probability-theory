from operator import itemgetter
from queue import Queue

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
# code_prob = distribution.quiprobable_code_prob
code_prob = distribution.cyrillic_code_prob
code_probs = Queue(208)
for i in range(208):
    code_probs.put(code_prob)
real_messages = []
for message in messages:
    real_message = []
    for letter in message:
        local_distribution = []
        code_prob = code_probs.get()
        for alpha in alphas:
            local_distribution.append((alpha, p_posterior(alpha, letter, code_prob, 0.135)))
        real_message.append(alphabet.code_letter.get(max(local_distribution, key=itemgetter(1))[0]))
        code_probs.put(dict(local_distribution))
    real_messages.append(real_message)
for real_message in real_messages:
    print(real_message)
