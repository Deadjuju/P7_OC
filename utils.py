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


def extract_csv(path):
    with open(path, 'r') as f:
        actions_file = csv.reader(f)
        return [Action(action) for action in actions_file if action != ['name', 'price', 'profit']]
