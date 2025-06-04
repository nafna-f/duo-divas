# Modules

import sqlite3
import os

# Helper Functions

# Clean the bloat from student_prefs and return a list of the student's actual preferred courses. The first parameter is how many AP courses they have selcted.
def cleanStudentPrefs(id):
    dbFile = "studentData.db"
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute(f"SELECT * FROM courseRanking WHERE studentID = '{id}'")
    for data in c.fetchall():
        print(data)
    db.close()

# Best Come First


def bestComeFirst():
    print("Executing 'bestComeFirst'...")
