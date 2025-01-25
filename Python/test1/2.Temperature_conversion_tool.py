#display the result
def display(result):
    print(result)
    
#conversion of celsius to fahrenheit
def celsius_to_fahrenheit(c):
    fahrenheit=(c*9/5)+32
    display(f"{c} celsius is equal to {fahrenheit} fahrenheit")
    
#conversion of fahrenheit to celsius
def fahrenheit_to_celsius(f):
    celsius=(f-32)*5/9
    display(f"{f} fahrenheit is equal to {celsius} celsius")
    
#conversion of celsius to kelvin
def celsius_to_kelvin(c):
    kelvin=c+273.15
    display(f"{c} celsius is equal to {kelvin} kelvin")

#converion of kelvin to celsius
def kelvin_to_celsius(k):
    celsius=k-273.15
    display(f"{k} kelvin is equal to {celsius} celsius")
    
#conversion of fahrenheit to kelvin
def fahrenheit_to_kelvin(f):
    kelvin=(f-32)*5/9+273.15
    display(f"{f} fahrenheit is equal to {kelvin} kelvin")
    
#conversion of kelvin to farenheit
def kelvin_to_fahrenheit(k):
    farenheit=(k-273.15)*9/5+32
    display(f"{k} kelvin is equal to {farenheit} farenheit")
    
#main function
def main():
    while True:
        display("1.celsius to fahrenheit")
        display("2.fahrenheit to celsius")
        display("3.celsius to kelvin")
        display("4.kelvin to celsius")
        display("5.fahrenhiet to kelvin")
        display("6.kelvin to fahrenheit")
        display("7.exit")
        
        choice=int(input("enter choice: "))
        if choice==1:
            celsius=float(input("enter celsius temperature: "))
            celsius_to_fahrenheit(celsius)
        elif choice==2:
            fahrenheit=float(input("enter fahrenheit temperature: "))
            fahrenheit_to_celsius(fahrenheit)
        elif choice==3:
            celsius=float(input("enter celsius temperature: "))
            celsius_to_kelvin(celsius)
        elif choice==4:
            kelvin=float(input("enter kelvin temperature: "))
            kelvin_to_celsius(kelvin)
        elif choice==5:
            fahrenheit=float(input("enter fahrenheit temperature: "))
            fahrenheit_to_kelvin(fahrenheit)
        elif choice==6:
            kelvin=float(input("enter kelvin temperature: "))
            kelvin_to_fahrenheit(kelvin)
        elif choice==7:
            break
        else:
            display("choose valid option")
            
main()
        
        
            
        