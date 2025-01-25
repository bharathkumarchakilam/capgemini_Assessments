#display the count of the each word
def display(result):
    print(result)

#input by the user 
def get_input():
    word=input("enter the input: ")
    return word

#counting each word in the input
def word_counter(word):
    word_list=word.split()
    word_count={}
    for i in word_list:
        if i in word_count:
            word_count[i]+=1
        else:
            word_count[i]=1
    return word_count

#main function
def main():
    word=get_input()
    result=word_counter(word)
    display(result)
    
main()