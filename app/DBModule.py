import sqlite

dbFile = "studentData"

def initDB():
    db = sqlite3.connect(dbFile)
    c = db.cursor()

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
    db.close()
