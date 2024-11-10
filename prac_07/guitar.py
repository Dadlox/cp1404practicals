class Guitar:
    def __init__(self, name="", year=2024, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}): ${self.cost:.2f}"

    def get_age(self):
        CURRENT_YEAR = 2024
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        if self.get_age() > 49:
            return True
        else:
            return False

    def __lt__(self, other):
        return self.year < other.year
