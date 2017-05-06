from operator import itemgetter
from queue import Queue

from alphabet import Alphabet
from probability import p_posterior


def decode(sent_messages: list, alphabet: Alphabet, code_prob: dict, q: float) -> (list, list):
    message_length = len(sent_messages[0])
    code_probs = Queue(message_length)
    for i in range(message_length):
        code_probs.put(code_prob)
    alphas = alphabet.code_letter.keys()
    real_messages = []
    posterior_distributions = []
    for message in sent_messages:
        real_message = []
        posterior_distributions.append([])
        for letter in message:
            local_posterior_distribution = []
            code_prob = code_probs.get()
            for alpha in alphas:
                local_posterior_distribution.append((alpha, p_posterior(alpha, letter, code_prob, q)))
            posterior_distributions[-1].append(
                [(local_posterior_distribution.index(pair) + 1, pair[1]) for pair in local_posterior_distribution]
            )
            real_message.append(alphabet.code_letter.get(max(local_posterior_distribution, key=itemgetter(1))[0]))
            code_probs.put(dict(local_posterior_distribution))
        real_messages.append(real_message)
    decoded_messages = []
    for real_message in real_messages:
        decoded_messages.append(''.join(real_message))

    return decoded_messages, posterior_distributions


def independent_prob_distribution(sent_messages: list, alphabet: Alphabet, code_prob: dict, q: float) -> list:
    alphas = alphabet.code_letter.keys()
    posterior_distributions = []
    for message in sent_messages:
        posterior_distributions.append([])
        for letter in message:
            local_posterior_distribution = []
            for alpha in alphas:
                local_posterior_distribution.append((alpha, p_posterior(alpha, letter, code_prob, q)))
            posterior_distributions[-1].append(
                [(local_posterior_distribution.index(pair) + 1, pair[1]) for pair in local_posterior_distribution]
            )
    return posterior_distributions
