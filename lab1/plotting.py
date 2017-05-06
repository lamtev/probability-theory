import matplotlib.pyplot as plt


def plot_posterior_prob_distr(posterior_distributions: list, decoded_messages: list, letter_number: int):
    for i in range(len(posterior_distributions)):
        axes = plt.figure(figsize=(13, 8)).gca()

        axes.plot([pair[0] for pair in posterior_distributions[i][letter_number]],
                  [pair[1] for pair in posterior_distributions[i][letter_number]], linewidth=1.5)

        axes.set_xlabel('$N$', fontsize=20, labelpad=20)
        axes.set_ylabel('$P$', fontsize=20, labelpad=20)
        axes.tick_params(labelsize=15, pad=10)
        axes.set_xlim([1, 87])
        plt.title('Апостериорное распределение вероятностей для {s}-й буквы ({a}) после {n}-й посылки'
                  .format(a=decoded_messages[-1][letter_number], n=i + 1, s=letter_number + 1), fontsize=20)
        plt.tight_layout()
        plt.show()


def plot_entropy(points: list, entropy: list):
    axes = plt.figure(figsize=(13, 8)).gca()

    axes.plot(points, entropy, linewidth=1.5)

    axes.set_xlabel('$N$', fontsize=20, labelpad=20)
    axes.set_ylabel('$H$', fontsize=20, labelpad=20)
    axes.tick_params(labelsize=15, pad=10)
    axes.set_xlim([1, 18])
    plt.title('Изменение условной энтропии', fontsize=20)
    plt.tight_layout()
    plt.show()


def plot_information(points: list, information: list):
    axes = plt.figure(figsize=(13, 8)).gca()

    axes.plot(points, information, linewidth=1.5)

    axes.set_xlabel('$N$', fontsize=20, labelpad=20)
    axes.set_ylabel('$I$', fontsize=20, labelpad=20)
    axes.tick_params(labelsize=15, pad=10)
    axes.set_xlim([1, 18])
    plt.title('Изменение количества информации', fontsize=20)
    plt.tight_layout()
    plt.show()
