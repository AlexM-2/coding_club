a = 4
b = 7
c = 2
d = 4

def getPercentage(mark, maxMarks):
    return mark * 100 / maxMarks # 100/maxMarks gets the amount mark needs to be multiplied by to get a percentage

def getGrade(percentage):
    if percentage < 60:
        return "F"
    elif percentage < 70:
        return "D"
    elif percentage < 80:
        return "C"
    elif percentage < 90:
        return "B"
    else:
        return "A"

maxMarks = 10
studentsMarks = {
    "Jeremy": a,
    "Alex": b,
    "James": c,
    "Oliver": d
}
studentsPercentages = {
    "Jeremy": getPercentage(a, maxMarks),
    "Alex": getPercentage(b, maxMarks),
    "James": getPercentage(c, maxMarks),
    "Oliver": getPercentage(d, maxMarks)
}
studentsGrades = {
    "Jeremy": getGrade(studentsPercentages["Jeremy"]),
    "Alex": getGrade(studentsPercentages["Alex"]),
    "James": getGrade(studentsPercentages["James"]),
    "Oliver": getGrade(studentsPercentages["Oliver"])
}

for person, grade in studentsGrades.items():
    print(f"{person} got {grade}.")