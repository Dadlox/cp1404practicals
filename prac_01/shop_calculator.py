"""
Shop Calculator

Notes:
User input how many items they're buying
get that number of price, then add them all into total price
If total price > 100, give 10% discount
Display must be in money format (e.g. $5.00)
"""

"""
DISCOUNT = 0.90
get number_of_items
while number_of_items < 0
    get number_of_items
while i < number_of_items:
    get price
    total += price
    i++
if total >= 100:
    total = total * DISCOUNT
print total
"""

DISCOUNT = 0.90
total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    number_of_items = input(int("Invalid: number of items can't be 0. try again: "))
for i in range(0,number_of_items):
    price = float(input("Input price:"))
    total += price
if total >= 100:
    print(f"Total: ${total * DISCOUNT:.2f}. 10% discount applies.")
else:
    print(f"Total: ${total:.2f}. No discount applies.")