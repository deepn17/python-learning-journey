print("=" * 50)
print("Welcome to the Contact Book")
print("=" * 50 )

contact_list = []

while True:
    print("\n What would you like to do today? Please select the options from (1 - 5): ")
    print("\n 1. Add New Contact")
    print(" 2. View Contact List")
    print(" 3. Edit/Update Existing contact")
    print(" 4. Delete Contact")
    print(" 5. Quit the Application")

    choice = input("Enter the option (1 - 5): ").strip()

    if not choice.isdigit():
        print("Enter a digit from (1 - 5) for valid actions: ")
        continue

    if int(choice) < 1 or int(choice) > 5:
        print("Enter a digit from (1 - 5) for valid actions:")
        continue

    if choice == "1":
        print("\n--- Add New Contact ---")
        name = input("Enter the name: ").strip()
        while not name:
            name = input("Name can't be empty. Enter the name: ").strip()
        phone = input("Enter the Phone-No with country code. E.g.- (+91): ").strip()
        while not phone:
            phone = input("Phone-No can't be empty. Enter the Phone-No with country code. E.g.- (+91): ").strip()
        email = input("Enter the email: ").strip()
        while not email:
            email = input("Email can't be empty. Enter the email: ").strip()
        contact_dict = {"Name": name,
                        "Phone": phone,
                        "Email": email}
        contact_list.append(contact_dict)
        print(f"\n{name} was added successfully")
    elif choice == "2":
        print("\n--- View Contact List ---")
        if not contact_list:
            print("No Contacts Found. Add one first!")
        else:
            for index,contact in enumerate(contact_list):
                print(f"SNO: {index + 1} | info: {contact}")
    elif choice == "3":
        print("\n--- Edit/Update Existing contact ---")
        if not contact_list:
            print("No Contacts Found. Add one first!")
            continue

        contact_edit = input("Enter the SNO of the contact to edit: ").strip()

        while not contact_edit.isdigit():
            contact_edit = input("Enter a valid SNO of the contact to edit: ").strip()

        while int(contact_edit) < 1 or int(contact_edit) > len(contact_list):
            contact_edit = input("SNO Not Found. Enter a valid SNO of the contact to edit: ").strip()
            while not contact_edit.isdigit():
                contact_edit = input("Enter a valid SNO of the contact to edit: ").strip()

        selected_contact = contact_list[int(contact_edit) - 1]
        print(f"\n Selected Contact for Update: {selected_contact}")

        update = input("What should be updated? Name, Phone-No or Email or all: ").lower().strip()

        while update not in ["name", "phone-no", "email", "all"]:
            print("Please enter Name, Phone-No, Email or All.")
            update = input("What should be updated? Name, Phone-No, Email or All: ").lower().strip()

        if update == "name":
            new_name = input("Enter the new name to be updated: ").strip()
            while not new_name:
                new_name = input("Name can't be empty. Enter the new name to be updated: ").strip()

            selected_contact["Name"] = new_name

        elif update == "phone-no":
            new_phone_no = input("Enter the new phone-no to be updated: ").strip()
            while not new_phone_no:
                new_phone_no = input("Phone-No can't be empty. Enter the new phone-no to be updated: ").strip()

            selected_contact["Phone"] = new_phone_no

        elif update == "email":
            new_email = input("Enter the new email to be updated: ").strip()
            while not new_email:
                new_email = input("Email can't be empty. Enter the new email to be updated: ").strip()

            selected_contact["Email"] = new_email

        elif update == "all":
            new_name = input("Enter the new name to be updated: ").strip()
            while not new_name:
                new_name = input("Name can't be empty. Enter the new name to be updated: ").strip()

            new_phone_no = input("Enter the new phone-no to be updated: ").strip()
            while not new_phone_no:
                new_phone_no = input("Phone-No can't be empty. Enter the new phone-no to be updated: ").strip()

            new_email = input("Enter the new email to be updated: ").strip()
            while not new_email:
                new_email = input("Email can't be empty. Enter the new email to be updated: ").strip()

            selected_contact["Name"] = new_name
            selected_contact["Phone"] = new_phone_no
            selected_contact["Email"] = new_email

        print(f"\nContact updated successfully: {selected_contact}")

    elif choice == "4":
        print("\n--- Delete Contact ---")
        if not contact_list:
            print("No Contacts Found. Add one first!")
            continue

        contact_delete = input("Enter the SNO of the contact that you wish to delete: ").strip()

        while not contact_delete.isdigit():
            contact_delete = input("Enter a valid SNO of the contact that you wish to delete: ").strip()

        while int(contact_delete) < 1 or int(contact_delete) > len(contact_list):
            contact_delete = input("SNO Not Found. Enter a valid SNO of the contact to delete: ").strip()
            while not contact_delete.isdigit():
                contact_delete = input("Enter a valid SNO of the contact that you wish to delete: ").strip()

        delete_contact = contact_list[int(contact_delete) - 1]
        print(f"\n Selected Contact for Deletion: {delete_contact}")

        confirmation = input(f"Are you sure you want to delete {delete_contact['Name']} from your contact list?"
                             f" Press Y to continue or N to cancel the operation.").strip().lower()

        while confirmation not in ("y", "n"):
            confirmation = input("Please enter Y or N: ").strip().lower()

        if confirmation == "y":
            contact_list.pop(int(contact_delete) - 1)
            print(f"\n{delete_contact['Name']} was deleted successfully.")
        else:
            print("You chose not to delete.")

    elif choice == "5":
        print("Good Bye! Have a good day.")
        break





