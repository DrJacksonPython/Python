#ex1
for i in range(1, ): #loop over the numbers 1 to 10
                     #print each number

#ex2
for i in                :#loop over the numbers from 10 to 1
    #print each number squared

#ex3
# we're going to add up all the numbers from 1 to 100
# for each number we're going to add it to my_sum, then print it at the end

  # create a variable called my_sum and set its value to 0
for i in : # create a for loop over the numbers 1 to 100
    my_sum + i #you need to reassign the value of my_sum to my_sum + i

# print out the value of my_sum


#ex4
# add up all the square numbers from 30 to 60


#ex5
# i want the sum of all the multiples of 3 and 5 less than 1000.
# you need to remove duplicates (they will be factors of ....)

#you need 3 loops - one to add all the multiples of 3, one to add all the multiples of 5
# and one to subtract all the duplicate multiples of ....
# i've written the first loop for you

mult_sum = 0 #this variable will hold the sum
for i in range(0, 333):
    mult_sum += 3*i # x += 2 is the same as x = x + 2


#ex6 -
#remember the first element of a list called great_list is great_list[0]

my_list = ["Anisa", ] #create a list with 4 names

for i in range(0, ): #loop over all the elements of the list - use len(x) to find the length of x
     # print the name of each person in your list

#ex7 -
#remember the first element of a list called great_list is great_list[0]

my_list = ["Anisa", ] #create a list with 4 names

for i in range(0, ): #loop over all the elements of the list - use len(x) to find the length of x
     # print a message to each person in your list

#ex8 - calculate the mean of this list
x = [1, 4, 9, 16, 25, 36, 49]
# use a for loop to calculate the sum of x - call the variable x_sum

# create a variable called x_mean - it will be x_sum divided by how many values of x there are

#print x_mean

#ex9
# use a while loop to print the numbers from 1 to 10
# DO NOT RUN AN INFINITE LOOP!!!!!!!
i = 1
while i < :#fill this in to stop the loop running when i is bigger than 10
    #print the value of i
    i += #what do you need to add to i here? if this wasn't here, what would happen to the loop?

#ex10
# say something nice while someone is asking you to!
say_more_stuff = True #the user will set this to False later
user_name = input(" ") # get the name of the user
while say_more_stuff:
    #print something nice here about the user
    user_answer = input("Do you want more compliments? Yes/No ") #ask the user if they want more compliments
    if user_answer :#if the user_answer is NO, set say_more_stuff to FALSE (remember to change user_answer to UPPER CASE!)


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
    if :#if the roll is a 1, set user_play to False and print a losing message

    else:
        #add the dice roll to the users money
        user_answer = input("Do you want to keep playing? Yes/No")
        if user_answer.upper() :#if the user says NO, change user_play to false
            print("Well done! You have won {}".format(user_money)) #this will print the users money

#ex12
#copy your stuff from ex11 - add a high score
#create a high score variable









##Sxy = 0
##Sxx = 0
##Syy = 0
##
##x = [150, 162, 148, 172, 159, 179]
##y = [63.1, 67.1, 68.7, 75.4, 72.0, 71.8]
##
##if len(x) == len(y):
##    for i in range(0, len(x)):
##        Sxy += x[i] * y[i]
##        Sxx += x[i] * x[i]
##        Syy += y[i] * y[i]
##    corr = Sxy / ( (Sxx * Syy) ** 0.5)
##    print(corr); print(Sxy); print(Sxx); print(Syy)
##else:
##    print("x and y need to be the same length")
    

    
