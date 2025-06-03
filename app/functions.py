# Modules

import sqlite3
import os

# DB file

dbFile = "studentData.db"
db = sqlite3.connect(dbFIle)
c = db.cursor()

# Helper Functions

# Clean the bloat from student_prefs and return a list of the student's actual preferred courses. The first parameter is how many AP courses they have selcted.
def cleanStudentPrefs(id): #look thru all lines: 
    c.execute(f"SELECT {id}")

# Best Come First

def bestComeFirst():
    print("Executing 'bestComeFirst'...")
