import csv

#planning
def studentDicts(file):
    with open(file, newline = '') as csvFile:
        student = csv.DictReader(csvFile)


studentDicts('subject_gpa.csv')
