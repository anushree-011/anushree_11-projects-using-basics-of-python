contacts = {}

def add_contact(name,phone,email):
    contacts[name] = {'phone':phone,'email':email}
    print(f"{name} has been added to your contacts")
def delete_contact(name):
    if name in contacts:
        del contacts[name]
        print(f"{name} has been deleted from your contact")
    else:
        print(f"{name} is not your contact")
def search_contact(name):
    if name in contacts:
        print(f'{name}: {contacts[name]["phone"]},{contacts[name]["email"]}')
    else:
        print(f"{name} is not your contact")
def print_contact():
    for name,contact in contacts.items():
        print(f"{name}:{contact['phone']},{contact['email']}")

while True:
    print("Address Book")
    print("1.Add Contact")
    print("2.Delete Contact")
    print("3.Search Contact")
    print("4.Print Contact")
    print("5.Quit")

    choice = input("Enter your choice:")

    if choice =='1':
        name = input("Enter name :")
        phone = input("Enter Phone Number :")
        email = input("Enter email address :")
        add_contact(name,phone,email)

    elif choice =='2':
        name=input("Enter name :")
        delete_contact(name)

    elif choice == '3':
        name=input("Enter name :")
        search_contact(name)

    elif choice =='4':
        print_contact()

    elif choice =='5':
        print("Goodbye")
        break

    else:
        print("Invalid choice. Please try again.")
