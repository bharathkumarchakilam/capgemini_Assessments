#display function
def display(result):
    print(result)
    
#list of the numbers
def numbers():
    n=int(input("enter the number of elements: "))
    lst=[]
    for i in range(n):
        element=int(input("enter the element: "))
        lst.append(element)
    display(f"elements in the list are: {lst}")
    return lst

#seperating the odd and even numbers in the list
def seperate(lst):
    odd=[]
    even=[]
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    display(f"odd numbers are: {odd}")
    display(f"even numbers are: {even}")
    
#main function
def main():
    lst=numbers()
    seperate(lst)
    
main()
    