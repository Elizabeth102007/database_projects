import sqlite3

def create_connection():
        return sqlite3.connect("contacts.db")
    

def create_table(connection):
    cursor = connection.cursor()
    with connection:
         cursor.execute("""
                   CREATE TABLE IF NOT EXISTS contacts( 
                   id INTEGER PRIMARY KEY AUTOINCREMENT, 
                   name TEXT NOT NULL,
                   phone TEXT,
                   email TEXT,
                   city TEXT)
                   """)
    

def add_contact(connection):
    cursor = connection.cursor()
    name = input("Enter your name: ").capitalize()
    phone = input("Enter your phone: ")
    email = input("Enter your email address: ")
    city = input("Enter the city you live in: ").capitalize()
    params = {"name": name, "phone": phone, "email": email, "city": city}
    query = ("""
                  INSERT INTO contacts(name, phone, email, city)
                  VALUES (:name,:phone,:email,:city)
                  """)
    
    with connection:
         cursor.execute(query, params)
    print("Contact Added successfully")
    contact_id = cursor.lastrowid
    print(f"Contact ID: {contact_id}")

def view_contacts(connection):
    cursor = connection.cursor()
    order = input("How do you want to view your cntacts in order(normal or ascend or descend?): ").lower()
    if order == "normal":
       query = ("""SELECT * FROM contacts
                """)
       cursor.execute(query)
       rows = cursor.fetchall()
       if not rows:
           print("NO contacts found")
       else:
          for row in rows:
              print(row)

    elif order == "ascend":
        query = ("""SELECT * FROM contacts
                 ORDER BY name;
                """)
        cursor.execute(query)
        rows = cursor.fetchall()
        if not rows:
            print("No contacts found")
        else:
            for row in rows:
                print(row)

    elif order == "descend":
           query = ("""SELECT * FROM contacts
                    ORDER BY name DESC
                    """)
           cursor.execute(query)
           rows = cursor.fetchall()
           if not rows:
              print("No contacts found")
           else:
              for row in rows:
                print(row)

def search_contact(connection):
    cursor = connection.cursor()
    name = input("Enter the name you want to search for: ").capitalize()
    params = {"name": name}
    query = ("""
             SELECT * FROM contacts 
             WHERE name LIKE :name
            """)
    params = {"name": f"%{name}%"}
    
    cursor.execute(query, params)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def update_contact(connection):
    cursor = connection.cursor()
    contact_id = input("Which id will you like to update in?: ")
    update = input("What will you like to update(name or phone or email or city): ").lower()
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

    elif update == "city":
            city = input("Enter your city: ").capitalize()
            query = ("""
                     UPDATE contacts
                     SET city = :city
                     WHERE id = :id
                     """)
            params_city = {"city": city, "id": contact_id}
            with connection:
                cursor.execute(query, params_city)
                print("City updated successfully!")
    else:
        print("Invalid input. You can only update name or phone or email.")

def count_contacts(connection):
    cursor = connection.cursor()
    
    cursor.execute("""
             SELECT COUNT(*)
             FROM contacts;
             """)
    result = cursor.fetchone()
    # result returns a tuple(because of fetchone()) in this format e.g: (4,)
    count = result[0]
    # result[0] makes it possible to access only the number
    print(f"Total contacts : {count}")

def count_contacts_by_city(connection):
    cursor = connection.cursor()
    cursor.execute("""
                   SELECT city, COUNT(*) AS contact_count
                   FROM contacts
                   GROUP BY city
                  """)

    rows = cursor.fetchall()
    for city, count in rows:
        print(f"{city}: {count} contact(s)")

       
def delete_contact(connection):
    cursor = connection.cursor()
    contact_id = input("Enter the id you will like to delete: ")
    params = {"id": contact_id}
    query = ("""
              DELETE FROM contacts 
              WHERE id = :id
            """)
    with connection:
        cursor.execute(query, params)

        print("Contact deleted successfully")
        

def menu():
    print("=================CONTACT MANAGER CLI===============")
    
    print("1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Count contact")
    print("7. Count contacts by city")
    print("0. Exit")

def main():
    connection = create_connection()
    try: 
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

           elif choice == "6":
               count_contacts(connection)

           elif choice == "7":
               count_contacts_by_city(connection)

           elif choice == "0":
               break

           else:
              print("Invalid choice. Check the options and try again")
              continue
    finally:
        connection.close()

if __name__ == "__main__":
    main()




    
    

            

            
            



    
    
    