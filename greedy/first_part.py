import csv
import time

from utils import execution_time


BUDGET = 500

with open('../csv/first_list.csv', 'r') as f:
    actions_file = csv.reader(f)
    all_actions = []

    for action in actions_file:
        name = action[0]
        cost = int(action[1])
        profit = round(cost * (1 + int(action[2][:-1])/100), 2)

        # Action format: (Name, Price, Profit after 2 years)
        all_actions.append((name, cost, profit))
# print(*all_actions, sep="\n")


@execution_time
def greedy(budget, actions):
    sorted_actions = sorted(actions, key=lambda x: x[2])
    selected_actions = []
    money_spent = 0

    while sorted_actions:
        current_action = sorted_actions.pop()
        if current_action[1] + money_spent <= budget:
            selected_actions.append(current_action)
            money_spent += current_action[1]

    return [action[0] for action in selected_actions], money_spent, sum([action[2] for action in selected_actions])


best_selected_actions = greedy(BUDGET, all_actions)

print(f"Actions sélectionnées: {best_selected_actions[0]}")
print(f"Argent dépensé: {best_selected_actions[1]}€.")
print(f"Profit: {best_selected_actions[2]}€.")

