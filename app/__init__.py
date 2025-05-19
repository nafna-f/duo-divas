import csv

neededGPAInfo = ["StudentID", "Attempted","Earned","English/ENL attempted","English/ENL earned",
    "Social Studies attempted","Social Studies earned","Mathematics attempted","Mathematics earned", "Science attempted",
    "Science earned", "Foreign Language attempted", "Foreign Language earned", "Career & Tech Education attempted",
    "Career & Tech Education earned,Arts attempted","Arts earned","Health/Physical Education attempted", 
    "Health/Physical Education earned","Miscellaneous/Guidance attempted", "Miscellaneous/Guidance earned"]

with open('subject_gpa.csv', newline='') as csvfile:
    gpaRaw = csv.DictReader(csvfile)
    for row in gpaRaw:
        print(row)
        


with open('ap_preferences.csv', newline='') as csvfile:
    #fieldnames = ["student_id","rule_id","rule_name","courses_1","courses_2","courses_3","courses_4"]
    studentPref = csv.DictReader(csvfile)
