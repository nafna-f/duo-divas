# Modules

import DBModule as db
import functions as func
import random
import os
import csv

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

# Read and place data into sqlite tables accordingly for subject_gpa.csv
with open('subject_gpa.csv', newline='') as csvfile:
    gpaRaw = csv.DictReader(csvfile)
    for row in gpaRaw:
        db.addGPA(row.get("StudentID"), row.get("English/ENL Avg"), row.get("Mathematics Avg"), row.get("Science Avg"),
                  row.get("Social Studies Avg"), row.get("Foreign Language Avg"), row.get("Arts Avg"))

with open('ap_courses.csv', newline = '') as csvfile:
    courses = csv.DictReader(csvfile)
    for row in courses:
        db.addApCourses(row.get("Course Code"), row.get("Course Name"), row.get("Number of Seats"),
                        0, row.get("Number of Seats"))

with open('ap_preferences.csv', newline='') as csvfile:
    studentPref = csv.DictReader(csvfile)
    courseKeys = ["courses_1", "courses_2", "courses_3", "courses_4"]
    studentPref = list(studentPref)
    print(len(studentPref))
    for x in range(50):
        row = studentPref[x]
        apsPicked = [row.get(i) for i in courseKeys]
        #print(apsPicked)
        db.addCourseRank(row.get("student_id"), row.get("rule_id"), row.get("rule_name"),
                        apsPicked[0], apsPicked[1], apsPicked[2], apsPicked[3])
        for course in apsPicked:
            if course != "":
                db.addStudentAP(row.get("student_id"), course, "Not Determined Yet")

    '''
    for row in studentPref:
        apsPicked = [row.get(i) for i in courseKeys]
        #print(apsPicked)
        db.addCourseRank(row.get("student_id"), row.get("rule_id"), row.get("rule_name"),
                        apsPicked[0], apsPicked[1], apsPicked[2], apsPicked[3])
        for course in apsPicked:
            if course != "":
                db.addStudentAP(row.get("student_id"), course, "Not Determined Yet")
'''
print(db.viewTable())
print("\n Table printed, now testing cleanStudentPrefs...")
func.cleanStudentPrefs("108945")
