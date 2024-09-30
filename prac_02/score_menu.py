"""
Week 2 - score_menu.py
"""

"""
function Get_valid_score()
    get score
    while score < 0 or score > 100:
        print invalid
        get new score
    return score
    
function Show_stars(score)
    for i in range of score:
        print("*"end =" ")
function main()
    score = 0
    print menu
        while choice != q:
            if choice = g:
                score = Get_valid_score()
            elif choice = P:
                print score
            elif choice = S:
                show_star(score)
    print("Farewell")
"""

def get_valid_score():
    score = int(input("Enter a score: "))
    while score < 0 or score > 100:
        score = int(input("Invalid score, enter a new score: "))
    return score

def show_stars(score):
    for i in range(score):
        print("*", end="")
def main():
    score = get_valid_score()
    menu = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(" >>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(score)
        elif choice == "S":
            show_stars(score)
            print("")
        print(menu)
        choice = input(" >>> ").upper()
    print("Farewell")




main()