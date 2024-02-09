import random
import matplotlib.pyplot as plt


def monte_carlo_simulation(num_trials):
    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_trials):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total_sum = dice1 + dice2
        sum_counts[total_sum] += 1

    probabilities = {sum_val: count / num_trials * 100 for sum_val, count in sum_counts.items()}
    return probabilities


def print_results(probabilities):
    print("Сума\tІмовірність")
    for sum_val, probability in probabilities.items():
        print(f"{sum_val}\t{probability:.2f}%")


def plot_results(probabilities):
    sums, probs = zip(*sorted(probabilities.items()))
    plt.bar(sums, probs, color='blue')
    plt.xlabel('Сума')
    plt.ylabel('Імовірність, %')
    plt.title('Імовірності сум при киданні двох кубиків (Метод Монте-Карло)')
    plt.show()


if __name__ == '__main__':
    # Проводимо симуляцію для великої кількості кидків (наприклад, 100000 разів)
    num_trials = 100000
    probabilities = monte_carlo_simulation(num_trials)

    # Виводимо результати
    print_results(probabilities)

    # Графік
    plot_results(probabilities)
