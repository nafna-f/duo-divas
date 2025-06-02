# Modules

import DBModule as db
import random
import os

# For Developer Reference:
# GPA: id, eng, math, science, ss, fLang, artMusic
# courseRank: id, ruleID, ruleName, oneID, twoID, threeID, fourID
# studentAP: id, courseID, status
# ApCourses: id, name, totalSeats, seatsTaken, seatsRemaining

# Check if studentData.db already exists, delete if so.
if os.path.exists("studentData.db"):
    print("studentData.db already exists, deleting now...")
    db.delFile()
    print("studentData.db deleted.")

# Create necessary tables
db.initDB()

# Populate tables w/ random data {TESTING, W.I.P}
for x in range(10):
    db.addGPA(random.randint(0, 10000), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))
    db.addCourseRank(random.randint(0, 10000), random.randint(0, 10), "RULENAME", "COURSEONE", "COURSETWO", "COURSETHREE", "COURSEFOUR")
    db.addStudentAP(random.randint(0, 10000), "COURSENAME", random.choice(["TRUE", "FALSE"]))
    testSeatsTotal = random.randint(20, 30)
    testSeatsTaken = testSeatsTotal - random.randint(0, testSeatsTotal)
    testSeatsRemaining = testSeatsTotal - testSeatsTaken
    print("Table Populated")

db.addApCourses("COURSEID", "COURSENAME", testSeatsTotal, testSeatsTaken, testSeatsRemaining)
print("apCourses Populated")
db.viewTable()
