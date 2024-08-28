import re
import os

# Contact storage
contacts = {}

# Utility functions
def validate_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

def validate_phone(phone):
    return re.match(r"\+?\d{10,15}", phone) is not None

def print_menu():
    print("\nWelcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file (BONUS)")
    print("8. Quit")

def add_contact():
    identifier = input("Enter phone number or email as the unique identifier: ").strip()
    if identifier in contacts:
        print("Contact already exists.")
        return
    name = input("Enter the name: ").strip()
    phone = input("Enter the phone number: ").strip()
    email = input("Enter the email address: ").strip()
    additional_info = input("Enter additional information: ").strip()
    
    if not validate_email(email):
        print("Invalid email format.")
        return
    
    if not validate_phone(phone):
        print("Invalid phone number format.")
        return

    contacts[identifier] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info
    }
    print("Contact added successfully.")

def edit_contact():
    identifier = input("Enter the phone number or email of the contact to edit: ").strip()
    if identifier not in contacts:
        print("Contact not found.")
        return
    print("Leave fields blank if you don't want to change them.")
    name = input("Enter the new name: ").strip() or contacts[identifier]['Name']
    phone = input("Enter the new phone number: ").strip() or contacts[identifier]['Phone']
    email = input("Enter the new email address: ").strip() or contacts[identifier]['Email']
    additional_info = input("Enter additional information: ").strip() or contacts[identifier]['Additional Info']
    
    if not validate_email(email):
        print("Invalid email format.")
        return
    
    if not validate_phone(phone):
        print("Invalid phone number format.")
        return

    contacts[identifier] = {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info
    }
    print("Contact updated successfully.")

def delete_contact():
    identifier = input("Enter the phone number or email of the contact to delete: ").strip()
    if identifier not in contacts:
        print("Contact not found.")
        return
    del contacts[identifier]
    print("Contact deleted successfully.")

def search_contact():
    search_term = input("Enter the name, phone number, or email of the contact to search: ").strip()
    found = False
    for identifier, info in contacts.items():
        if (search_term.lower() in info['Name'].lower() or
            search_term in info['Phone'] or
            search_term in info['Email']):
            print(f"Identifier: {identifier}")
            print(f"Name: {info['Name']}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print(f"Additional Info: {info['Additional Info']}")
            print()
            found = True
    if not found:
        print("No contact found.")

def display_contacts():
    if not contacts:
        print("No contacts to display.")
        return
    for identifier, info in contacts.items():
        print(f"Identifier: {identifier}")
        print(f"Name: {info['Name']}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
        print(f"Additional Info: {info['Additional Info']}")
        print()

def export_contacts():
    filename = input("Enter the filename to export to: ").strip()
    with open(filename, 'w') as file:
        for identifier, info in contacts.items():
            file.write(f"Identifier: {identifier}\n")
            file.write(f"Name: {info['Name']}\n")
            file.write(f"Phone: {info['Phone']}\n")
            file.write(f"Email: {info['Email']}\n")
            file.write(f"Additional Info: {info['Additional Info']}\n")
            file.write("\n")
    print(f"Contacts exported to {filename} successfully.")

def import_contacts():
    filename = input("Enter the filename to import from: ").strip()
    if not os.path.exists(filename):
        print("File not found.")
        return
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 6):
            identifier = lines[i].split(": ")[1].strip()
            name = lines[i+1].split(": ")[1].strip()
            phone = lines[i+2].split(": ")[1].strip()
            email = lines[i+3].split(": ")[1].strip()
            additional_info = lines[i+4].split(": ")[1].strip()
            
            if identifier not in contacts:
                contacts[identifier] = {
                    'Name': name,
                    'Phone': phone,
                    'Email': email,
                    'Additional Info': additional_info
                }
    print("Contacts imported successfully.")

def main():
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Quitting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
