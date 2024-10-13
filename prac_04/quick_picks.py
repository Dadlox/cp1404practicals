import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def generate_quick_pick(number_picks):
    quick_picks = []

    for number in range(number_picks):
        picked_number = []

        while len(picked_number) < NUMBERS_PER_PICK:
            num = random.randint(MIN_NUMBER, MAX_NUMBER)
            if num not in picked_number:  # Check for duplicates
                picked_number.append(num)

        # Sort the numbers in ascending order
        picked_number.sort()
        quick_picks.append(picked_number)

    return quick_picks


def main():
    while True: #Found this code while searching up how to make codes denser and more understandable.
        try:
            num_picks = int(input("How many quick picks would you like to generate? "))
            if num_picks < 1:
                print("Number can't be negative.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    quick_picks = generate_quick_pick(num_picks)

    # Display the quick picks
    print("Here are your quick picks:")
    for i, pick in enumerate(quick_picks, start=1):
        formatted_pick = ' '.join(f"{num:2}" for num in pick)
        print(f"Pick {i}: {formatted_pick}")


main()
