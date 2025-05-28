# Testing with populated data since currently, we don't have the right files.

import DBModule as db
import random

# populate the db

# GPA: id, eng, math, science, ss, artMusic
# courseRank: id, ruleID, ruleName, oneID, twoID, threeID, fourID
# studentAP: id, courseID, status
# ApCourses: id, name, totalSeats, seatsTaken, seatsRemaining

db.initDB()

for x in range(10):
    db.addGPA(random.randint(0, 10000), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0), random.uniform(0.0, 100.0))
    db.addCourseRank(random.randint(0, 10000), random.randint(0, 10), "RULENAME", "COURSEONE", "COURSETWO", "COURSETHREE", "COURSEFOUR")
    db.addStudentAP(random.randint(0, 10000), "COURSENAME", random.choice(["TRUE", "FALSE"]))
    testSeatsTotal = random.randInt(20, 30)
    testSeatsTaken = testSeatsTotal - random.randInt(0, testSeatsTotal)
    testSeatsRemaining = testSeatsTotal - testSeatsTaken
    db.addApCourses("COURSEID", "COURSENAME", testSeatsTotal, testSeatsTaken, testSeatsRemaining)
