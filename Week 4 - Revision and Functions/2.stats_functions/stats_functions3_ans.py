## we are going to combine a series of functions to make a useful stats calculator, just like your casio calculators

# the beauty of using functions is we can REUSE code - we don't have to keep writing code to do the same thing over and over!

#function 1 - sumList. It will add up all the values in a list
def sumList(aList):#create a function caled sumList - the parameter will be a list, give it a sensible name
    mySum = 0#set mySum to something sensible
    for i in range(0, len(aList)):      #use a for loop here to add all the values to mySum - use len( ) to get the length of your list
        mySum += aList[i]#put some code here to add to your mySum variable
    return mySum# what should you return?

testList = [4, 7, 15, 28, 46]
print(sumList(testList))    #run your function sumList with the list testList - it should return 100


#function 2 - mean. It will return the mean of a list
def mean(aList):#create a function called mean - the parameter will be a list, give it a sensible name
    return (sumList(aList) / len(aList))#use your function sumList to return the mean - you'll need len() for the length of the list

print(mean(testList))#print your function mean applied to testList - you should get 20

#function 3 - Sxx. It will calculate Sxx, Sum(x - mean)^2
def Sxx(aList):#create a function called Sxx  - the parameter will be aList
    sxx = 0
    for i in range(0, len(aList)):#finish the for loop
        sxx += ((aList[i] - mean(aList)) ** 2) # increment sxx by this value
    return sxx#what do you need to return

print(Sxx(testList))

