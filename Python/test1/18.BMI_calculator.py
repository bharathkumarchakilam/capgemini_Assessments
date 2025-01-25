#display the result
def display(result):
    print(result)
    
#input of the weight
def weight_of_the_person():
    w=float(input("enter the weight in kilograms: "))
    return w

#input of the height
def height_of_the_person():
    h=float(input("enter the height in meters: "))
    return h

#calculating the BMI of the person
def BMI(weight,height):
    bmi=weight/(height*height)
    return bmi

#main function
def main():
    weight=weight_of_the_person()
    height=height_of_the_person()
    bmi=BMI(weight,height)
    if(bmi<18.5):
        display("underweight")
    elif(bmi>=18.5 and bmi<=25):
        display("normal")
    elif(bmi>25 and bmi<=30):
        display("overweight")
    else:
        display("obese")
        
main()
