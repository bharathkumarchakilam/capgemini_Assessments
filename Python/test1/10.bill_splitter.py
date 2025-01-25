#display function
def display(result):
    print(result)

#total amount
def total_amount():
    amount=int(input("enter the amount:"))
    return amount

#number of persons
def person():
    persons=int(input("enter the number of persons: "))
    return persons

#tip amount:
def tip_amount():
    tip=int(input("enter the tip amount: "))
    return tip

#spilt the amount among the persons
def spilt(amount,persons,tip):
    total_amount=amount+tip
    per_person=total_amount/persons
    display(f"amount should be paid by every person is {per_person}")
    
#main function
def main():
    amount=total_amount()
    persons=person()
    tip=tip_amount()
    spilt(amount,persons,tip)
    
main()
