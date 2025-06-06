import sqlite3
import os

# Helper Functions

#get rid of any duplicate rows in the studentAP table.
def removeDuplicates():
    dbFile = "studentData.db"
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    c.execute(f"DELETE FROM studentAP WHERE rowIndex NOT IN (SELECT MIN(rowIndex) FROM studentAP GROUP BY studentID, courseID)")
    db.commit()
    db.close()

def bestComeFirst(percentage):
    for i in range(1, 5):
        bcfLevel(i, percentage)


# Best Come First Method Helper
def bcfLevel(level, percentage):
    dbFile = "studentData.db"
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    categories = ["ZQAPENG", "ZQAPBIO", "ZQAPPHYSICAL", "ZQAPHG"]
    specialCases = ["ZQAPHEHV", "ZQAPHVT", "ZQAPMAMI", "ZQHUSHQS", "ZQAPHVHT", "MCPREC"]
    exclusions = ["", "ZZ", "ZZNOAPPHY", "ZZNOAPBIO","ZZNOAPENG"]

    levelDict = {
                 1: "courseOneID",
                 2: "courseTwoID",
                 3: "courseThreeID",
                 4: "courseFourID",
                }
    
    subjectDict = {
                   "E": "englishGPA",
                   "M": "mathGPA",
                   "S": "scienceGPA",
                   "H": "socialStudiesGPA",
                   "F": "foreignLangGPA",
                   "A": "artMusicGPA",
                   "U": "artMusicGPA",
                  }
    courseColumn = levelDict.get(level)
    #print(courseColumn)
    
    
    c.execute(f"SELECT DISTINCT {courseColumn} FROM courseRanking WHERE (ruleID = 123 OR ruleID = 133 OR ruleID = 134 OR ruleID = 135) AND {courseColumn} NOT LIKE '%WAITLIST'")
    coursesRanked = list(c.fetchall())
    coursesRanked = [ap for courses in coursesRanked for ap in courses if ap not in exclusions]
    print(coursesRanked)
    for ap in coursesRanked:
        if ap not in categories and ap not in specialCases:
            #print(ap)
            c.execute(f"SELECT studentID FROM courseRanking WHERE (ruleID = 123 OR ruleID = 133 OR ruleID = 134 OR ruleID = 135) AND {courseColumn} = ?", (ap,))
            candidates = list(c.fetchall())
            candidates = [student for students in candidates for student in students]
            c.execute("SELECT seatsRemaining FROM apCourses WHERE courseID = ?", (ap,))
            totalSeats = c.fetchone()[0] 
            seats = round(totalSeats * (percentage/100))
            if seats >= len(candidates):
                c.execute("UPDATE apCourses SET seatsRemaining = seatsRemaining - ? WHERE courseID = ?", (len(candidates), ap))
                c.execute("UPDATE apCourses SET seatsTaken = seatsTaken + ? WHERE courseID = ?", (len(candidates), ap))
                for student in candidates:
                    c.execute("UPDATE studentAP SET status = 'Accepted' WHERE studentID = ? AND courseID = ?", (student, ap))
                    
            else:
                subject = subjectDict.get(ap[:1])
                acceptedStudents = []
                for i in range(len(candidates)):
                    c.execute(f"SELECT studentID, {subject} FROM students WHERE studentID = ?", (candidates[i],))
                    studentGPAs = c.fetchone()
                    acceptedStudents.append(studentGPAs)
                acceptedStudents = sorted(acceptedStudents, key=lambda x: x[1], reverse=True)
                acceptedStudents = acceptedStudents[:seats]
                for i in range(len(acceptedStudents)):
                    acceptedStudents[i] = acceptedStudents[i][0]
                c.execute("UPDATE apCourses SET seatsRemaining = seatsRemaining - ? WHERE courseID = ?", (len(acceptedStudents), ap))
                c.execute("UPDATE apCourses SET seatsTaken = seatsTaken + ? WHERE courseID = ?", (len(acceptedStudents), ap))
                for student in candidates:
                    if student in acceptedStudents:
                        c.execute("UPDATE studentAP SET status = 'Accepted' WHERE studentID = ? AND courseID = ?", (student, ap))
                    else:
                        if totalSeats > seats:
                            c.execute("UPDATE studentAP SET status = 'Waitlisted' WHERE studentID = ? AND courseID = ?", (student, ap))
                #for candidates[i]
    db.commit()
    db.close()


    