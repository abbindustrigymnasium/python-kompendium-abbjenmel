import requests#imports the liberary requests that is needed to use the api
import random#importes the liberary random that is later used to shuffle an array
url= 'https://opentdb.com/api.php?amount=10&type=multiple'#sets the variable url to the api that i used
#the following to rows getss the values from the api and saves them in the variable quanda_dictionary (questions and answers dictionary)
r = requests.get(url) 
qanda_dictionary = r.json()
correct_answers=0# creates the variable correct answers and sets it equal to zero
theanswer="1"#creates a variable that holds a string value
playersanswer="1"#creates a variable that holds a string value
whatquestion=1#creates a variable that holds an integer value
for questions in qanda_dictionary["results"]:#for every question in the dictionary the following code is run once
    print("-----------------------------------"+"\n"+ "Question nr."+ str(whatquestion)+ ":"+ "\n"+" "+questions["question"])#prints what question nuber it is and then prints the question
    whatquestion+=1#updates the integer so that it is itself plus one
    s=" , "
    answers= [questions["correct_answer"], (questions["incorrect_answers"][0]), (questions["incorrect_answers"][1]), (questions["incorrect_answers"][2])]#creates an array called answers and saves all the different answer alternatives in one spot each
    random.shuffle(answers)#shuffles the values in the array answers
    # the following rows finds what place the correct answer holds and then updates the value of theanswer to the correct answers position from 1-4
    if answers[0]== questions["correct_answer"]:
        theanswer="1"
    elif answers[1]==questions["correct_answer"]:
        theanswer="2"
    elif answers[2]==questions["correct_answer"]:
        theanswer="3"
    elif answers[3]==questions["correct_answer"]:
        theanswer="4"
    print("\n" + "   "+  "1." +answers[0]+ "\n" +"   "+  "2."+ answers[1]+ "\n" +"   "+  "3."+ answers[2]+ "\n" +"   "+  "4."+ answers[3]+ "\n"+"\n" +" "+ "Which answer do you think is correct, 1, 2, 3 or 4? "+"\n")#prints the four answers on one line each and adds the number the alternative holds in front then asks the player to enter which answer they think is correct
    playersanswer = input()#saves the players answer in the variable playersanswer
    if playersanswer== theanswer:#if the players answer is the same as the correct answers number the value of correctanswers is updated and the player gets the message that they were correct and is informed how many correct answers they have so far
        correct_answers+=1
        print("\n" + "You were right "+ questions["correct_answer"]+", was the correct answer" + " you've got "+ str(correct_answers)+ " points")
    else:#if the players answer was not correct they get the message that they were wrong and they are informed how many correct answers they have so far
        print("\n" +"You were unfortionatley wrong, "+ questions["correct_answer"]+ " was the correct answer"+ " you've still got " + str(correct_answers)+ " points")

print("\n"+ "The quiz is now over, good job, you got a total of "+str(correct_answers)+" points out of 10 possible"+"\n"+ "-----------------------------------")#after all questions have been asked and answered the player recives this message of how many right answers they got out of ten possible