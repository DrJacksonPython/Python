import random

user_choice = input("Choose ROCK, PAPER or SCISSORS: ") 
user_choice =  user_choice.upper()


if user_choice == "ROCK" or user_choice == "PAPER" or user_choice == "SCISSORS":  
    print("You chose " + user_choice) 
else: 
    print("Silly - you have been given ROCK, good luck")    
    user_choice = "ROCK" 

com_ran_num = random.random() # this creates a random number between 0 and 1
com_choice = "" # create a global variable com_choice - set it to be an empty string for now. 

# you need to randomly assign the computer either ROCK, PAPER or SCISSORS
# use com_ran_num, a random number between 0 and 1, to do this
if com_ran_num < (1/3): # what condition could you use here?
    com_choice = "ROCK"
elif com_ran_num > (2 / 3): #again put a condition in here
    com_choice = "SCISSORS"               #don't forget to assign com_choice!
else:              #if com_ran_num isn't in the above two choices, what do you do?
    com_choice = "PAPER"
print("Computer chose " + com_choice)    #finally, complete this print statement to tell the user what the computer chose

if user_choice == com_choice: #check if the user's choice and computer choice are the same
     print("It's a draw!")#tell the user its a draw

#you can write this bit two different ways: we'll do it one way in this part
#and use nested if statements in the last part

if user_choice == "ROCK" and com_choice == "SCISSORS": #check if the user chooses ROCK _and_ computer chooses SCISSORS
     print("You've won, well done!") #tell the user who won
elif user_choice == "ROCK" and com_choice == "PAPER":                      #check if the user chooses ROCK _and_ computer chooses PAPER
     print("You've lost, better luck next time!")#tell the user who won

#try and write this bit without looking at what you've done - it's good practice!

#write some code that checks if the user chooses SCISSORS and computer chooses PAPER
# or user chooses SCISSORS and computer chooses ROCK
#then the correct result is printed

    #check if the user chooses ROCK _and_ computer chooses SCISSORS
    #tell the user who won
    #check if the user chooses ROCK _and_ computer chooses PAPER and tell the user who won


#run your code a few times
#choose ROCK, PAPER and SCISSORS, see what happens - is it doing what you expect?
