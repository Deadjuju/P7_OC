import csv
from typing import Tuple, List

from actions_class import Action
from utils import execution_time

BUDGET = 500

with open('../data_csv/first_list.csv', 'r') as f:
    actions_file = csv.reader(f)
    all_actions = [Action(action) for action in actions_file]


@execution_time
def greedy(budget: int, actions) -> Tuple[List[Action], float, float]:
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

    return ([action.name for action in selected_actions],
            money_spent,
            sum([action.profit for action in selected_actions]))


best_selected_actions = greedy(BUDGET, all_actions)

print(f"Actions sélectionnées: {best_selected_actions[0]}")
print(f"Argent dépensé: {best_selected_actions[1]:.2f}€.")
print(f"Profit: {best_selected_actions[2]:.2f}€.")
