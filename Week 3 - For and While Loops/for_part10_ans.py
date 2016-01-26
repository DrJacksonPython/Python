#ex10
# say something nice while someone is asking you to!
say_more_stuff = True #the user will set this to False later
user_name = input("Hello, what is your name? ") # get the name of the user
while say_more_stuff:
    print("You look smart " + user_name)#print something nice here about the user - make sure you use their name!
    user_answer = input("Do you want more compliments? Yes/No ") #ask the user if they want more compliments
    if user_answer.upper() == "NO":#if the user_answer is NO, set say_more_stuff to FALSE (remember to change user_answer to UPPER CASE!)
        say_more_stuff = False
