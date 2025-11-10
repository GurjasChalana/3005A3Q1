import psycopg2

# PSQL Connection Handling
conn = psycopg2.connect("dbname=student_db user=your_username password=your_password")
cur = conn.cursor()


#CRUD Functions
def getAllStudents():
    cur.execute("SELECT * FROM students ORDER BY student_id;")
    for row in cur.fetchall():
        print(row)

def addStudent(first_name, last_name, email, enrollment_date):
    cur.execute(
        """
        INSERT INTO students (first_name, last_name, email, enrollment_date)
        VALUES (%s, %s, %s, %s);
        """,
        (first_name, last_name, email, enrollment_date)
    )
    conn.commit()
    print(f"Added student {first_name} {last_name}")

def updateStudentEmail(student_id, new_email):
    cur.execute("UPDATE students SET email=%s WHERE student_id=%s;", (new_email, student_id))
    if cur.rowcount == 0:
        print("No student with ID", student_id)
    else:
        print("Updated email for student ID", student_id)
        conn.commit()

def deleteStudent(student_id):
    cur.execute("DELETE FROM students WHERE student_id=%s;", (student_id,))
    if cur.rowcount == 0:
        print("No student with ID", student_id)
    else:
        print("Deleted student ID", student_id)
        conn.commit()

# Test cases
if __name__ == "__main__":
    print("--- TEST 1: Get all students ---")
    getAllStudents()

    print("\n--- TEST 2: Add a student ---")
    addStudent("Tom","Wonderland","alice@example.com","2023-09-05")

    print("\n--- TEST 3: Update a student's email ---")
    updateStudentEmail(1,"john.newemail@example.com")

    print("\n--- TEST 4: Delete a student ---")
    deleteStudent(3)

    print("\n--- TEST 5: Get all students after changes ---")
    getAllStudents()

cur.close()
conn.close()
