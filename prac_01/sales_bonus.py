"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

"""
get sales
while sales >= 0
    calculate bonus (this line is intentionally incomplete pseudocode)
    print bonus
    get sales
do next thing
"""

sales = float(input("Enter sales: $"))
while sales >= 0:
    if sales < 1000:
        bonus = 0.10
    else:
        bonus = 0.15
    sales_bonus = sales * bonus
    print (f"Sales: {sales}       Bonus: {sales_bonus}")
    sales = float(input("Enter sales: $"))