#display the nummber is palindrome or not
def display(palin):
   if palin==True:
      print("The number is palindrome")
   else:
      print("The number is not a palindrome")
      
#input by the user
def get_input():
   n=int(input("enter the number: "))
   return n

#checking whether the number is palindrome or not
def palindrome(n):
   temp=n
   rev=0
   while(n>0):
      dig=n%10
      rev=rev*10+dig
      n=n//10
   if(temp==rev):
      return True
   else:
      return False

#main function  
def main():
   n=get_input()
   palin=palindrome(n)
   display(palin)
   
main()
      