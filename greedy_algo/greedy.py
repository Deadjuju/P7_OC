from typing import List

from stocks_class import Stock
from utils import execution_time


@execution_time
def get_greedy(budget: int, stocks: List[Stock]) -> List[Stock]:
    """
    Greedy algorithm to quickly calculate an estimate of the most profitable stocks
    :param budget: budget limit not to be exceeded
    :param stocks: list of all actions
    :return: list of stocks with the most profitable combination
    """
    sorted_stocks = sorted(stocks)
    selected_stocks = []
    money_spent = 0

    while sorted_stocks:
        current_stock = sorted_stocks.pop()
        if current_stock.cost + money_spent <= budget:
            selected_stocks.append(current_stock)
            money_spent += current_stock.cost
    return selected_stocks


if __name__ == '__main__':
    from utils import extract_csv

    file = '../data_csv/first_list.csv'
    file2 = '../data_csv/dataset1_Python+P7.csv'
    file3 = '../data_csv/dataset2_Python+P7.csv'

    BUDGET = 500

    all_stocks = extract_csv(path=file3)
    best_selected_stocks = get_greedy(BUDGET, all_stocks)

    print(f"Actions sélectionnées: {best_selected_stocks}")
    print(f"Argent dépensé: {sum([stock.cost for stock in best_selected_stocks]):.2f}€.")
    print(f"Profit: {sum([stock.profit for stock in best_selected_stocks]):.2f}€.")
