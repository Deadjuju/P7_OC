from utils import execution_time


@execution_time
def get_matrix_prices(budget, actions: list):
    # Create matrix
    matrix = []
    for _ in range(len(actions) + 1):
        line = [0 for _ in range(budget + 1)]
        matrix.append(line)

    for i in range(1, len(actions) + 1):
        for w in range(1, budget + 1):
            if actions[i - 1].cost <= w:
                matrix[i][w] = max(actions[i - 1].profit + matrix[i - 1][w - int(actions[i - 1].cost)],
                                   matrix[i - 1][w])
            else:
                matrix[i][w] = matrix[i - 1][w]

    return matrix


@execution_time
def get_actions_list(budget, actions_list: list, matrix):
    n = len(actions_list)
    selection = []

    while budget >= 0 and n >= 0:
        action = actions_list[n - 1]
        if matrix[n][budget] == matrix[n - 1][budget - int(action.cost)] + action.profit:
            selection.append(action)
            # print(selected_actions)
            budget -= int(action.cost)
        n -= 1
    return selection


if __name__ == '__main__':
    from utils import extract_csv

    file = '../data_csv/first_list.csv'
    file2 = '../data_csv/dataset1_Python+P7.csv'
    file3 = '../data_csv/dataset2_Python+P7.csv'

    is_decimal_prices = True

    if is_decimal_prices:
        BUDGET = 499 * 100
        all_actions = extract_csv(path=file3, is_decimal_prices=is_decimal_prices)
    else:
        BUDGET = 500
        all_actions = extract_csv(path=file)

    prices_matrix = get_matrix_prices(BUDGET, all_actions)
    selected_actions = get_actions_list(BUDGET, all_actions, prices_matrix)

    prices = prices_matrix[-1][-1]
    total_cost = sum([action.cost for action in selected_actions])
    total_return = sum([action.profit for action in selected_actions])

    if is_decimal_prices:
        prices /= 100

        print(round(prices, 2))
        print(selected_actions)
        print(f"Actions sélectionnées: {selected_actions}")
        print(f"Argent dépensé: {total_cost / 100 :.2f}€.")
        print(f"Profit: {total_return / (100 * 100) :.2f}€.")

    else:
        print(round(prices, 2))
        print(selected_actions)
        print(f"Actions sélectionnées: {selected_actions}")
        print(f"Argent dépensé: {total_cost}€.")
        print(f"Profit: {total_return}€.")
