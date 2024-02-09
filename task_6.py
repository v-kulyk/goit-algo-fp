def greedy_algorithm(items:dict, budget:int):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    selected_items = []
    remaining_budget = budget

    for item, details in sorted_items:
        if details['cost'] <= remaining_budget:
            selected_items.append((item, details))
            remaining_budget -= details['cost']

    return selected_items


def dynamic_programming(items:dict, budget:int):
    items_list = [item for item in items.items()]
    n = len(items_list)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(budget + 1):
            cost = items_list[i - 1][1]['cost']
            calories = items_list[i - 1][1]['calories']

            if cost > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)

    selected_items = []
    i, j = n, budget
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(items_list[i - 1])
            j -= items_list[i - 1][1]['cost']
        i -= 1

    return selected_items[::-1]


if __name__ == '__main__':
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    budget = 70

    greedy_result = greedy_algorithm(items, budget)
    print("Greedy Algorithm Result:", greedy_result)

    dynamic_result = dynamic_programming(items, budget)
    print("Dynamic Programming Result:", dynamic_result)
