#  Leap Year Checker
#    - Write a program to check if a given year is a leap year.
#    - Allow the user to check multiple years.

def display(result):
    print(result)
    
def get_input():
    year=int(input("enter the year: "))
    return year

def leap_year(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def main():
    year=get_input()
    result=leap_year(year)
    if(result==True):
        display(f"The year {year} is a leap year")
    else:
        display(f"The year {year} is not a leap year")
        
main()