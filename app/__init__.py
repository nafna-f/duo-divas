import sqlite3
import csv
import DBModule as db 
import functions as func
import os

if not os.path.isfile("studentData.db"):
    db.initDB()
    print("Please be patient, this process can take up to several minutes...")
    # Add the data to the database
    with open('subject_gpa.csv', newline='') as csvfile:
        print("Adding student information...")
        gpaRaw = csv.DictReader(csvfile)
        for row in gpaRaw:
            db.addGPA(row.get("StudentID"), row.get("English/ENL Avg"), row.get("Mathematics Avg"), row.get("Science Avg"),
                    row.get("Social Studies Avg"), row.get("Foreign Language Avg"), row.get("Arts Avg"))

    with open('ap_courses.csv', newline = '') as csvfile: 
        print("Adding AP course information...")
        courses = csv.DictReader(csvfile)
        for row in courses: 
            db.addApCourses(row.get("Course Code"), row.get("Course Name"), row.get("Number of Seats"), 
                            0, row.get("Number of Seats"))

    with open('ap_preferences.csv', newline='') as csvfile:
        print("Adding student AP selections...")
        studentPref = csv.DictReader(csvfile)
        courseKeys = ["courses_1", "courses_2", "courses_3", "courses_4"]
        courseExclusions = ["ZZ", "ZZNOAPPHY", "ZZNOAPBIO","ZZNOAPENG", "ZQAPENG", "ZQAPPHYSICAL", "ZQAPBIO"]
        studentPref = list(studentPref)
        #print(len(studentPref))
        for x in range(len(studentPref)):
            row = studentPref[x]
            apsPicked = [row.get(i) for i in courseKeys]
            #print(apsPicked)
            db.addCourseRank(row.get("student_id"), row.get("rule_id"), row.get("rule_name"), 
                            apsPicked[0], apsPicked[1], apsPicked[2], apsPicked[3])
            for course in apsPicked:
                if (course != "") and (course not in courseExclusions):
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
    func.removeDuplicates()

#print(func.bestComeFirst(100))
print(db.viewTable())
