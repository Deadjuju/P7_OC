from itertools import combinations
from typing import List

from stocks_class import Stock
from utils import execution_time


@execution_time
def brute_force(budget: int, stocks: list) -> List[Stock]:
    """
     Brute force algorithm - calculation of the optimal combination
    :param budget: Client's maximum budget for the purchase of stocks
    :param stocks: list of stocks available
    :return: the most profitable combination
    """
    max_profit = 0
    best_combination = None
    n = 1
    while n <= len(stocks):
        for comb in combinations(stocks, n):
            money_spent = sum([stock.cost for stock in comb])
            total_profit = sum([stock.profit for stock in comb])
            if total_profit > max_profit and money_spent <= budget:
                max_profit = total_profit
                best_combination = comb
        n += 1
    return best_combination


if __name__ == '__main__':
    from utils import extract_csv

    file = '../data_csv/first_list.csv'
    BUDGET = 500

    all_stocks = extract_csv(path=file)
    best_comb = brute_force(budget=BUDGET, stocks=all_stocks)

    print("-------------- Best Choice: --------------")
    print(best_comb)
    print(f"Argent dépensé: {sum([price.cost for price in best_comb])}€.")
    print(f"Profit: {(sum([profit.profit for profit in best_comb])):.2f}€.")
