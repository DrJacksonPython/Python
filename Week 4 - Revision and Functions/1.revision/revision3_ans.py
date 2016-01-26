#for myNumbers in range(1, 11):      this will print the numbers 1 to 10
#    print(myNumbers)

#
#I suggest doing these one at a time - running, check you've got it right and move on to the next one!
#


#use the above to print the numbers from 1 to 5
for i in range(1, 6):
    print(i)

#use the above to print the even numbers from 1 to 10
for i in range(1, 6):
    print(2*i)

myName = "Ziggy" #create a variable myName and assign a string with your name
#use a for loop to print each letter of your name
for i in range(0, len(myName)):
    print(myName[i])

mySum = 0
#use a for loop to add the numbers 1 to 100 to the variable mySum
#you will need the following - if x = 2 and y= 7, then x +=y will make x = 9
#it is the same as x = x + y

for i in range(1, 101):
    mySum += i
    
#print mySum - it should be 5050
print(mySum)

#do the same as above but for even numbers from 1 to 100 - what do you get now?
myEvenSum = 0
for i in range(1, 51):
    myEvenSum += (2 * i)

print(myEvenSum)



