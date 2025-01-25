#displaying the password is strong and weak
def display(password):
  if(password==True):
    print("Password is strong")
  else:
    print("password is weak")
  
#password input by the user
def get_input():
  password=input("Enter the password: ")
  return password

#checking whether the password is strong or weak
def check_password_strength(password):
  upper=False
  lower=False
  digit=False
  special=False
  if len(password)>=8:
        for i in password:
            if i.isupper():
              upper=True
            if i.islower():
              lower=True
            if i.isdigit():
              digit=True
            if i in ['!','@','#','$','%','^','&','*','(',')']:
              special=True
  if upper and lower and digit and special:
    return True
  else:
    return False
  
#main function  
def main():
  password=get_input()
  strength=check_password_strength(password)
  display(strength)
  
main()