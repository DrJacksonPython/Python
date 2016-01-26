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

#function 4 - variance. It will calculate the variance, which is Sxx / n
#you do this one by yourself! - use function 2 to guide you if you need help
def variance(aList):
    return Sxx(aList) / len(aList)

print(variance(testList))

timeList = [1.5, 2.6, 3.4, 5.0, 6.1, 8.2]
ageList = [5.5, 5.0, 7.7, 9.0, 10.0, 10.2]
#function 5 - Sxy. It calculates the covariance, which is Sum (x - x_mean)(y - y_mean)
def Sxy(xList, yList):
    sxy = 0
    for i in range(0, len(xList)): #write a for loop here to calculate sxy
        sxy += (xList[i] - mean(xList)) * (yList[i] - mean(yList))
    return sxy #return a value here    

print(Sxy(timeList, ageList)) # should print 25.35

#function 6 - correlation. Last one! This is pretty easy now.
#the correlation is Sxy / sqrt(Sxx * Syy) - you should get 0.919

#i'll leave this to you!
