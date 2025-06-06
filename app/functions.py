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

#def bestComeFirst():


# Best Come First Method Helper
def bcfLevel(level, percentFill):
    dbFile = "studentData.db"
    db = sqlite3.connect(dbFile)
    categories = ["ZQAPENG", "ZQAPBIO", "ZQAPPHYSICAL"]
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
                   "S": "scienceGPA,"
                   "H": "socialStudiesGPA",
                   "F": "foreignLangGPA",
                   "A": "artMusicGPA",
                   "U": "artMusicGPA",
                  }

    c = db.cursor()

    courseColumn = levelDict.get(level)
    
    c.execute("SELECT DISTINCT " + courseColumn + " FROM courseRanking WHERE (ruleID = 123 OR ruleID = 133 OR ruleID = 134 OR ruleID = 135) AND " + courseColumn + " NOT LIKE '%WAITLIST'")
    coursesRanked = list(c.fetchall())
    coursesRanked = [ap for courses in coursesRanked for ap in courses if ap not in exclusions]

    for ap in coursesRanked:
        if ap not in categories:
            c.execute("SELECT studentID FROM courseRanking WHERE (ruleID = 123 OR ruleID = 133 OR ruleID = 134 OR ruleID = 135) AND " + courseColumn + " = " + ap)
        candidates = 


    