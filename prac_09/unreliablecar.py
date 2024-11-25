import random

from Codes.Practical.Week9.Assessment.car import Car


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability=0):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if random.randint(1, 100) < self.reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven
