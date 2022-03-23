import csv
import time

from actions_class import Action


def execution_time(funct):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        funct(*args, **kwargs)
        end_time = time.time()
        print(f"EXECUTION: {(end_time - start_time):.3f}s\n")

        return funct(*args, **kwargs)

    return wrapper


def extract_csv(path, is_decimal_prices=False):
    if not is_decimal_prices:
        with open(path, 'r') as f:
            actions_file = csv.reader(f)
            return [Action(action) for action in actions_file if action != ['name', 'price', 'profit']]

    else:
        with open(path, 'r') as f:
            actions_file = csv.reader(f)
            all_actions = []

            for action in actions_file:
                if action != ['name', 'price', 'profit']:
                    name = action[0]
                    cost = float(action[1])*100
                    profit = round(float(action[2][:-1]) / 100, 2)*100
                    if cost > 0:
                        all_actions.append(Action([name, str(cost), str(profit)]))
            return all_actions
