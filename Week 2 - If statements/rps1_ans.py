#part 1
user_choice = input("Choose ROCK, PAPER or SCISSORS: ") # get input from the user
user_choice =  user_choice.upper()# convert their choice to upper case text


if user_choice == "ROCK" or user_choice == "PAPER" or user_choice == "SCISSORS":   #if they choose ROCK OR PAPER OR SCISSORS, tell them their choice
    print("You chose " + user_choice) # you need to add something in here to tell them their choice
else: # otherwise, tell them they are silly and set their choice to rock
    print("Silly - you have been given ROCK, good luck")#print something here    
    user_choice = "ROCK" # set global variable user_choice to ROCK


#test your code works - run the code 4 times, choosing ROCK, PAPER, SCISSORS and then something else.
#check the code does what you would expect
    
