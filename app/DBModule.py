# Modules
import sqlite3
import os

dbFile = "studentData.db"

# Create the tables
def initDB():
    db = sqlite3.connect(dbFile)
    c = db.cursor()

    c.execute('''
              CREATE TABLE IF NOT EXISTS students (
              studentID INTEGER PRIMARY KEY,
              englishGPA DOUBLE,
              mathGPA DOUBLE,
              scienceGPA DOUBLE,
              socialStudiesGPA DOUBLE,
              foreignLangGPA DOUBLE,
              artMusicGPA DOUBLE
              )
              '''
              )
    c.execute('''
              CREATE TABLE IF NOT EXISTS courseRanking (
              studentID INTEGER,
              ruleID INTEGER,
              ruleName TEXT,
              courseOneID TEXT,
              courseTwoID TEXT,
              courseThreeID TEXT,
              courseFourID TEXT,
              FOREIGN KEY (studentID) REFERENCES students(studentID)
              )
              '''
          )
    c.execute('''
              CREATE TABLE IF NOT EXISTS studentAP(
              studentID INTEGER,
              courseID TEXT,
              status TEXT,
              FOREIGN KEY (studentID) REFERENCES students(studentID)
              )
              '''
              )
    c.execute('''
              CREATE TABLE IF NOT EXISTS apCourses(
              courseID TEXT PRIMARY KEY,
              courseName TEXT,
              totalSeats INTEGER,
              seatsTaken INTEGER,
              seatsRemaining INTEGER
              )
              '''
              )

    db.commit()
    db.close()

# Add student gpa data
def addGPA(id, eng, math, science, ss, fLang, artMusic):
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("INSERT INTO students(studentID, englishGPA, mathGPA, scienceGPA, socialStudiesGPA, foreignLangGPA, artMusicGPA) VALUES (?, ?, ?, ?, ?, ?, ?)", (id, eng, math, science, ss, fLang, artMusic))
    db.commit()
    db.close()

# Adds course ranking data
def addCourseRank(id, ruleID, ruleName, oneID, twoID, threeID, fourID):
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("INSERT INTO courseRanking(studentID, ruleID, ruleName, courseOneID, courseTwoID, courseThreeID, courseFourID) VALUES (?, ?, ?, ?, ?, ?, ?)", (id, ruleID, ruleName, oneID, twoID, threeID, fourID))
    db.commit()
    db.close()

# Adds student AP data
def addStudentAP(id, courseID, status):
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("INSERT INTO studentAP(studentID, courseID, status) VALUES (?, ?, ?)", (id, courseID, status))
    db.commit()
    db.close()

# Adds Ap Course data
def addApCourses(id, name, totalSeats, seatsTaken, seatsRemaining): # use only once
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("INSERT INTO apCourses(courseID, courseName, totalSeats, seatsTaken, seatsRemaining) VALUES (?, ?, ?, ?, ?)", (id, name, totalSeats, seatsTaken, seatsRemaining))
    db.commit()
    db.close()

# WIP, prints the table for reader viewability
def viewTable():
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row[0] for row in c.fetchall()]
    for table in tables:
        print(f"\n{table}")
        c.execute(f"SELECT * FROM {table}")
        for row in c.fetchall():
            print(row)

    db.close()

# Deletes studentData.db for testing purposes
def delFile():
    os.remove("studentData.db")
