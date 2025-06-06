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
        bcfLevel(i, percentage, False)
    for i in range(1, 5):
        bcfLevel(i, percentage, True)


# Best Come First Method Helper
def bcfLevel(level, percentage, Waitlist, subCategory):
    dbFile = "studentData.db"
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    mainCategories = ["ZQAPENG", "ZQAPBIO", "ZQAPPHYSICAL", "ZQAPHG"] #you can rank three courses in these
    subCategories = ["AP MATH", "AP WORLD LANGUAGE"] #you only rank one course with these
    specialCases = ["ZQAPHEHV", "ZQAPHVT", "ZQAPMAMI", "ZQHUSHQS", "ZQAPHVHT", "MCPREC"] #these have combined courses
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
    
    if waitList:
        waitlistQ = "LIKE"
    else:
        waitlistQ = "NOT LIKE"
    
    ruleIDQ = "(ruleID = 123 OR ruleID = 133 OR ruleID = 134 OR ruleID = 135)"

    c.execute(f"SELECT DISTINCT {courseColumn} FROM courseRanking WHERE {ruleIDQ} AND {courseColumn} {waitListQ}'%WAITLIST'")
    coursesRanked = list(c.fetchall())
    coursesRanked = [ap for courses in coursesRanked for ap in courses if ap not in exclusions]
    print(coursesRanked)
        if ap not in categories and ap not in specialCases:
            #print(ap)
            ogAP = ap
            if waitList:
                ap = ap.split("_")
                ap = ap[0]
            c.execute(f"SELECT studentID FROM courseRanking WHERE {ruleIDQ} AND {courseColumn} = ?", (ap,))
            candidates = list(c.fetchall())
            candidates = [student for students in candidates for student in students]
            for student in candidates:
                if studentAPLimit(student):
                    candidates.pop(student)
            c.execute("SELECT seatsRemaining FROM apCourses WHERE courseID = ?", (ap,))
            totalSeats = c.fetchone()[0] 
            seats = round(totalSeats * (percentage/100))
            if seats >= len(candidates):
                c.execute("UPDATE apCourses SET seatsRemaining = seatsRemaining - ? WHERE courseID = ?", (len(candidates), ap))
                c.execute("UPDATE apCourses SET seatsTaken = seatsTaken + ? WHERE courseID = ?", (len(candidates), ap))
                for student in candidates:
                    c.execute("UPDATE studentAP SET status = 'Accepted' WHERE studentID = ? AND courseID = ?", (student, ogAP))
                    
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
                        c.execute("UPDATE studentAP SET status = 'Accepted' WHERE studentID = ? AND courseID = ?", (student, ogAP))
                    else:
                        if totalSeats > seats:
                            c.execute("UPDATE studentAP SET status = 'Waitlisted' WHERE studentID = ? AND courseID = ?", (student, ogAP))
                #for candidates[i]
    
    db.commit()
    db.close()

def bcfCategoryAP(category, categoryLevel, sublevel, percentage):
    dbFile = "studentData.db"
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    categoryDict = {
                  "ZQAPENG": "ruleID = 133",
                  "ZQAPBIO": "ruleID = 141",
                  "ZQAPPHYSICAL": "ruleID = 143",
                  "ZQAPHG": "ruleID = 142",
                  "": "(ruleID = 123 OR ruleID = 133 OR ruleID = 134 OR ruleID = 135)"
                }
    levelDict = {
                 1: "courseOneID",
                 2: "courseTwoID",
                 3: "courseThreeID",
                 4: "courseFourID",
                }
    ruleIDQ = categoryDict.get("")
    courseColumn = levelDict.get(categoryLevel)
    c.execute(f"SELECT studentID FROM courseRanking WHERE {ruleIDQ} AND {courseColumn} = ?", (ap,))
    candidates = list(c.fetchall())
    candidates = [student for students in candidates for student in students]
    for student in candidates:
        if studentAPLimit(student):
            candidates.remove(student)
        ruleIDQ = categoryDict.get(category)
        courseColumn = levelDict.get(sublevel)
        c.execute(f"SELECT DISTINCT {courseColumn} FROM courseRanking WHERE {ruleIDQ} AND studentID IN ({','.join('?' for student in candidates)}) NOT LIKE '%WAITLIST'", candidates)
        subLvlCourses = list(c.fetchall())
        subLvlCourses= [course for courses in subLvlCourses for student in students]
        for course in subLvlCourses:
            c.execute(f"SELECT studentID FROM courseRanking WHERE {ruleIDQ} AND courseID = {course} AND studentID IN ({','.join('?' for student in candidates)}) NOT LIKE '%WAITLIST'", candidates)
            subLvlCand = list(c.fetchall()) 
            subLvlCand = [student for students in subLvlCand for student in students]
            c.execute(f"SELECT studentID FROM courseRanking WHERE {ruleIDQ} AND {courseColumn} = ?", (ap,))
            candidates = list(c.fetchall())
            candidates = [student for students in candidates for student in students]
            for student in candidates:
                if studentAPLimit(student):
                    candidates.pop(student)
            c.execute("SELECT seatsRemaining FROM apCourses WHERE courseID = ?", (ap,))
            totalSeats = c.fetchone()[0] 
            seats = round(totalSeats * (percentage/100))
            if seats >= len(candidates):
                c.execute("UPDATE apCourses SET seatsRemaining = seatsRemaining - ? WHERE courseID = ?", (len(candidates), ap))
                c.execute("UPDATE apCourses SET seatsTaken = seatsTaken + ? WHERE courseID = ?", (len(candidates), ap))
                for student in candidates:
                    c.execute("UPDATE studentAP SET status = 'Accepted' WHERE studentID = ? AND courseID = ?", (student, ogAP))
                    
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
                        c.execute("UPDATE studentAP SET status = 'Accepted' WHERE studentID = ? AND courseID = ?", (student, ogAP))
                    else:
                        if totalSeats > seats:
                            c.execute("UPDATE studentAP SET status = 'Waitlisted' WHERE studentID = ? AND courseID = ?", (student, ogAP))
                #for candidates[i]
            c.execute()
            

def studentAPLimit(studentID):
    dbFile = "studentData.db"
    db = sqlite3.connect(dbFile)
    c = db.cursor()
    numAPdict = {
                 123: 4,
                 133: 1
                 134: 2
                 135: 3
                }
    c.execute("SELECT ruleID FROM courseRanking WHERE (ruleID = 123 OR ruleID = 133 OR ruleID = 134 OR ruleID = 135) AND studentID = ?", (studentID,))
    studentRule = c.fetchone()[0]
    studentRule = numAPdict.get(studentRule)
    c.execute("SELECT COUNT(*) FROM studentAP WHERE studentID = ?", (studentID,))
    numAps = c.fetchone()[0]
    return studentRule <= numAps



    