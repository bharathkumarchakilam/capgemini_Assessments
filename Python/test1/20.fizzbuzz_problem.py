#displays the result
def display(result):
    print(result)

#finding the number is divisible by (3 and 5) or 3 or 5  
def fizzbuzz():
    for i in range(1,101):
        if i%3==0 and i%5==0:
            display("FizzBuzz")
        elif i%3==0:
            display("Fizz")
        elif i%5==0:
            display("Buzz")
        else:
            display(i)

#main function()           
def main():
    fizzbuzz()
    
main()