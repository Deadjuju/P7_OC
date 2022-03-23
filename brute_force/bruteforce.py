from itertools import combinations

from utils import execution_time


@execution_time
def bruteforce(actions):
    max_profit = 0
    best_combination = None
    n = 1
    while n <= len(actions):
        for comb in combinations(actions, n):
            money_spent = sum([action_price.cost for action_price in comb])
            total_profit = sum([profit.profit for profit in comb])
            if total_profit > max_profit and money_spent <= BUDGET:
                max_profit = total_profit
                best_combination = comb
        n += 1
    return best_combination


if __name__ == '__main__':
    from utils import extract_csv

    file = '../data_csv/first_list.csv'

    BUDGET = 500

    all_actions = extract_csv(path=file)

    best_comb = bruteforce(actions=all_actions)

    print("-------------- Best Choice: --------------")
    print(best_comb)
    print(f"Argent dépensé: {sum([action_price.cost for action_price in best_comb])}€.")
    print(f"Profit: {(sum([profit.profit for profit in best_comb])):.2f}€.")
