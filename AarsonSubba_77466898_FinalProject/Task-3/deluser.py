def delete_user(username):
    with open("passwd.txt", "r") as file:
        # Creating a list excluding the lines with the specified username
        lines = [line for line in file if username not in line]
         

    with open("passwd.txt", "w") as file:
        # Writing back the modified lines to the password file
        file.writelines(lines)

if __name__ == "__main__":
    username = input("Enter username: ")

    with open("passwd.txt", "r") as file:
        # Checking if the user exists before attempting deletion
        if any(username in line for line in file):
            delete_user(username)
            print("User Deleted.")
        else:
            print("User not found. Nothing changed.")
