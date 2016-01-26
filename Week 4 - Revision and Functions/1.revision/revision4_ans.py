##this function will add up the first N natural numbers:
def sumFirstNumbers(N):
    mySum = 0#assign this a suitable value
    for i in range(1, N): #what should the values of range be
        mySum += i#finish this statement
    return mySum#what do I want to return?

sum100 = sumFirstNumbers(100) #fill in the function to add up the first 100 numbers
print(sum100)#print the value of sum100 - is it 5050 like before?

sum50 = sumFirstNumbers(50)#now create a variable sum50 - do as above and print its value
print(sum50)

#this function won't return anything - it is used to
#run the same procedure with different inputs
#however it will still print a result
def greeting():
    userName = input("What is your name? ") #get the user's name and assign it to a variable userName
    print("Hello " + userName + ", nice to meet you!")#print a message to the user with their name

greeting() # this will run the code in greeting once
         

    


