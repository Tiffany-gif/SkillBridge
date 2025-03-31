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

# Creates a unique alpha numeric string that identifies each job post
def generate_job_id():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Function to get a valid category
def get_valid_category():
    while True:
        print("Select a category:")
        for i, category in enumerate(CATEGORIES, 1):
            print(f"{i}. {category}")
        try:
            choice = int(input("Enter number: "))
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            else:
                print("Invalid selection. Please enter a valid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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

   
# Function allows job postsers to manage(edit/delete) job posts
def manage_jobs():
    job_id = input("Enter your job ID: ")
    cursor.execute("SELECT * FROM jobs WHERE id = %s", (job_id,))
    job = cursor.fetchone()
    
    if not job:
        print("Job not found!")
        return
    
    action = input("Edit or Delete? (e/d): ").strip().lower()
    if action == "e":
        # Validate title input
        while True:
            try:
                title = str(input(f"New title ({job[1]}): ")).strip() or job[1]
                if len(title) == 0:
                    print("Please enter a job title.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid text title.")
        # Validate description input
        while True:
            try:
                description = str(input(f"New description ({job[2]}): ").strip() or job[2])
                if len(description) == 0:
                    print("Please enter a job description.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid text description.")
        # Validate pay input
        while True:
            try:
                pay = input(f"New pay ({job[3]}) USD: ").strip() or job[3]
                pay = float(pay)
                if pay < 0:
                    print("Pay cannot be negative.")
                else:
                    break
            except ValueError:
                print("Invalid input. Enter a valid number.")
        
        # Validate contact input
        while True:
            try:
                contact = str(input(f"New contact ({job[4]}): ")).strip() or job[4]
                if len(contact) == 0:
                    print("Please enter a contact. Email or Phone.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid contact. Email or Phone")
        
        # Validate location input
        while True:
            try:
                location = str(input(f"New location ({job[5]}): ")).strip() or job[5]
                if len(location) == 0:
                    print("Please enter a job location.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid text location.")
        
        # Validate job date input
        while True:
            job_date = str(input(f"New job date ({job[7]}): ")).strip() or job[7].strftime('%Y-%m-%d %H:%M')
            try:
                job_date = datetime.datetime.strptime(job_date, "%Y-%m-%d %H:%M")
                break
            except ValueError:
                print("Invalid date format. Please enter in YYYY-MM-DD HH:MM format.")
        
        cursor.execute("UPDATE jobs SET title=%s, description=%s, pay=%s, contact=%s, location=%s, job_date=%s WHERE id=%s",
                       (title, description, pay, contact, location, job_date, job_id))
        conn.commit()
        print("Job updated!")
    elif action == "d":
        cursor.execute("DELETE FROM jobs WHERE id = %s", (job_id,))
        conn.commit()
        print("Job deleted!")
    else:
        print("Invalid choice.") 

# Function allows job seekers to browse for jobs


def browse_jobs():
    # Get validated category
    category = get_valid_category()
    # Fetch All jobs in specified category
    cursor.execute("SELECT title, description, pay, contact, location, job_date FROM jobs WHERE category = %s", (category,))
    jobs = cursor.fetchall()
    if jobs:
        for job in jobs:
            print(f"\nTitle: {job[0]}\nDescription: {job[1]}\nPay: ${job[2]}\nContact: {job[3]}\nLocation: {job[4]}\nDate: {job[5]}")
    else:
        print("No jobs found.")

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
