#Displaying the number of vowels, consonants, digits, special characters and reverse of the string
def display(vowels,consonants,digits,special_characters,reverse):
    print("Vowels:",vowels)
    print("Consonants:",consonants)
    print("Digits:",digits)
    print("Special Characters:",special_characters)
    print("Reverse:",reverse)

#input by the user
def get_input():
    string=input("Enter the string: ")
    return string

#checking the number of vowels, consonants, digits, special characters and reverse of the string
def string_analysis(string):
    vowels=0
    consonants=0
    digits=0
    special_characters=0
    reverse=string[::-1]
    for i in string:
        if i.isalpha():
            if i in ['a','e','i','o','u','A','E','I','O','U']:
                vowels+=1
            else:
                consonants+=1
        elif i.isdigit():
            digits+=1
        else:
            special_characters+=1
    return vowels,consonants,digits,special_characters,reverse

#main function  
def main():
    string=get_input()
    vowels,consonants,digits,special_characters,reverse=string_analysis(string)
    display(vowels,consonants,digits,special_characters,reverse)
    
main()