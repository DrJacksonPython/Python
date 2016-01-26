#ex12
#copy your stuff from ex11 - add a high score

import random
high_score = 0 #create a high score variable called high_score - set to 0
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
            if(user_money > high_score):
                print("You've set a new high score!")
                high_score = user_money




#when the user quits, if their new score is higher than high_score
#tell them they have a new high score and update the value of high_score
