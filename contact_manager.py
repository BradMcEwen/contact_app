import re

def add_contact(contacts):
    first_name = input("Please enter the first name of the contact you want to add: ").title()
    
    if first_name.isalpha() == True:
        print("First name stored successfully")
        last_name = input("Enter the last name of the contact you would like to add: ").title()
        
        try:
            last_name.isalpha() == True
            print("Last name stored successfully")
            name = first_name + ' ' + last_name
                
        except Exception as e:
            print("The error is:", e)
        if name not in contacts:
            print("Contact name has been added successfully")
            phone_number = input('Enter a valid phone number like so - (Example: "123-456-7890"): ')
            valid_number = re.match(r"\d{3}-\d{3}-\d{4}", phone_number)

            if valid_number:
                print("Number is valid")
                email = input("Enter a valid email address for the contact you would like to add: ").lower()
                valid_email = re.match(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", email)

                if valid_email:
                    print("Valid email")
                else:
                    print("Invalid email")

                add_info = input("Would you like to add additional information to the contact? Enter yes or no: ")
                if add_info == "yes":
                    add_info = input("Enter the info you would like to add (Example: Anniversary, August 3rd): ")
                    print(f"{add_info} has been added to {name}'s contact")

                elif add_info == "no":
                    print("Nothing will be added to additional information")
                    
                else:
                    print("Enter a valid response")
                    
            else:
                print("Invalid number")

        else:
            print("contact name already in use")
    else:
        print("Invalid name")

    contacts[name] = {"phone number": phone_number, "email": email, "additional information": add_info }

def edit_contact(contacts):
    name = input("Enter the first and last name of the contact you would like to make changes to: ").title()

    if name in contacts:
        edit = input('''What would you like to edit? Select an option from the menu below
                     Edit menu:
                     1 - name
                     2 - phone number
                     3 - email
                     ''')
        
        if edit == "1":
            first_name_update = input("Enter the new first name of this contact: ").title()

            if first_name_update.isalpha() == True:
                print("Valid first name")
                last_name_update = input("Enter the new last name for this contact: ").title()

                if last_name_update.isalpha() == True:
                    print("Valid last name")
                    name_update = first_name_update + " " + last_name_update
                    contacts[name_update] = contacts[name]
                    del contacts[name]
                    print(f"The name has been updated, here is your updated contacts list: \n {contacts}")
                else:
                    print("Invalid name entry")
            else:
                print("Invalid name entry")

        elif edit == "2":
            number_update = input('Enter a valid phone number like so (Example "123-456-7890") to change the number: ')
            valid_number = re.match(r"\d{3}-\d{3}-\d{4}", number_update)
            
            if valid_number:
                print("Valid phone number") 
                contacts[name]["Phone Number"] = number_update
                print(f"The phone number has been updated. Here is your updated list of contacts: \n{contacts}")
            
            else:
                print("Invalid phone number entry")


        elif edit == "3":
            email_update = input("Enter a valid email to update in the contact").lower()
            valid_email = re.match(r"\b[A-Za-z0-9À-ÿ._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z0-9]{2,}\b", email_update)

            if valid_email:
                print("Valid email")
                contacts[name]["email"] = email_update
                print(f"Email has been updated. Here is your updated contacts list \n{contacts}")
            
            else:
                print("Invalid email")
        
        else:
            print("The name you entered doesn't match any of your contacts")

def delete_contact(contacts):
    name = input("Enter the full name of the contact you would like to delete: ").title()

    if name in contacts:
        del contacts[name]
        print(f"Successfully deleted. Here is the updated contact list \n{contacts}")

    else:
        print("That name does not match any contacts")

def search_contact(contacts):
    search_choice = input("""Choose how you would like to search for a contact by entering a number from the menu below: 
                
                Category Menu:
                    1 - Name
                    2 - Phone Number 
                    3 - Email
                    """)
    
    if search_choice == "1":
        name = input("Enter the first and last name of the contact you want to search for: ").title()

        if name in contacts:
            print(f"Here is the contact you searched for: \n{contacts[name]}")

        else:
            print("Name not found in contacts")

    elif search_choice == "2":
        phone_number = input('Enter the phone number like so (Example "123-456-7890") of the contact you would like to search: ')
        valid_number = re.match(r"\d{3}-\d{3}-\d{4}", phone_number)
        
        if valid_number:
            for name, value in contacts.items():
                for phone_number, info in value.items():
                        
                        if info == phone_number:
                            print("\nname:", name)
                            print(value)
        
        else: 
            print("You entered an invalid phone number")

    elif search_choice == "3":
        email = input("Enter the email address for the contact you would like to search for: ").lower()

        if email in contacts:
            for name, value in contacts.items():
                for key, info in value.items():
                    if info == email:
                        print("\nname:", name)
                        print(value)

        else:
            print("You entered an invalid email")
    else:
        print("Invalid choice")

def display_contacts(contacts):
    sorted_contacts = dict(sorted(contacts.items()))
    print("Here are your contacts in alphabetical order: ")
    for name in sorted_contacts.items():
        print(f"{sorted_contacts}")

def export_contacts(contacts):
    my_contacts = contacts
    with open("contacts.txt", "w") as file:
        for name, phone_number in my_contacts.items():
            file.write(f"{name}:\n")
            for contact_info, email in name.items():
                file.write(f"  {contact_info}: {email}\n")
        
        
        
def import_contact():
        my_contacts = {}
        with open("my_contacts.txt", "r") as file:
            for line in file:
                name, phone_number, email = line.strip().split(":")
                my_contacts[name] = {f"{phone_number} {email}"}
        print(my_contacts)

def contact_management_system():
    contacts_info = {}
    print("Welcome to the Contact Management System!")
    
    while True: 
        menu_choice = input("""Please select an option below from the menu by entering the number assigned to your desired choice: 
            
            Menu:
                1 - Add a new contact
                2 - Edit an existing contact
                3 - Delete a contact
                4 - Search for a contact
                5 - Display all contacts
                6 - Export contacts to a text file
                7 - Import contacts from a text file
                8 - Quit         
            """)
        
        if menu_choice == "1":
            add_contact(contacts_info)
            
        elif menu_choice == "2":
            edit_contact(contacts_info)
            
        elif menu_choice == "3":
            delete_contact(contacts_info)
            
        elif menu_choice == "4":
            search_contact(contacts_info)
            
        elif menu_choice == "5":
            display_contacts(contacts_info)
            
        elif menu_choice == "6":
            export_contacts(contacts_info)
            
        elif menu_choice == "7":
            import_contact()
            
        elif menu_choice == "8":
            print("Thanks for using the Contact Management System! Good-bye!")
            break
        
        else:
            print("You entered an invalid choice")

contact_management_system()