
class Action:

    def __init__(self, action):
        self.name = action[0]
        self.cost = float(action[1])
        self.profit = round(self.cost * float(action[2].replace("%", "")) / 100, 2)

    def __str__(self) -> str:
        return f"{self.name} - {self.cost}€"

    def __repr__(self) -> str:
        return f"{self.name}"

    def __lt__(self, other):
        return self.profit < other.profit
