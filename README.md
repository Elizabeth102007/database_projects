# Contact Manager CLI

A command-line contact management application built with **Python** and **SQLite**. The application allows users to manage a personal contact database by adding, viewing, searching, updating, deleting, and analyzing contacts through SQL queries.

Unlike a file-based contact book that stores information in CSV or JSON files, this project uses a **SQLite relational database**, providing persistent storage, efficient querying, and structured data management.

---

# How It Works

```text
User
   │
   ▼
CLI Menu
   │
   ▼
Python Application
   │
   ▼
SQLite Database (contacts.db)
```

When the program starts, it:

* Connects to a local SQLite database
* Creates the `contacts` table if it does not already exist
* Displays an interactive menu
* Executes SQL queries based on the user's selected operation
* Automatically saves all changes to the database

---

# Features

* Add new contacts
* View all contacts
* Sort contacts alphabetically (ascending or descending)
* Search contacts using partial name matching
* Update existing contact information
* Delete contacts
* Count the total number of contacts
* Count contacts grouped by city
* Automatically generate unique contact IDs
* Persistent data storage using SQLite
* Automatic database and table creation
* Safe SQL parameter binding
* Transaction management using context managers
* Automatic database connection cleanup

---

# Contact Information

Each contact stores the following information:

| Field | Description                      |
| ----- | -------------------------------- |
| ID    | Auto-generated unique identifier |
| Name  | Contact's full name              |
| Phone | Phone number                     |
| Email | Email address                    |
| City  | City of residence                |

The table is automatically created using:

```sql
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone TEXT,
    email TEXT,
    city TEXT
);
```

---

# CRUD Operations

The project demonstrates the four fundamental database operations.

| Operation | SQL Command | Purpose                  |
| --------- | ----------- | ------------------------ |
| Create    | `INSERT`    | Add new contacts         |
| Read      | `SELECT`    | View and search contacts |
| Update    | `UPDATE`    | Modify contact details   |
| Delete    | `DELETE`    | Remove contacts          |

---

## Add Contact

Users can add a contact with:

* Name
* Phone number
* Email address
* City

After insertion, SQLite automatically generates a unique ID using:

```sql
AUTOINCREMENT
```

The application displays the generated contact ID using:

```python
cursor.lastrowid
```

---

## View Contacts

Contacts can be displayed in three different ways:

* Normal order
* Alphabetical order (A → Z)
* Reverse alphabetical order (Z → A)

This demonstrates SQL sorting with:

```sql
ORDER BY name
```

and

```sql
ORDER BY name DESC
```

---

## Search Contacts

Users can search for contacts using part of a name instead of requiring an exact match.

For example, searching:

```
Ann
```

can match:

```
Ann
Anna
Annabelle
Joanne
```

This is achieved using SQL's `LIKE` operator:

```sql
SELECT *
FROM contacts
WHERE name LIKE :name;
```

---

## Update Contacts

Users can update individual fields without modifying the entire record.

Supported updates include:

* Name
* Phone
* Email
* City

Each update uses SQL's `UPDATE` statement with parameterized queries.

---

## Delete Contacts

Contacts are deleted using their unique ID.

```sql
DELETE FROM contacts
WHERE id = :id;
```

---

# Contact Statistics

The application also performs simple database analysis using SQL aggregate functions.

## Total Contacts

Displays the total number of contacts stored.

Uses:

```sql
SELECT COUNT(*)
FROM contacts;
```

---

## Contacts by City

Groups contacts according to their city and counts how many contacts belong to each city.

Example output:

```text
Cairo: 5 contact(s)
Lagos: 3 contact(s)
Abuja: 2 contact(s)
```

This demonstrates SQL aggregation with:

```sql
SELECT city, COUNT(*)
FROM contacts
GROUP BY city;
```

---

# Database Transactions

Database-modifying operations are wrapped using:

```python
with connection:
```

This automatically manages transactions by:

* Committing successful operations
* Rolling back failed operations when necessary

Operations using transactions include:

* INSERT
* UPDATE
* DELETE
* CREATE TABLE

---

# SQL Parameter Binding

Instead of building SQL statements using string concatenation, the project uses named parameters.

Example:

```python
params = {
    "name": name,
    "phone": phone,
    "email": email,
    "city": city
}

cursor.execute(query, params)
```

This approach:

* Improves code readability
* Separates SQL from user input
* Helps protect against SQL injection attacks

---

# Database Connection Management

The application creates a single database connection at startup:

```python
connection = sqlite3.connect("contacts.db")
```

The connection remains open while the application runs and is safely closed using:

```python
finally:
    connection.close()
```

This ensures database resources are released properly, even if an unexpected error occurs.

---

# How To Run

SQLite is included with Python, so no additional database installation is required.

Run the application using:

```bash
python contact_manager_cli.py
```

On the first run, SQLite automatically creates:

```
contacts.db
```

---

# Example Menu

```text
================= CONTACT MANAGER CLI =================

1. Add contact
2. View contacts
3. Search contact
4. Update contact
5. Delete contact
6. Count contact
7. Count contacts by city
0. Exit
```

---

# Project Structure

```text
contact-manager-cli/
│
├── contact_manager_cli.py
├── contacts.db
└── README.md
```

---

# Topics Covered

* Python
* SQLite
* Relational Databases
* SQL
* CRUD Operations
* `sqlite3`
* Database Connections
* SQL Cursors
* Transactions
* Context Managers
* Parameterized Queries
* Primary Keys
* AUTOINCREMENT
* Aggregate Functions
* SQL Sorting
* SQL Filtering
* `LIKE`
* `COUNT`
* `GROUP BY`
* `ORDER BY`
* Database Persistence
* Command-Line Interfaces (CLI)

---

# Key Concepts Demonstrated

This project demonstrates how Python applications interact with relational databases to store and manage persistent data.

It covers the complete lifecycle of database programming:

```text
Connect
    ↓
Create Table
    ↓
Insert Records
    ↓
Query Records
    ↓
Update Records
    ↓
Delete Records
    ↓
Analyze Data
    ↓
Close Connection
```

It also introduces several SQL concepts beyond basic CRUD operations, including:

* Sorting records with `ORDER BY`
* Partial searches using `LIKE`
* Counting records with `COUNT()`
* Grouping data with `GROUP BY`
* Retrieving automatically generated IDs with `lastrowid`
* Managing transactions with context managers
* Safely passing user input through parameterized SQL queries

Overall, this project provides practical experience building a complete **database-driven command-line application** while demonstrating how Python and SQLite work together to create persistent, queryable, and structured data applications.

---

# Future Improvements

* Validate email addresses and phone number formats before saving.
* Prevent duplicate contacts based on email or phone number.
* Search by phone number, email, or city in addition to name.
* Add pagination when displaying large numbers of contacts.
* Export contacts to CSV or JSON.
* Import contacts from CSV files.
* Add advanced filtering (e.g., contacts from a specific city).
* Support deleting or updating multiple contacts at once.
* Add timestamps for contact creation and last modification.
* Build a graphical user interface (GUI) using Tkinter or PyQt.
* Migrate to a full-featured database system such as PostgreSQL or MySQL for larger datasets.
