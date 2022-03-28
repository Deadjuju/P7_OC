from utils import execution_time


def get_matrix_prices(budget, actions: list):
    # Create matrix
    matrix = []
    for _ in range(len(actions) + 1):
        line = [0 for _ in range(budget + 1)]
        matrix.append(line)

    # Search optimised solution for which case
    for i_action, action in enumerate(actions, start=1):
        for budget_step in range(1, budget + 1):
            if action.cost <= budget_step:
                matrix[i_action][budget_step] = max(
                    action.profit + matrix[i_action - 1][budget_step - int(action.cost)],
                    matrix[i_action - 1][budget_step])
            else:
                matrix[i_action][budget_step] = matrix[i_action - 1][budget_step]
    return matrix


@execution_time
def get_actions_list(budget, actions_list: list):
    matrix = get_matrix_prices(budget, actions_list)

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
    BUDGET = 500

    if is_decimal_prices:
        budg = BUDGET * 100 - 1
        all_actions = extract_csv(path=file2, is_decimal_prices=is_decimal_prices)
    else:
        budg = BUDGET
        all_actions = extract_csv(path=file)

    selected_actions = get_actions_list(budg, all_actions)

    # prices = prices_matrix[-1][-1]
    total_cost = sum([action.cost for action in selected_actions])
    total_return = sum([action.profit for action in selected_actions])

    if is_decimal_prices:

        print(selected_actions)
        print(f"Actions sélectionnées: {selected_actions}")
        print(f"Argent dépensé: {total_cost / 100 :.2f}€.")
        print(f"Profit: {total_return / (100) :.2f}€.")

    else:
        print(selected_actions)
        print(f"Actions sélectionnées: {selected_actions}")
        print(f"Argent dépensé: {total_cost}€.")
        print(f"Profit: {total_return}€.")
