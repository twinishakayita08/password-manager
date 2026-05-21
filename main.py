# Simple Password Manager
# Save password
def save_password():

    website = input("Enter website name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open("passwords.txt", "a")

    file.write(
        website + " | " +
        username + " | " +
        password + "\n"
    )

    file.close()

    print("Password saved successfully!\n")


# View passwords
def view_passwords():

    try:
        file = open("passwords.txt", "r")

        data = file.read()

        print("\nSaved Passwords:\n")
        print(data)

        file.close()

    except:
        print("No passwords saved yet.\n")


# Main Program
while True:

    print("===== PASSWORD MANAGER =====")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        save_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice\n")
