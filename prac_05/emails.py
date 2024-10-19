"""
CP1404/CP5632 Practical
Name: Hein Htet
Make a program to collect Email, store them in a dictionary with their name
Estimate: 30 minutes
Actual:23 minutes
"""


def main():
    email_to_username = {}
    email = input("Email: ")
    while email != "":
        username = get_name(email).title()
        user_confirmation = input(f"Is your name {username}? Y/n  ").lower()
        if user_confirmation == "y":
            email_to_username[email] = username
        else:
            username = input("Enter your name: ").title()
            email_to_username[email] = username
        email = input("Email: ")

    for email, username in email_to_username.items():
        print(f"{username} ({email})")


def get_name(email):
    name_part = email.split('@')[0] #Splits the email into two bits, take the first bit(In this case, everything before @)
    name = " ".join(name_part.split('.')).title()
    return name


main()
