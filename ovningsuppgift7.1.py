from random import randint #includes the function randint from the liberary random
print("Try and guess what random number i am thinking of it is between 0 and 99")#askts the person to guess the number
number=input()#number is equal to the number the person wrote
number=int(number)#converts the value of the variable number from string to integer
randomnumber=randint(0,99)#generates a random number between 0 and 99 and stores it in the variable randomnumber
while number <= randomnumber or number >  randomnumber:#the following loop is run until the person guesses the number correctly
    if number == randomnumber:#if the persons number is the same as the randomnumber the following code is run
        print("You guessed correctly, "+ str(number) +" was my number")#prints a statement that the person guessed the number correctly
        break #ends the while loop
    elif number > randomnumber:#if the persons number is greater than the randomnumber the following code is run
        print("To HIGH guess again")#prints a statement that their number is too high and that they should choose a new number
        number=input()#saves their new number
        number=int(number)#changes their guess from string to integer
    elif number < randomnumber:#if the persons number is lower than the randomnumber the following code is run
        print("To LOW guess again")#prints a statement that their number is too low and that they should choose a new number
        number=input()#saves their new number
        number=int(number) #changes their guess from string to integer


