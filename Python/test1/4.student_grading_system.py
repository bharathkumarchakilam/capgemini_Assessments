#Displays the details of the student
def display(total,percentage,grade):
    print("Total marks:",total)
    print("Percentage:",percentage)
    print("Grade:",grade)

#input by the user   
def get_input():
    name=input("Enter the student name: ")
    marks=[]
    for i in range(5):
        m=int(input("Enter the marks for subject "+str(i+1)+": "))
        marks.append(m)
    return name,marks

#calculating the total marks, percentage and grade of the student
def calculate_grade(marks):
    total=sum(marks)
    percentage=total/5
    if percentage>=90:
        grade='A'
    elif percentage>=80:
        grade='B'
    elif percentage>=70:
        grade='C'
    else:
        grade='Fail'
    return total,percentage,grade

#main function  
def main():
    name,marks=get_input()
    total,percentage,grade=calculate_grade(marks)
    display(total,percentage,grade)
    
main()