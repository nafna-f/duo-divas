import csv
import json

neededGPAInfo = ["StudentID", "Class", "Attempted","Earned","English/ENL attempted","English/ENL earned",
                 "Social Studies attempted","Social Studies earned","Mathematics attempted","Mathematics earned", "Science attempted",
                 "Science earned", "Foreign Language attempted", "Foreign Language earned", "Career & Tech Education attempted",
                 "Career & Tech Education earned","Arts attempted","Arts earned","Health/Physical Education attempted",
                  "Health/Physical Education earned","Miscellaneous/Guidance attempted", "Miscellaneous/Guidance earned", "rule_id,rule_name,courses_1,courses_2,courses_3,courses_4,courses_"]

neededPrefInfo = ["student_id", "ruleID", ""]

filteredData = []

with open('subject_gpa.csv', newline='') as csvfile:
    #neededInfo = csvfile.readline().strip('\n')
    #csvfile.seek(0)
    gpaRaw = csv.DictReader(csvfile)
    for row in gpaRaw:
        data = {i: row[i] for i in neededGPAInfo}
        filteredData.append(data)
    print(filteredData)

with open('ap_preferences.csv', newline='') as csvfile:
    studentPref = csv.DictReader(csvfile)

filename = 'data.json'

with open(filename, 'w') as file:
    json.dump(filteredData, file, indent=4)
