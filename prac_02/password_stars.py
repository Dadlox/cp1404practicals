"""
Task: Password check with Functions
By: Hein Htet/David Linn
"""

def main():
    """Function: getting password"""
    password = get_password()
    print(password)

def get_password():
    """Get password"""
    input_password = input("Enter password: ")
    check_password = input("Enter password again to ensure: ")

    """If the password isn't the same as the first one, ask until there's two same password"""
    while input_password != check_password:
        print("Password doesn't match up.")
        input_password = input("Enter password: ")
        check_password = input("Enter password again to ensure: ")
    return input_password

main()