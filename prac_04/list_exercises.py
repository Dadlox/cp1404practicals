"""
Basic list operations
"""
# def main():
#     numbers = []
#     while len(numbers) < 5:
#         number = int(input("Input a number: "))
#         numbers.append(number)
#     print(numbers)
#     print(f"The first number is {numbers[0]}")
#     print(f"The last number is {numbers[4]}")
#     print(f"The smallest number is {min(numbers)}")
#     print(f"The largest number is {max(numbers)}")
#     print(f"The average number is {sum(numbers)/len(numbers)}")
# main()

"""
Woefully inadequate security checker
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter your username: ")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")