#displays the pattern of stars
def display_pattern(n,choice):
    if choice==0:
        for i in range(1,n+1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()
    else:
        for i in range(n,0,-1):
            for j in range(1,i+1):
                print("*",end=" ")
            print()

#input by the user
def get_input():
    n=int(input("enter the number: "))
    return n

#main function
def main():
    n=get_input()
    print("Enter '0' for increasing pattern")
    print("Enter '1' for decreasing pattern")
    choice=int(input("Enter choice: "))
    display_pattern(n,choice)

main()