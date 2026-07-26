# Contact Book CLI

A command-line contact management application built with Python and SQLite. The application allows users to create, view, search, update, and delete contacts stored in a local SQLite database.

Unlike a file-based contact book that stores data in CSV or JSON files, this project uses a relational database and SQL queries to manage persistent contact records.

## How It Works

```text
User
 ↓
CLI Menu
 ↓
Python Application
 ↓
SQLite Database Connection
 ↓
contacts.db
```

When the program starts, it:

1. Creates a connection to the SQLite database.
2. Creates the `contacts` table if it does not already exist.
3. Displays the available contact management operations.
4. Allows the user to perform CRUD operations on stored contacts.

## Features

* Add new contacts
* View all contacts
* Search for a contact by name
* Update contact information
* Delete contacts
* Persistent local data storage
* Automatic database and table creation
* SQL parameter binding
* Transaction management using Python's `with connection:` syntax
* Interactive command-line interface

## Contact Data

Each contact contains:

| Column  | Description                               |
| ------- | ----------------------------------------- |
| `id`    | Automatically generated unique identifier |
| `name`  | Contact's name                            |
| `phone` | Contact's phone number                    |
| `email` | Contact's email address                   |

The database table is created with:

```sql
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT
);
```

## CRUD Operations

This project demonstrates the four fundamental database operations:

| Operation | SQL Command | Purpose                    |
| --------- | ----------- | -------------------------- |
| Create    | `INSERT`    | Add a new contact          |
| Read      | `SELECT`    | View or search contacts    |
| Update    | `UPDATE`    | Modify contact information |
| Delete    | `DELETE`    | Remove a contact           |

### Create

Users can add a new contact with a name, phone number, and email address.

```sql
INSERT INTO contacts(name, phone, email)
VALUES (:name, :phone, :email);
```

### Read

The application can retrieve all contacts:

```sql
SELECT * FROM contacts;
```

It can also search for a specific contact by name:

```sql
SELECT * FROM contacts
WHERE name = :name;
```

### Update

Individual contact fields can be updated:

```sql
UPDATE contacts
SET name = :name
WHERE id = :id;
```

The application supports updating:

* Name
* Phone number
* Email address

### Delete

Contacts can be removed using their unique ID:

```sql
DELETE FROM contacts
WHERE id = :id;
```

---

## How To Run

SQLite is included in Python's standard library, so no external package installation is required.

Run the program with:

```bash
python main.py
```

The `contacts.db` database file will be created automatically when the program runs.

---

## Example Menu

```text
=================CONTACT BOOK CLI===============

1. Add contact
2. View contacts
3. Search contact
4. Update contact
5. Delete contact
0. Exit
```

## Example Usage

### Adding a Contact

```text
Enter your name: Jenny
Enter your phone: 123456789
Enter your email address: jenny@example.com

Contact Added successfully
```

### Viewing Contacts

```text
(1, 'Jenny', '123456789', 'jenny@example.com')
(2, 'John', '987654321', 'john@example.com')
```

### Searching for a Contact

```text
Enter the name you want to search for: Jenny

(1, 'Jenny', '123456789', 'jenny@example.com')
```

---

## Database Connection

The application creates a connection to the SQLite database using:

```python
def create_connection():
    return sqlite3.connect("contacts.db")
```

This creates or opens the local:

```text
contacts.db
```

SQLite is a file-based relational database, meaning the entire database is stored locally in a single file.

---

## Transactions and `with connection:`

The project uses:

```python
with connection:
    cursor.execute(query, params)
```

for database-changing operations such as `INSERT`, `UPDATE`, and `DELETE`.

This allows SQLite to manage the transaction automatically:

* If the operation succeeds, the changes are committed.
* If an error occurs, the transaction can be rolled back.

This is one of the important database concepts demonstrated in the project.

---

## SQL Parameter Binding

The project uses named parameters instead of directly inserting user input into SQL queries:

```python
params = {
    "name": name,
    "phone": phone,
    "email": email
}
```

Then:

```python
cursor.execute(query, params)
```

For example:

```sql
INSERT INTO contacts(name, phone, email)
VALUES (:name, :phone, :email);
```

This is safer and helps prevent SQL injection compared with building SQL queries using string concatenation.

---

## Project Structure

```text
contact-book-cli/
│
├── main.py
├── contacts.db
└── README.md
```

### `main.py`

Contains the application logic, including:

* Database connection
* Table creation
* Adding contacts
* Viewing contacts
* Searching contacts
* Updating contacts
* Deleting contacts
* Menu management

### `contacts.db`

The local SQLite database that stores the contact records.

If the database does not exist, SQLite creates it automatically.

---

## Topics Covered

* Python
* SQLite
* Relational databases
* SQL
* `sqlite3`
* Database connections
* Cursors
* Tables
* Primary keys
* `AUTOINCREMENT`
* `NOT NULL` constraints
* `INSERT`
* `SELECT`
* `UPDATE`
* `DELETE`
* SQL parameter binding
* Transactions
* Database persistence
* CRUD operations
* Command-line interfaces

---

## Key Concepts Demonstrated

This project demonstrates the transition from storing application data in files to using a database.

A file-based application might store data like this:

```text
Python Application
       ↓
CSV / JSON File
```

This project uses:

```text
Python Application
       ↓
SQL Query
       ↓
SQLite Database
       ↓
contacts.db
```

The application also demonstrates how a database-backed application performs CRUD operations:

```text
Create  → INSERT
Read    → SELECT
Update  → UPDATE
Delete  → DELETE
```

Overall, this project provides practical experience with **Python database programming, SQL queries, SQLite persistence, transactions, and building a complete CRUD command-line application**.
