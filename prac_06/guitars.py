"""
Code: guitars.py
Coder: Hein Htet
Start: 11:34
End:
"""
from Codes.Practical.Week6.prac_06.guitar import Guitar


def main():
    guitars = [Guitar(" Gibson L-5 CES", 1922, 16035.40), Guitar("Line 6 JTV-59", 2010, 1512.90)]
    print("My Guitars!")
    while True:
        name = input("Name: ")
        if name == "":
            break

        year = int(input("Year: "))
        cost = float(input("Cost: "))
        if cost == "" or cost < 0:
            print("Cost can't be blank or be less than 0!")
            cost = float(input("Cost: "))

        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}): ${cost:.2f} is added")

    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(Vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")


main()
