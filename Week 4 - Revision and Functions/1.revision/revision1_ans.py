x = 6 # assign the variable x the value 6
y = x #create a variable y. set its value to x

if x == y   : #check IF x and y are equal.
    print("x and y are equal") #finish this
else:
    print("x and y are not equal")  #print something here

y = 4    #now set y = 4
z = x + y   #create a new variable z - set its value to x + y

#use if, elif and else to check if x equals y or x equals z
#print a statement in each case
if x == y:
    print("x and y are equal")
elif x == z:
    print("x and z are equal")
else:
    print("this is a mess")

