#!/usr/bin/python3
import mysql.connector
import random
import string
import datetime

# Connect to mysql
conn = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password"
)

# Get a database cursor object that allows us to interact with the database from the above connection
cursor = conn.cursor()

# Create database if it doesn't exist
cursor.execute("CREATE DATABASE IF NOT EXISTS skillbridge_db")
cursor.execute("USE skillbridge_db")

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
    id VARCHAR(10) PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    pay DECIMAL(10,2),
    contact VARCHAR(255),
    location VARCHAR(255),
    category VARCHAR(50),
    job_date DATETIME
)''')
conn.commit()

# List of different job categories
CATEGORIES = [
    "Writing", "Programming", "Design", "Marketing", "Consulting",
    "Photography", "Music", "Teaching", "Handyman", "Other"
]

# Function posts a job and saves it into the SkillBridge database
def post_job():
    # Validate title input 
    while True:
        try:
            title = str(input("Job title: ")).strip()
            if len(title) == 0:
                print("Please enter a job title.")
            else:
                break 
            except ValueError:
                print("Invalid input. Please enter valid text title.")
    # Validate description input 
    while True:
        try:
            description = str(input("Description: ")).strip()
            if len(description) == 0:
                print("Please enter a job description.")
            else:
                break
            except ValueError:
                print("Invalid input. Please enter a valid text validation.")
    # Validate pay input
    while True:
        try:
            pay = input("Pay in USD: ").strip()
            pay = float(pay)
            if pay < 0:
                print("Pay cannot be negative.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # Validate contact input
    while True:
        try:
            contact = str(input("Contact info: ")).strip()
            if len(contact) == 0:
                print("Please enter a contact.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid contact. Email or Phone.")
    # Validate location
    while True:
        try:
            location = str(input("Location: ")).strip()
            if len(contact) == 0:
                print("Please enter a job location.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid text location.")
    # Get validated category input
    category = get_valid_category()

    # Validate job date input
    while True:
        job_date = input("Enter job date and time (YYYY-MM-DD HH:MM): ").strip()
        try:
            job_date = datetime.datetime.strptime(job_date, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid date format. Please enter in YYYY-MM-DD HH:MM format.")

    job_id = generate_job_id()
    cursor.execute("INSERT INTO jobs VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                   (job_id, title, description, pay, contact, location, category, job_date))
    conn.commit()
    print(f"Job posted! Save this job ID for management: {job_id}")

# Main execution unit
def main():
    while True:
        print("\nSkillBridge - Job Marketplace")
        print("1. Post a Job")
        print("2. Browse Jobs")
        print("3. Manage Jobs")
        print("4. Exit")
        choice = input("Choice: ")

        if choice == "1":
            post_job()
        elif choice == "2":
            browse_jobs()
        elif choice == "3":
            manage_jobs()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
    cursor.close()
    conn.close()
