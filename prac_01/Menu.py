"""
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""
def menu():
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

name = input("Input name: ")
menu()
choice = input(">>>")
while choice.upper() != "Q":
    if choice.upper() == "H":
        print(f"Hello, {name}")
    elif choice.upper() == "G":
        print(f"Goodbye, {name}")
    else:
        print("Invalid choice, try again")
    choice = input(">>>")
print("Quiting program")
