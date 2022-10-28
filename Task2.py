




# # part 1

student_list = [
{
    "name":"hamza",
    "homeWorkMarks":[20,10],
    "quizMarks":[30,20],
    "semesterProjectMarks":90
},
{
    "name":"abdul",
    "homeWorkMarks":[20,10,30],
    "quizMarks":[30,20],
    "semesterProjectMarks":70
},
{
    "name":"Rauf",
    "homeWorkMarks":[20,30],
    "quizMarks":[30,20],
    "semesterProjectMarks":60
}
]


## part 2

def print_students(stud):
    print("Name:",stud["name"])
    print("HomeWork Marks:")
    for i in range(len(stud['homeWorkMarks'])):
        print(stud["homeWorkMarks"][i])
    print("Quiz Marks:")
    for i in range( len(stud['quizMarks'])):
        print(stud["quizMarks"][i])
    print("Semester Project Marks:",stud['semesterProjectMarks'])

## part 3
def average(myList):
    sum = 0
    for item in myList:
        sum+=item
    avg  = sum/(len(myList))
    return avg



## part 4

def get_average_of_student(stud):
    homeWorkAvg= average(stud["homeWorkMarks"])
    quizAvg = average(stud["quizMarks"])
    return (homeWorkAvg,quizAvg)



## part 5


def weighted_average(tup,proj):
    homeWorkTotalMarks=40
    quizTotalMarks = 40
    projectTotalMarks= 100
    homeWorkPercentage= 25
    quizPercentage = 40
    projectPercentage= 35
    HM_Weightage = (tup[0]/homeWorkTotalMarks)*homeWorkPercentage
    quiz_Weightage= (tup[1]/quizTotalMarks)*quizPercentage
    project_Weightage = (proj/projectTotalMarks)*projectPercentage
    return (HM_Weightage+quiz_Weightage+project_Weightage)


## part 6

def get_letter_grade(marks):
    if(marks>=80 and marks<=100):
        return 'A'
    elif(marks>=70 and marks <80):
        return 'B'
    elif (marks >=60 and marks < 70):
        return 'C'
    elif(marks >= 50 and marks < 60):
        return 'D'
    else :
        return 'F'




