# Bank Loan Eligibility
#    - Develop a program to check loan eligibility:
#      - Input: Salary, age, and credit score.
#      - Output: Loan approval or rejection with reasons.

def display(loan):
    if(loan==True):
        print("Loan is approved")
    else:
        print("Loan is rejected")
        
def get_input():
    salary=int(input("Enter the salary: "))
    age=int(input("Enter the age: "))
    credit_score=int(input("Enter the credit score: "))
    return salary,age,credit_score

def check_loan_eligibility(salary,age,credit_score):
    if salary>=50000 and age>=21 and credit_score>=700:
        return True
    else:
        return False    
    
def main(): 
    salary,age,credit_score=get_input()
    loan=check_loan_eligibility(salary,age,credit_score)
    display(loan)
    
main()