
class Stock:

    def __init__(self, stock):
        self.name = stock[0]
        self.cost = float(stock[1])
        self.profit = round(self.cost * float(stock[2].replace("%", "")) / 100, 2)

    def __str__(self) -> str:
        return f"{self.name}€"

    def __repr__(self) -> str:
        return f"{self.name}"

    def __lt__(self, other):
        return self.profit < other.profit
