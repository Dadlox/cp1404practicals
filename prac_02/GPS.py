"""
Week 2 - GPS (Gopher Population Simulator)
"""
import random


def adding_gopher(input):
    new_addition = input * random.uniform(0.1,0.15)
    return new_addition

def removing_gopher(input):
    removal = input * random.uniform(0.05, 0.25)
    return removal

def main():
    print("Welcome to Gopher Population Simulator!")
    population = 1000
    print(f"Starting population: {population}")

    for i in range(1,10):
        print("")
        print(f"Year {i}")
        new_birth = round(adding_gopher(population))
        death = round(removing_gopher(population))
        print(f"{new_birth} Gophers are born. {death} died.")
        population = population + new_birth - death
        print(f"Population: {population}")



main()