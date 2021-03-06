from typing import List

from stocks_class import Stock
from utils import execution_time


def get_matrix_prices(budget: int, stocks: List[Stock]) -> List[List[float]]:
    """
    Create a matrix with the optimal profit of each stock at each budget step
    :param budget: budget limit not to be exceeded
    :param stocks: list of all actions
    :return: matrix with optimal profit
    """

    # Create matrix
    matrix = []
    for _ in range(len(stocks) + 1):
        line = [0 for _ in range(budget + 1)]
        matrix.append(line)

    # Search optimised solution for which case
    for i_action, action in enumerate(stocks, start=1):
        for budget_step in range(1, budget + 1):
            if action.cost <= budget_step:
                matrix[i_action][budget_step] = max(
                    action.profit + matrix[i_action - 1][budget_step - int(action.cost)],
                    matrix[i_action - 1][budget_step])
            else:
                matrix[i_action][budget_step] = matrix[i_action - 1][budget_step]
    return matrix


@execution_time
def get_stocks_list(budget: int, stocks: List[Stock]) -> List[Stock]:
    """
    Optimized algorithm to quickly calculate the most profitable stocks
    :param budget: Client's maximum budget for the purchase of stocks
    :param stocks: list of stocks available
    :return: the most profitable combination
    """

    matrix = get_matrix_prices(budget=budget, stocks=stocks)

    selection = []
    for n, stock in reversed(list(enumerate(stocks))):
        if matrix[n+1][budget] == matrix[n][budget - int(stock.cost)] + stock.profit:
            selection.append(stock)
            budget -= int(stock.cost)
    return selection


if __name__ == '__main__':
    from utils import extract_csv

    file = '../data_csv/first_list.csv'
    file2 = '../data_csv/dataset1_Python+P7.csv'
    file3 = '../data_csv/dataset2_Python+P7.csv'

    is_decimal_prices = True
    BUDGET = 500

    if is_decimal_prices:
        budg = BUDGET * 100 - 1
        all_actions = extract_csv(path=file2, is_decimal_prices=is_decimal_prices)
    else:
        budg = BUDGET
        all_actions = extract_csv(path=file)

    selected_stocks = get_stocks_list(budg, all_actions)

    total_cost = sum([action.cost for action in selected_stocks])
    total_return = sum([action.profit for action in selected_stocks])

    if is_decimal_prices:
        print(selected_stocks)
        print(f"Actions s??lectionn??es: {selected_stocks}")
        print(f"Argent d??pens??: {total_cost / 100 :.2f}???.")
        print(f"Profit: {total_return / 100 :.2f}???.")

    else:
        print(selected_stocks)
        print(f"Actions s??lectionn??es: {selected_stocks}")
        print(f"Argent d??pens??: {total_cost}???.")
        print(f"Profit: {total_return}???.")
