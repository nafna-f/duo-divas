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

# Read and place data into sqlite tables accordingly for ap_preferences.csv
with open('ap_preferences.csv', newline='') as csvfile:
    #fieldnames = ["student_id","rule_id","rule_name","courses_1","courses_2","courses_3","courses_4"]
    studentPref = csv.DictReader(csvfile)

# Print the table for viewer readability
db.viewTable()
