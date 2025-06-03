import sqlite3
import csv
import DBModule as db 

db.initDB()

with open('subject_gpa.csv', newline='') as csvfile:
    gpaRaw = csv.DictReader(csvfile)
    for row in gpaRaw:
        db.addGPA(row.get("StudentID"), row.get("English/ENL Avg"), row.get("Mathematics Avg"), row.get("Science Avg"),
        row.get("Social Studies Avg"), row.get("Foreign Language Avg"), row.get("Arts Avg"))


with open('ap_preferences.csv', newline='') as csvfile:
    #fieldnames = ["student_id","rule_id","rule_name","courses_1","courses_2","courses_3","courses_4"]
    studentPref = csv.DictReader(csvfile)

print(db.viewTable())