class Phonebook:
    def __init__(self):
        self.contacts = {}  # Initialize an empty dictionary to store contacts

    def add_contact(self, name, number):
        self.contacts[name] = number  # Add a contact to the dictionary
        print("Contact added successfully!")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for name, number in self.contacts.items():
                print(f"{name}: {number}")
        else:
            print("No contacts found.")


def main():
    phonebook = Phonebook()  # Create an instance of the Phonebook class

    while True:
        print("\nPhonebook Organizer")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter number: ")
            phonebook.add_contact(name, number)
        elif choice == "2":
            phonebook.display_contacts()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()  # Run the main function if the script is executed directly
