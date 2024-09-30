import random


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
    no_of_scores = int(input("Enter the number of scores to generate: "))
    for i in range(no_of_scores):
        score = random.randint(0,100)
        print(f"{score} is {check_score(score)}")
        with open("result.txt", 'a') as f:
            print(f"{score} is {check_score(score)}", file=f)
main()