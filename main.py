import json
import os

class ContactManager:
    def __init__(self, filename='contacts.json'):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return []

    def save_contacts(self):
        with open(self.filename, 'w') as file:
            json.dump(self.contacts, file, indent=4)

    def add_contact(self, name, phone, email):
        contact = {
            'name': name,
            'phone': phone,
            'email': email
        }
        self.contacts.append(contact)
        self.save_contacts()
        print(f'Contact {name} added successfully!')

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for index, contact in enumerate(self.contacts):
            print(f"{index + 1}: {contact['name']} - {contact['phone']} - {contact['email']}")

    def edit_contact(self, index, name=None, phone=None, email=None):
        if 0 <= index < len(self.contacts):
            if name:
                self.contacts[index]['name'] = name
            if phone:
                self.contacts[index]['phone'] = phone
            if email:
                self.contacts[index]['email'] = email
            self.save_contacts()
            print('Contact updated successfully!')
        else:
            print('Invalid contact index.')

    def delete_contact(self, index):
        if 0 <= index < len(self.contacts):
            removed_contact = self.contacts.pop(index)
            self.save_contacts()
            print(f'Contact {removed_contact["name"]} deleted successfully!')
        else:
            print('Invalid contact index.')

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            manager.add_contact(name, phone, email)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            manager.view_contacts()
            index = int(input("Enter contact number to edit: ")) - 1
            name = input("Enter new name (leave blank to keep unchanged): ")
            phone = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            manager.edit_contact(index, name or None, phone or None, email or None)

        elif choice == '4':
            manager.view_contacts()
            index = int(input("Enter contact number to delete: ")) - 1
            manager.delete_contact(index)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
