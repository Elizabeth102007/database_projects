import sqlite3

def create_connection():
        return sqlite3.connect("contacts.db")
    

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS contacts( 
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   name TEXT NOT NULL,
                   phone TEXT,
                   email TEXT)
                   """)
    return "Table created"

def add_contact(connection):
    cursor = connection.cursor()
    name = input("Enter your name: ").capitalize()
    phone = input("Enter your phone: ")
    email = input("Enter your email address: ")
    params = {"name": name, "phone": phone, "email": email}
    query = ("""
                  INSERT INTO contacts(name, phone, email)
                  VALUES (:name,:phone,:email)
                  """)
    
    with connection:
         cursor.execute(query, params)
    print("Contact Added successfully")

def view_contacts(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM contacts")
    
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)



def search_contact(connection):
    cursor = connection.cursor()
    name = input("Enter the name you want to search for: ").capitalize()
    params = {"name": name}
    query = ("""
             SELECT * FROM contacts 
             WHERE name = :name
            """)
    params = {"name": name}
    
    cursor.execute(query, params)
    row = cursor.fetchone()
    print(row)

def update_contact(connection):
    view_contacts(connection)
    cursor = connection.cursor()
    contact_id = input("Which id will you like to update in?: ")
    update = input("What will you like to update(name or phone or email): ").lower()
    if update == "name":
        name = input("Enter your new name: ").capitalize()
        query = ("""
                 UPDATE contacts
                 SET name = :name
                 WHERE id = :id
                 """)
        params_name = {"name": name, "id": contact_id}
        with connection:
            cursor.execute(query, params_name)
            print("Name updated successfully!")

    elif update == "phone":
        phone = input("Enter your new phone number: ")
        query = ("""
                 UPDATE contacts
                 SET phone = :phone
                 WHERE id = :id
                """)
        params_phone = {"phone": phone, "id": contact_id}
        with connection:
            cursor.execute(query, params_phone)
            print("Phone updated successfully!")

    elif update == "email":
        email = input("Enter your new email address: ")
        query = ("""
                 UPDATE contacts
                 SET email = :email
                 WHERE id = :id
                 """)
        params_email = {"email": email, "id": contact_id}
        with connection:
            cursor.execute(query, params_email)
            print("Email updated successfully!")
    else:
        print("Invalid input. You can only update name or phone or email.")

def delete_contact(connection):
    view_contacts(connection)
    cursor = connection.cursor()
    id = input("Enter the id you will like to delete: ")
    params = {"id": id}
    query = ("""
              DELETE FROM contacts 
              WHERE id = :id
            """)
    with connection:
        cursor.execute(query, params)
        print("Contact deleted successfully")

def menu():
    print("=================CONTACT BOOK CLI===============")
    
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("0. Exit")

def main():
    connection = create_connection()
    print(create_table(connection))

    menu()
    while True:
        choice = input("Enter the action you will like to perform: ")
        
        if choice == "1":
            add_contact(connection)

        elif choice == "2":
            view_contacts(connection)

        elif choice == "3":
            search_contact(connection)

        elif choice == "4":
            update_contact(connection)

        elif choice == "5":
            delete_contact(connection)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Check the options and try again")
            continue

if __name__ == "__main__":
    main()

        


    
    

            

            
            



    
    
    