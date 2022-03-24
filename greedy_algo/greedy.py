from typing import Tuple, List

from actions_class import Action
from utils import execution_time


@execution_time
def get_greedy(budget: int, actions) -> List[Action]:
    """
    Greedy algorithm to quickly calculate an estimate of the most profitable stocks
    :param budget: budget limit not to be exceeded
    :param actions: list of all actions
    :return: (selected_actions, total actions price, total gain after 2 years)
    """
    sorted_actions = sorted(actions, key=lambda x: x.profit)
    selected_actions = []
    money_spent = 0

    while sorted_actions:
        current_action = sorted_actions.pop()
        if current_action.cost + money_spent <= budget:
            selected_actions.append(current_action)
            money_spent += current_action.cost

    return selected_actions


if __name__ == '__main__':
    from utils import extract_csv

    file = '../data_csv/first_list.csv'
    file2 = '../data_csv/dataset1_Python+P7.csv'
    file3 = '../data_csv/dataset2_Python+P7.csv'

    BUDGET = 500

    all_actions = extract_csv(path=file3)

    best_selected_actions = get_greedy(BUDGET, all_actions)

    print(f"Actions sélectionnées: {best_selected_actions}")
    print(f"Argent dépensé: {sum([action.cost for action in best_selected_actions]):.2f}€.")
    print(f"Profit: {sum([action.profit for action in best_selected_actions]):.2f}€.")
