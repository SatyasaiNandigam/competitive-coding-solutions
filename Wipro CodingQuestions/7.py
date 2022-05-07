no_of_persons = int(input("Enter number of persons: "))
student_marks ={}
for i in range(no_of_persons):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
queury_name = input("Enter the name of the student: ")
average= 0
for i in student_marks[queury_name]:
    average +=i
average = average/3
print("%.2f"%average)


    
