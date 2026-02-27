marks = [75, 60, 85, 90, 45, 67, 80, 92]

def totalstudents(marks):
    return len(marks)

def avgmarks(marks):
    return sum(marks)/len(marks)
    
def passedstudents(marks):
    count = 0      
    for i in marks:
        if i >= 50:
            count += 1
    return count
    
def failedstudents(marks):
    count = 0
    for i in marks:
        if i < 50:
            count += 1
    return count

    
print("Total Students:", totalstudents(marks))
print("Average Marks:", avgmarks(marks))
print("Students Passed:", passedstudents(marks))
print("Students Failed:", failedstudents(marks))