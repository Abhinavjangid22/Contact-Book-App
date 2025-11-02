CONTACT_FILE = "contacts.txt"

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")

    with open(CONTACT_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("Contact added successfully!\n")


def view_contacts():
    print("\n--- Contact List ---")
    try:
        with open(CONTACT_FILE, "r") as file:
            contacts = file.readlines()
            if not contacts:
                print("No contacts found.\n")
                return
            for contact in contacts:
                name, phone, email = contact.strip().split(",")
                print(f"Name: {name}\nPhone: {phone}\nEmail: {email}\n")
    except FileNotFoundError:
        print("No contacts file found. Add a contact first.\n")


def search_contact():
    keyword = input("Enter name or phone to search: ").lower()
    found = False
    try:
        with open(CONTACT_FILE, "r") as file:
            for contact in file:
                name, phone, email = contact.strip().split(",")
                if keyword in name.lower() or keyword in phone:
                    print(f"\n🔍 Found Contact:\nName: {name}\nPhone: {phone}\nEmail: {email}\n")
                    found = True
        if not found:
            print("No matching contact found.\n")
    except FileNotFoundError:
        print("No contacts file found.\n")


def main():
    while True:
        print("=== CONTACT BOOK ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Try again.\n")


if __name__ == "__main__":
    main()
