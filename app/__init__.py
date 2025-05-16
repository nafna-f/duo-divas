# AP Program Seat Selection Program
# DuoDivas, Software Development
# Nafiyu (Naf) Murtaza, Dua Baig

# Classes

class Course:
    # code: Course Code
    # name: Course Name
    # numSect: Number of Sections in this course
    # numSeat: Number of Seats for this course
    def __init__(a, code, name, numSect, numSeat):
        a.code = code
        a.name = name
        a.numSect = numSect
        a.numSeat = numSeat
    def __str__(a):
        return(f"{self.name}, Code: {self.code}, # of Sections: {self.numSect}, # of Seats: {self.numSeat}")


class Student: # (later)
