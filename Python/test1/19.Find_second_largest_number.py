#display the result
def display(result):
    print(result)

#elements in the list
def numbers():
    n=int(input("enter the number of elements: "))
    lst=[]
    for i in range(n):
        element=int(input("enter the element: "))
        lst.append(element)
    display(f"elements in the list are: {lst}")
    return lst

#finding the second largest number in the list
def second_largest(lst):
    lst.sort()
    display(f"second largest number in the list is: {lst[-2]}")

#main function
def main():
    lst=numbers()
    second_largest(lst)
    
main()