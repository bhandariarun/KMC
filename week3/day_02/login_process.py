import sqlite3
import re
import hashlib

# Connect to the SQLite database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create user registration table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS register_user
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, email TEXT, password TEXT)''')
conn.commit()

# Create user login table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS login_user
             (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE,password TEXT, logged_in INTEGER DEFAULT 0)''')
conn.commit()

# Custom Exceptions
class UsernameExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass

class UserNotLoggedInError(Exception):
    pass

class UserAlreadyLoggedInError(Exception):
    pass

# Function to register a new user
def register_user(username, email, password):
    # Check if the username already exists
    c.execute("SELECT * FROM register_user WHERE username=?", (username,))
    if c.fetchone():
        raise UsernameExistsError("Username is already taken")

    # Validate email format
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("Invalid email format")

    # Hash the password securely
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Insert user into the registration table
    c.execute("INSERT INTO register_user (username, email, password) VALUES (?, ?, ?)", (username, email, hashed_password))
    c.execute("INSERT INTO login_user (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

    print("Registration successfull")


def login_user(username, password):
    # Check if the user is already logged in
    c.execute("SELECT * FROM login_user WHERE username=? AND logged_in=1", (username,))
    if c.fetchone():
        raise UserAlreadyLoggedInError("User is already logged in")

    # Verify the entered username and password against the stored information in the login_user table
    c.execute("SELECT * FROM login_user WHERE username=?", (username,))
    login_user_data = c.fetchone()

    if not login_user_data:
        raise InvalidCredentialsError("Invalid username")

    # Verify the password
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password != login_user_data[2]:
        raise InvalidCredentialsError("Invalid password")

    # Mark the user as logged in
    c.execute("UPDATE login_user SET logged_in=1 WHERE username=?", (username,))
    conn.commit()
    print("Login successful")




# Function to update password
# def update_password(username, old_password, new_password):
#     # Check if the user is logged in
#     c.execute("SELECT * FROM login_user WHERE username=? AND logged_in=1", (username,))
#     if not c.fetchone():
#         raise UserNotLoggedInError("User must be logged in to update password")

#     c.execute("SELECT * FROM register_user WHERE username=?", (username,))
#     user = c.fetchone()
#     hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
#     if hashed_old_password != user[2]:
#         raise InvalidCredentialsError("Invalid old password")

#     # Update password
#     hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()
#     c.execute("UPDATE register_user SET password=? WHERE username=?", (hashed_new_password, username))
#     conn.commit()
#     print("Password updated successfully")


def update_password(username, old_password, new_password):
    # Check if the user is logged in
    c.execute("SELECT * FROM login_user WHERE username=? AND logged_in=1", (username,))
    if not c.fetchone():
        raise UserNotLoggedInError("User must be logged in to update password")

    # Verify the old password
    c.execute("SELECT * FROM login_user WHERE username=?", (username,))
    login_user_data = c.fetchone()
    hashed_old_password = hashlib.sha256(old_password.encode()).hexdigest()
    if hashed_old_password != login_user_data[2]:
        raise InvalidCredentialsError("Invalid old password")

    # Hash the new password securely
    hashed_new_password = hashlib.sha256(new_password.encode()).hexdigest()

    # Update the password
    c.execute("UPDATE login_user SET password=? WHERE username=?", (hashed_new_password, username))
    conn.commit()
    print("Password updated successfully")




# Function to delete account
def delete_account(username, password):
    # Check if the user is logged in
    c.execute("SELECT * FROM login_user WHERE username=? AND logged_in=1", (username,))
    if not c.fetchone():
        raise UserNotLoggedInError("User must be logged in to delete account")

    # Verify password
    c.execute("SELECT * FROM login_user WHERE username=?", (username,))
    login_user_data = c.fetchone()
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password != login_user_data[2]:
        raise InvalidCredentialsError("Invalid password")

    # Delete user's information from both tables
    c.execute("DELETE FROM register_user WHERE username=?", (username,))
    c.execute("DELETE FROM login_user WHERE username=?", (username,))
    conn.commit()
    print("Account deleted successfully")


# Main function
def main():
    while True:
        print("\nWelcome to the User Authentication and Management System!")
        print("1. Register")
        print("2. Login")
        print("3. Update password")
        print("4. Delete account")

        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                username = input("Enter username: ")
                email = input("Enter email: ")
                password = input("Enter password: ")

                register_user(username, email, password)
            except (UsernameExistsError, ValueError) as e:
                print("Error:", e)

        elif choice == '2':
            try:

                username = input("Enter username: ")
                password = input("Enter password: ")

                login_user(username, password)
            except (InvalidCredentialsError, UserAlreadyLoggedInError) as e:
                print("Error:", e)

        elif choice == '3':
            try:
                username = input("Enter a username: ")
                old_password = input("Enter a old password: ")
                new_password = input("Enter a new password: ")

                update_password(username, old_password, new_password)
            
            except(UserNotLoggedInError,InvalidCredentialsError) as e:
                print("Error:", e)

        elif choice == '4':
            try:
                username = input("Enter a username: ")
                password = input("Enter a password: ") 
                delete_account(username,password)

            except(UserNotLoggedInError, InvalidCredentialsError) as e:
                print("Error:", e)

        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
