"""
CP1404/CP5632 - Practical
Week 2 - Add function to this code
"""

def check_score(input):
    if input < 0 or input > 100:
        return("Invalid score")
    else:
        if input >= 90:
            return("Excellent")
        elif input >= 50:
            return("Pass")
        else:
            return("Bad")

def main():
    score = float(input("Enter score: "))
    print(check_score(score))



main()