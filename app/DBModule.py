import sqlite

dbFile = "studentData"

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
              artMusicGPA DOUBLE,
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
              FOREIGN KEY(studentID) REFERENCES students(studentID)
              '''
          )
    c.execute('''
              CREATE TABLE IF NOT EXISTS studentAP(
              studentID INTEGER
              courseID TEXT
              status TEXT
              FOREIGN KEY(studentID) REFERENCES students(studentID)
              '''
              )
    c.execute('''
              CREATE TABLE IF NOT EXISTS apCourses(
              courseID TEXT PRIMARY KEY,
              courseName TEXT,
              totalSeats INTEGER,
              seatsTaken INTEGER,
              seatsRemaining INTEGER,
              '''
              )
              
    db.commit()
    db.close()

def addGPA(id, eng, math, science, ss, foreignLang, artMusic):
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("INSERT INTO students(studentID, englishGPA, mathGPA, scienceGPA, socialStudiesGPA, foreignLangGPA, artMusicGPA) VALUES (?, ?, ?, ?, ?, ?)", (id, eng, math, science, ss, artMusic))
    db.commit()
    db.close()

def addCourseRank(id, ruleID, ruleName, oneID, twoID, threeID, fourID):
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("INSERT INTO courseRanking(studentID, ruleID, ruleName, courseOneID, courseTwoID, courseThreeID, courseFourID) VALUES (?, ?, ?, ?, ?, ?, ?)", (id, ruleID, ruleName, oneID, twoID, threeID, fourID))
    db.commit()
    db.close()

def addStudentAP(id, courseID, status):
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("INSERT INTO studentAP(studentID, courseID, status) VALUES (?, ?, ?)", (id, courseID, status))
    db.commit()
    db.close()

def addApCourses(id, name, totalSeats, seatsTaken, seatsRemaining):
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute("INSERT INTO apCourses(courseID, courseName, totalSeats, seatsTaken, seatsRemaining) VALUES (?, ?, ?, ?, ?)", (id, name, totalSeats, seatsTaken, seatsRemaining))
    db.commit()
    db.close()