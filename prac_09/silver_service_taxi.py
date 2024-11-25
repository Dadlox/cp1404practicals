from Codes.Practical.Week9.Assessment.car import Car
from Codes.Practical.Week9.Assessment.taxi import Taxi


class SilverServiceTaxi(Taxi):
    FLAGFALL = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = super().price_per_km * fanciness

    def __str__(self):
        return f"{super().__str__()} plus flagfall of ${self.FLAGFALL:.2f}"

    def get_fare(self):
        return super().get_fare() + self.FLAGFALL
