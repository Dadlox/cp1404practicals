"""
CP1404/CP5632 Practical
Name: Hein Htet
Make a program to read, and display information from wimbledon.csv
Estimate: 30 minutes
Actual:43 minutes
"""
import csv
champion_wins = {}
champ_countries = set()

with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
    reader = csv.reader(in_file)
    next(reader)
    for row in reader:
        year, country_code, champion, country, runner_up, final_score = row
        if champion in champion_wins:
            champion_wins[champion] += 1
        else:
            champion_wins[champion] = 1
        champ_countries.add(country_code)

print("Wimbledon Champions: ")
for champion in champion_wins:
    print(f"{champion}: {champion_wins[champion]}")

print("")
print(f"There are {len(champ_countries)} have won Wimbledon: ")
print(" ".join(champ_countries))
