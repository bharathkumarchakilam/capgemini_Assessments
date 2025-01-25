#displays the factorial of the number
def display(result,number):
   print(f"The factorial of the {number} is: {result}")

#input by the user
def get_input():
   number=int(input("enter the number: "))
   return number

#calculating the factorial of the number
def factorial_calculator(number):
   result=1
   for i in range(1,number+1):
      result=result*i;
   return result

#main function
def main():
   number=get_input()
   while(number<0):
      print("please enter a positive number")
      number=get_input()
   result=factorial_calculator(number)
   display(result,number)
   
main()