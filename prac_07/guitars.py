"""
Code: guitars.py
Coder: Hein Htet
Start: 11:34
End: 1:30
"""
from Codes.Practical.Week7.Prac7.guitar import Guitar
import csv


def main():
    guitars = add_csv()  # Load guitars from the CSV file
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(Vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")
    guitars.sort()

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(Vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


def add_csv():
    guitars = []
    with open('guitars.csv', 'r') as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars

#Completed the first part of guitars exercise

main()
