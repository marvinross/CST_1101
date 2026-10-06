import getpass
CORRECT_USERNAME = "rossm"
CORRECT_PASSWORD = "Echo3791"

attempts = 0
max_attempts = 5

while attempts < max_attempts:
    username = input("Enter Username: ")
    password = getpass.getpass("Enter Password: ", echo_char="*")

    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print("Login successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        print(f"Incorrect. Remaining attempts: {remaining}\n")

else:
    print("Too many failed attempts. Access Denied.")