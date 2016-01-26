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
