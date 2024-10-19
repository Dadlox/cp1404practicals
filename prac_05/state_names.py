"""
CP1404/CP5632 Practical
Name: Hein Htet
File needs reformatting
Complete prac 5 state names exercise
"""

""" Code in LBYL """
# TODO: Reformat this file so the dictionary code follows PEP 8 convention
# CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
#                 "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
# print(CODE_TO_NAME)
#
# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()
#
# code_width = int((max(len(code) for code in CODE_TO_NAME)))
# country_width = (max(len(CODE_TO_NAME[code]) for code in CODE_TO_NAME))
# for code in CODE_TO_NAME:
#     print(f"{code:<{code_width}} is {CODE_TO_NAME[code]}")

""" Code rewritten in EAFP """

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(state_code, "is", CODE_TO_NAME[state_code])
        state_code = input("Enter short state: ").upper()
    except KeyError:
        print("Invalid short state")
        state_code = input("Enter short state: ").upper()

code_width = int((max(len(code) for code in CODE_TO_NAME)))
country_width = (max(len(CODE_TO_NAME[code]) for code in CODE_TO_NAME))
for code in CODE_TO_NAME:
    print(f"{code:<{code_width}} is {CODE_TO_NAME[code]}")