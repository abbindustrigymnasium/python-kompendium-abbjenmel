print("What number would you like me to multiply?")#asks the person what number they want to multiply
number=input()#saves the persons answer in the variable number in the format string
number=int(number)#changes the format from string to integer
first=number#creates the variable first and sets it equal to number
while 0 <= number or 0 > number:#runs the following loop until the user tells it to stop no matter what number the user chose to multiply
    print(first)#prints the content of the variable first
    first+=number#adds the number the person chose to the variable first
    print(first)#prints the new value of the variable first
    first+=number#yet again adds the number the person chose to the variable first
    print(first)#prints the new value of the variable first
    print("Would you like me to continue multiplying your number yes/no?")#asks the user if they want the program to continue multiplying the number
    answer=input().title()#saves the string input the user gave with a capitalised first letter in the variable answer
    if answer=="No":#if the answer is no the loop breaks
        break
    else:#if the answer is not no the following code runs
        first+=number#adds the number the person chose to the variable first