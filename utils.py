import csv
import time

from actions_class import Action


def execution_time(funct):
    """
    Calculate the execution time of a function and print it
    :param funct: Function to be analyzed
    """

    def wrapper(*args, **kwargs):
        start_time = time.time()
        funct(*args, **kwargs)
        end_time = time.time()
        print(f"EXECUTION: {(end_time - start_time):.3f}s\n")

        return funct(*args, **kwargs)

    return wrapper


def extract_csv(path: str, is_decimal_prices: bool = False):
    """
    Extract data from a csv file
    :param path: file path
    :param is_decimal_prices: indication if the prices are decimal
    :return: stock list
    """
    if not is_decimal_prices:
        with open(path, 'r') as f:
            stocks_file = csv.reader(f)
            all_stocks = []

            for stock in stocks_file:
                if stock != ['name', 'price', 'profit']:
                    name = stock[0]
                    cost = float(stock[1])
                    profit = round(float(stock[2].replace("%", "")), 2)
                    if cost > 0:
                        all_stocks.append(Action([name, str(cost), str(profit)]))
            return all_stocks

    else:
        with open(path, 'r') as f:
            stocks_file = csv.reader(f)
            all_stocks = []

            for stock in stocks_file:
                if stock != ['name', 'price', 'profit']:
                    name = stock[0]
                    cost = float(stock[1]) * 100
                    profit = round(float(stock[2].replace("%", "")), 2)
                    if cost > 0:
                        all_stocks.append(Action([name, str(cost), str(profit)]))
            return all_stocks
