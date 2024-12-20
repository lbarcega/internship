class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

class AddressBook:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"{contact.name} has added to the address book.\n")
    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"{name} deleted from the address book.\n")
            else:
                print(f"No matches found for '{name}'\n")
    def search_contact(self, search):
        search_match = []
        for contact in self.contacts:
            if (search.lower() in contact.name.lower()) or (search in contact.phone) or (search in contact.email):
                search_match.append(contact)
        if search_match:
            search_index = 0
            print(f"Found {len(search_match)} match for '{search}':")
            for contact in search_match:
                search_index += 1
                print(f"({search_index})")
                print(contact,"\n")
            return search_match
        else:
            print(f"No matches found for '{search}'\n")

    def print_all_contacts(self):
        search_index = 0
        print(f"There are {len(self.contacts)} contacts in your address book.")
        for contact in self.contacts:
            search_index += 1
            print(f"({search_index})")
            print(f"{contact}\n")

    def edit_contact(self, search):
        search_match = self.search_contact(search)
        contact_index = 0
        if search_match and len(search_match) > 0:
            while True:
                try:
                    contact_index = int(input("Select from the list: ")) - 1
                    if 0 <= contact_index < len(search_match):
                        break
                    else:
                        print("Invalid index. Select a number from the options.\n")
                except ValueError:
                    print("Invalid input. Select a number from the options.\n")
            print(f"({contact_index + 1})\n{search_match[contact_index]}\n")
        else:
            return
        
        for contact in self.contacts:
            if contact.name == search_match[contact_index].name:
                while True:
                    new_field = input("Enter the new value: ")
                    edit_field = input("Edit which field?\n(1) Name\n(2) Phone\n(3) Email\n")
                    if edit_field == '1':
                        contact.name = new_field
                        break
                    elif edit_field == '2':
                        contact.phone = new_field
                        break
                    elif edit_field == '3':
                        contact.phone = new_field
                        break
                    else:
                        print(f"Invalid input. Select a number from the options.\n")
                print(f"Contact for {contact.name} updated.\n")

def use_address_book():
    address = AddressBook()
    c1 = Contact("Janelle Zamora", "09291291929", "jzamora@gmail.com")
    c2 = Contact("Janelle Dimaapi", "0123123123", "jdimaapi@gmail.com")
    address.add_contact(c1)
    address.add_contact(c2)

    print("Welcome to your Address Book!")
    while True:
        print(f"Select an option:\n(1) Display all contacts\n(2) Search for a contact\n(3) Add a new contact\n(4) Edit a contact\n(5) Delete a contact\n(6) Exit\n")
        option = input()
        if option == '1':
            address.print_all_contacts()
        elif option == '2':
            search = input("Search for: ")
            address.search_contact(search)
        elif option == '3':
            print(f"Add contact:")
            while True:
                try:
                    name = str(input("Name: "))
                    phone = int(input("Phone: "))
                    email = str(input("Email: "))
                    break
                except ValueError:
                    print("Invalid input. Try again.")
            address.add_contact(Contact(name, phone, email))
        elif option == '4':
            name = input(f"Edit contact: ")
            address.edit_contact(name)
        elif option == '5':
            name = input(f"Delete contact (Enter the full name): ")
            address.delete_contact(name)
        elif option == '6':
            print("Have a nice day!\n")
            break
        else:
            print("Invalid input. Select a number from the options.\n")

use_address_book()