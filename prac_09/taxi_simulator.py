from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    fare = 0
    taxi_choice = ""
    print("Let's drive!")
    show_menu()
    choice = input(">>> ")
    while choice != "q":

        if choice == "c":
            show_taxi()
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    print(f"You have chosen {taxis[taxi_choice].name}")
                else:
                    print("Invalid choice")
            except ValueError:
                print("Input must be a number")

        elif choice == "d":
            if taxi_choice == "":
                print("Pick a vehicle first!")
            else:
                distance = int(input("Enter the distance: "))
                taxis[taxi_choice].drive(distance)
                fare += taxis[taxi_choice].get_fare()
                print(f"Your {taxis[taxi_choice].name} trip costs you ${taxis[taxi_choice].get_fare():.2f}")


        else:
            print("Invalid choice. Please choose from the menu.")
        print(f"Bill to date: ${fare:.2f}")
        show_menu()
        choice = input("Enter your choice: ").lower()
    print("Taxis are now:")
    show_taxi()


def show_menu():
    print("q)uit, c)hoose taxi, d)rive")


def show_taxi():
    for i, taxi in enumerate(taxis):
        print(i, f"-", taxi)


main()
