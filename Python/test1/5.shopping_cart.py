#displays the cart items
def display(cart):
    print("Items in the cart:")
    for i in cart:
        print(i)

#adding the item to the cart       
def add_item(cart):
    item=input("Enter the item name: ")
    price=int(input("Enter the price: "))
    cart.append((item,price))

#calculating the total price of items in the cart  
def total_price(cart):
    total=0
    for i in cart:
        total+=i[1]
    return total

#main function
def main():
    cart=[]
    while True:
        print()
        print("1. Add item")
        print("2. View cart items")
        print("3. Calculate total price")
        print("4. Exit")
        choice=int(input("Enter your choice: "))
        if choice==1:
            add_item(cart)
        elif choice==2:
            display(cart)
        elif choice==3:
            total=total_price(cart)
            print("Total price:",total)
        else:
            break

main()