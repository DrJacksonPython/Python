def MyPoly(x):#create a function MyPoly which returns the value of x^3 + 5x -3
    return x ** 3 + 5 * x - 3

def MyDiffPoly(x): #create a function MyDiffPoly which returns the value of the derivative of MyPoly
    return 3 * x **2 + 5

#create a function called NewtonRaphson which takes 4 inputs:
#1. Fn - any mathematical function which returns a value
#2. DiffFn - the derivative of Fn
#3. startValue - the initial value to start a Newton Raphson process
#4. tol - the precision of your answer, for example 0.00001

#the function will hold two values, xOld and xNew.
#it will terminate EITHER when xOld and xNew are within tol of eachother, OR there have been 20 iterations
#which suggests the function won't converge

def NewtonRaphson(Fn, DiffFn, startValue, tol):
    #create a variable called count - give it a sensible start value
    xOld = startValue - 100 * tol # why have I initialised xOld in this way?
    xNew = #what should the value of xNew be?
    while abs(xNew - xOld) > tol : #you need to check if 20 iterations have occured
        #you need to assign xOld a value - what is it?
        xNew = xNew - (Fn(xNew) / DiffFn(xNew)) # this is the Newton Raphson formula for xNew
        print("x{} = {}".format(count, xNew)) # this will print the current value of the process after N processes
        # what do you need to do to count here?
    return # what should you return?

#uncomment this to check if your function works - should get 0.5640997....
#NewtonRaphson(MyPoly, MyDiffPoly, 0.6, 0.00000001)
