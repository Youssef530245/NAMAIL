import os
import pyfiglet

print()
def display_center(text):
    # Get terminal width
    terminal_width = os.get_terminal_size().columns
    
    # Calculate left padding to center the text
    left_padding = (terminal_width - len(text)) // 3
    
    # Display text with padding
    print(" " * left_padding + text)

def main():
    text = "Nannyy"
    banner = pyfiglet.figlet_format(text)
    display_center(banner)
    display_center("####################################")
    display_center("#### Made by Eng Youssef Mohamed ###")
    display_center("####################################")
    print()
    print()
if __name__ == "__main__":
    main()
##-----------------------------------------------------------
class EmailBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, email, password):
        self.contacts[name.lower()] = {'email': email.lower(), 'password': password}

    def get_email_and_password(self, name):
        contact = self.contacts.get(name.lower())
        if contact:
            return contact['email'], contact['password']
        else:
            return "Email not found", "Password not found"

    def get_all_emails_and_passwords(self):
        return [(contact['email'], contact['password']) for contact in self.contacts.values()]

def read_contacts_from_file(file_path):
    email_book = EmailBook()
    try:
        print("Attempting to open file at path:", file_path)
        with open(file_path, "r") as file:
            for line in file:
                name, email, password = line.strip().split(",")
                email_book.add_contact(name, email, password)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error occurred:", e)
    return email_book

def main():
    file_path = input("Enter the path to the file containing names, emails, and passwords: ")
    email_book = read_contacts_from_file(file_path)

    while True:
        print("\n1. Get Email and Password by Name")
        print("2. View All Emails and Passwords")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the name: ")
            email, password = email_book.get_email_and_password(name)
            print("Email:", email)
            print("Password:", password)
        elif choice == "2":
            print("All Emails and Passwords:")
            for email, password in email_book.get_all_emails_and_passwords():
                print("Email:", email, "Password:", password)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
