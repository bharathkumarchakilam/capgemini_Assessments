#display the result
def display(result):
    print(result)

#number for multiplication table
def number():
    n=int(input("enter the number: "))
    return n

#range of the table
def table_range():
    r=int(input("enter the range of the table: "))
    return r

#multiplucation table of the number
def table(number,ran):
    for i in range(1,ran+1):
        res=number*i
        display(f"{number} * {i} = {res}")
        
#main function
def main():
    num=number()
    ran=table_range()
    table(num,ran)
    
main()
