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
