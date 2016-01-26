import random

#part 1
user_choice = input("Choose ROCK, PAPER or SCISSORS: ") # get input from the user
user_choice = user_choice.upper() # convert their choice to upper case text

#if they choose ROCK, PAPER or SCISSORS, tell them their choice
if user_choice == "ROCK" or user_choice == "PAPER" or user_choice == "SCISSORS": 
    print("You chose " + user_choice)
else:
    print("You have not chosen properly! You get ROCK")
    user_choice = "ROCK" # set global variable user_choice to ROCK

#part 2
com_ran_num = random.random() # create a random number between 0 and 1
com_choice = "" # create a global variable com_choice - this will be assigned to within the if statement
if com_ran_num < 0.33:
    com_choice = "ROCK"
elif com_ran_num> 0.66:
    com_choice = "SCISSORS"
else:
    com_choice = "PAPER"
print("The computer chose " + com_choice)

#part 3

#same choice will be a draw
if user_choice == com_choice:
    print("It's a draw!")

#if user chooses rock, two options left
if user_choice == "ROCK" and com_choice == "SCISSORS":
    print("user wins - ROCK beats SCISSORS!")
elif user_choice == "ROCK" and com_choice == "PAPER":
    print("user loses - PAPER beats ROCK!")

#if user chooses scissors, two options left
if user_choice == "SCISSORS" and com_choice == "ROCK":
    print("user loses - ROCK beats SCISSORS!")
elif user_choice == "SCISSORS" and com_choice == "PAPER":
    print("user wins - SCISSORS beats PAPER!")

#if user chooses paper, two options left
if user_choice == "PAPER" and com_choice == "ROCK":
    print("user wins - ROCK beats PAPER!")
elif user_choice == "PAPER" and com_choice == "SCISSORS":
    print("user loses - SCISSORS beats PAPER!")

    
