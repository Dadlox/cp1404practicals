from datetime import datetime


class Project:
    def __init__(self, name="", start_date="", priority=0, cost=0, completion=0):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y")
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def __str__(self):
        start_date_str = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name:<20} start_date:{start_date_str:<15} "
                f"priority:{self.priority:<15} cost:${self.cost:<15.2f} completion:{self.completion:}%")


def compare_date(self, other):
        return self.start_date < other.start_time
