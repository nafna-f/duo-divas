import sqlite3

dbFile = "studentData"
db = sqlite3.connect(dbFile)
c = db.cursor()

def initDB():
    #db = sqlite3.connect(dbFile)
    #c = db.cursor()

    c.execute('''
              CREATE TABLE IF NOT EXISTS students (
              studentID INTEGER
              englishGPA DOUBLE
              mathGPA DOUBLE
              scienceGPA DOUBLE
              socialStudiesGPA DOUBLE
              artMusicGPA DOUBLE
              PRIMARY KEY(studentID)
              '''
              )
    c.execute('''
              CREATE TABLE IF NOT EXISTS courseRanking (
              studentID INTEGER
              ruleID INTEGER
              ruleName TEXT
              courseOneID TEXT
              courseTwoID TEXT
              courseThreeID TEXT
              courseFourID TEXT
              FOREIGN KEY(studentID)
              '''
          )
    c.execute('''
              CREATE TABLE IF NOT EXISTS studentAP(
              studentID INTEGER
              courseID TEXT
              status TEXT
              FOREIGN KEY(studentID)
              '''
              )
    c.execute('''
              CREATE TABLE IF NOT EXISTS apCourses(
              courseID TEXT
              courseName TEXT
              totalSeats INTEGER
              seatsTaken INTEGER
              seatsRemaining INTEGER
              PRIMARY KEY(courseID)
              '''
              )

    db.commit()
    # db.close()

def addGPA(id, eng, math, science, ss, artMusic):
    c.execute("INSERT INTO students(studentID, englishGPA, mathGPA, scienceGPA, socialStudiesGPA, artMusicGPA) VALUES (?, ?, ?, ?, ?, ?)", (id, eng, math, science, ss, artMusic))
    db.commit()

def addCourseRank(id, ruleID, ruleName, oneID, twoID, threeID, fourID):
    c.execute("INSERT INTO courseRanking(studentID, ruleID, ruleName, courseOneID, courseTwoID, courseThreeID, courseFourID) VALUES (?, ?, ?, ?, ?, ?, ?)", (id, ruleID, ruleName, oneID, twoID, threeID, fourID))
    db.commit()

def addStudentAP(id, courseID, status):
    c.execute("INSERT INTO studentAP(studentID, courseID, status) VALUES (?, ?, ?)", (id, courseID, status))
    db.commit()

def addApCourses(id, name, totalSeats, seatsTaken, seatsRemaining):
    c.execute("INSERT INTO apCourses(courseID, courseName, totalSeats, seatsTaken, seatsRemaining) VALUES (?, ?, ?, ?, ?)", (id, name, totalSeats, seatsTaken, seatsRemaining))
    db.commit()
