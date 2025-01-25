# display the balance
def display(result):
    print(result)

#check the balance
def check_balance(balance):
    display(f"your balance is: {balance}")

#deposit of the amount
def deposit(balance,amount):
    balance += amount
    display(f"Deposited {amount}. now your balance is: {balance}")
    return balance

#withdraw of the amount
def withdraw(balance,amount):
    if amount>balance:
        display("****insuffient balance****")
    else:
        balance -= amount
        display(f"withdrawn amount is {amount}. now your balance is: {balance}")
        return balance

#operations of the ATM
def atm():
    display("welcome to ATM")
    balance = 0
    while True:
        print()
        display("1.check balance")
        display("2.deposit")
        display("3.withdrawn")
        display("4.exit")
        choice=int(input("enter choice:"))
        if choice==1:
            check_balance(balance)
        elif choice==2:
            amount=float(input("enter amount for deposit:"))
            balance=deposit(balance,amount)
        elif choice==3:
            amount=float(input("enter amount for withdrawn:"))
            balance=withdraw(balance,amount)
        elif choice==4:
            break;
        else:
            display("choose valid option")

#main function
def main():
    atm()
    
main()
        
        