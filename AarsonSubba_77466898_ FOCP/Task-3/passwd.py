def change_password(username, current_password, new_password):
    with open("passwd.txt", "r") as file:
        # Creating a list with modified password for the specified username
        lines = [line.replace(f"{username}:{current_password}", f"{username}:{new_password}") for line in file]

    with open("passwd.txt", "w") as file:
        # Writing back the modified lines to the password file
        file.writelines(lines)

if __name__ == "__main__":
    username = input("User: ")
    current_password = input("Current Password: ")

    while True:
        new_password = input("New Password: ")
        confirm_password = input("Confirm: ")

        if new_password == confirm_password and new_password:
            break
        elif not new_password:
            print("Password cannot be empty. Please enter a password.")
        else:
            print("Passwords do not match. Please try again.")

    with open("passwd.txt", "r") as file:
        # Checking if the user and current password match before changing
        if any(f"{username}:{current_password}" in line for line in file):
            change_password(username, current_password, new_password)
            print("Password changed.")
        else:
            print("Invalid current password. Nothing changed.")
