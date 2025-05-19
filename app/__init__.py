import csv

with open('subject_gpa.csv', newline=None) as csvfile:
    fieldnames = ["StudentID", "Attempted","Earned","English/ENL attempted","English/ENL earned",
    "Social Studies attempted","Social Studies earned","Mathematics attempted","Mathematics earned", "Science attempted",
    "Science earned", "Foreign Language attempted", "Foreign Language earned", "Career & Tech Education attempted",
    "Career & Tech Education earned,Arts attempted","Arts earned","Health/Physical Education attempted", 
    "Health/Physical Education earned","Miscellaneous/Guidance attempted", "Miscellaneous/Guidance earned"]
    studentGpas = csv.DictReader(csvfile, fieldnames = fieldnames)
    for row in studentGpas:
        print(row)

with open('ap_preferences.csv', newline='') as csvfile:
    print("hi")
