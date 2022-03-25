from bruteforce_algo.bruteforce import brute_force
from greedy_algo.greedy import get_greedy
from optimised.optimized import get_actions_list
from utils import extract_csv


CHOICES = [("0", 'data_csv/first_list.csv'),
           ("1", 'data_csv/dataset1_Python+P7.csv'),
           ("2", 'data_csv/dataset2_Python+P7.csv')]

BUDGET = 500


def choose_file():
    choices = [ch[0] for ch in CHOICES]
    while True:
        print("Please choose the dataset to analyze:", * CHOICES, sep="\n-> ")
        user_choice = input("Please enter the number equivalent to the dataset: |--> ")
        if user_choice not in choices:
            print("\nPlease type a correct number.")
        else:
            return CHOICES[int(user_choice)]


def choose_algorithm(user_choice):
    print("Please choose an algorithm: ")
    if user_choice[0] == "0":
        while True:
            choices = ['greedy', 'bruteforce', 'optimized']
            algo_choice = input("Type 'greedy', 'bruteforce' or 'optimized': ").lower()
            if algo_choice not in choices:
                print("Not in choices!")
            else:
                return algo_choice
    else:
        while True:
            choices = ['greedy', 'optimized']
            algo_choice = input("Type 'greedy' or 'optimized': ").lower()
            if algo_choice not in choices:
                print("Not in choices!")
            else:
                return algo_choice


def execute_algorithm(file_path, algorithm_choice):
    best_selected_stocks = []
    is_decimal_prices = False

    if algorithm_choice == "greedy":
        all_stocks = extract_csv(path=file_path[1])
        best_selected_stocks = get_greedy(BUDGET, all_stocks)

    elif algorithm_choice == "bruteforce":
        all_stocks = extract_csv(path=file_path[1])
        best_selected_stocks = brute_force(BUDGET, all_stocks)

    elif algorithm_choice == "optimized":
        if file_path[0] == "1" or file_path[0] == "2":
            is_decimal_prices = True
        if is_decimal_prices:
            budget = BUDGET * 100 - 1
            all_stocks = extract_csv(path=file_path[1], is_decimal_prices=is_decimal_prices)
        else:
            budget = BUDGET
            all_stocks = extract_csv(path=file_path[1])

        best_selected_stocks = get_actions_list(budget, all_stocks)

    money_pent = sum([action.cost for action in best_selected_stocks])
    profit = sum([action.profit for action in best_selected_stocks])

    text = f"********** {algorithm_choice.upper()} - {file_path[1]} ********** \n" \
           f" • Actions sélectionnées:\n   --->|| {best_selected_stocks}\n" \
           f" • Argent dépensé: {((money_pent / 100) if is_decimal_prices else money_pent):.2f}€.\n" \
           f" • Profit: {((profit / 100) if is_decimal_prices else profit):.2f}€."
    print(text)


if __name__ == '__main__':

    file = choose_file()
    algo = choose_algorithm(user_choice=file)
    print(file, algo)

    execute_algorithm(file_path=file, algorithm_choice=algo)
