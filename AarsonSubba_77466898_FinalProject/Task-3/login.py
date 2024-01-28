def login(username, password):
    with open("passwd.txt", "r") as file:
        # Checking if the username and password match any entry in the file
        return any(f"{username}:{password}" in line for line in file)

if __name__ == "__main__":
    username = input("User: ")
    password = input("Password: ")

    # Checking if the login is successful
    if login(username, password):
        print("Access granted.")
    else:
        print("Access denied.")
    
