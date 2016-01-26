#ex11
# we're going to make a game of snake eyes
# each turn, the user a dice
# if they roll a 1, they lose all their money and the game is over
# if they roll a 2 - 6, then they earn their dice roll
# they can choose to quit and take their money after a roll

import random
user_money = 100 #give the user £100 to start with
user_play = True # this variable will control whether the game keeps running
while user_play:
    die1 = random.randint(1,6) #generates a random dice roll from 1 to 6
    print("You rolled a {}".format(die1)) #prints the score on the die
    if die1 == 1:#if the roll is a 1, set user_play to False and print a losing message
        user_play = False
        print("You lose!")
    else:
        user_money += die1 #add the dice roll to the users money
        print("You have £{}".format(user_money)) #prints how much money the user currently has
        user_answer = input("Do you want to keep playing? Yes/No ") #asks the user if they want to keep playing
        if user_answer.upper() == "NO":#if the user says NO, set user_play to false
            user_play = False #set user_play to False here
            print("Well done! You have won £{}".format(user_money)) #this will print the users money
            
