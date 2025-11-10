# Student Management Application

Name: Gurjas Chalana
Student Number: 101234914

This is a minimal Python app that connects to a PostgreSQL database to manage students. It performs basic CRUD operations: list, add, update, and delete students.

Project Files
-------------
- db_setup.sql — SQL script to create the database and populate initial data.
- app.py — Python script with CRUD functions and test cases.
- README.md — This file.

Setup
-----
1. Install PostgreSQL  
   Download from https://www.postgresql.org/download/.

2. Install Python  
   Download Python 3 from https://www.python.org/downloads/.

3. Install required library  
   Open a terminal and run:
    pip install psycopg2-binary

Database Setup
--------------
1. Open the PostgreSQL shell:
    psql -U your_username

2. Run the setup script:    
    \i 'project_path'/db_setup.sql'

3. Check the table:
    SELECT * FROM students;

Run the App
-----------
1. Update the connection in app.py, by replacing your_username and your_password with your PostgreSQL credentials:
```python
conn = psycopg2.connect("dbname=student_db user=your_username password=your_password")

Video Demonstration
-------------------
URL = https://youtu.be/_SXVCaq2dgM
