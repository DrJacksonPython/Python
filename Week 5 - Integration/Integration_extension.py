#define a function called myIntegrand - it should take a single input and return the value
#of the polynomial x^2 + 3x + 4
def MyIntegrand(x):
    return x**2 + 3 * x + 4

#define a function Area to return the area of a section under your curve.
#To make things simple, we will use a rectangle.
#The width of the rectangle is the distance between the x-coordinates
#The height will be the value of your function evaluated at the mid-point of the width

# the inputs should be
# Integrand - the function to be integrated
# x1 and x2 - the two x co-ordinates
def Area(Integrand, x1, x2):
    midpoint = 0.5 * (x1 + x2)
    width = x2 - x1
    return (width * Integrand(midpoint))

#define a function RiemannSum
#it will split your integral between a and b into numPoints equally spaced points, called a partition
#it will calculate the area of the rectangle on each piece of your partition
#the areas will be added together, which is a simple version of a Riemann sum

#the inputs should be
# Integrand - the function to be integrated
# a and b - the end points of integration
# numPoints - the number of points in your partition

def RiemannSum(Integrand, a, b, numPoints):
    width = (b - a) / numPoints
    riemannSum = 0
    for i in range(0, numPoints):
        xLeft = a + i * width
        xRight = a + (i + 1) * width
        riemannSum += Area(Integrand, xLeft, xRight)
    return riemannSum

def Integration(Integrand, a, b, tol = 0.0000001):
    oldRiemannSum = 0
    newRiemannSum = oldRiemannSum + 100 * tol #why have I initialised this like this? Look at the while loop to see
    n = 1
    while abs(oldRiemannSum - newRiemannSum) > tol and n < 5000:#make this run whilst your Riemann sums are further apart than tol and n is smaller than 5000
        oldRiemannSum = newRiemannSum#what should I make oldRiemannSum?
        newRiemannSum = RiemannSum(Integrand, a, b, n)#use your RiemannSum function to evaluate a new Riemann sum
        n += 1#what MUST you do to n to stop the possibility of this being an infinite loop?!
    print("The value of your integral is {}, completed in {} steps".format(newRiemannSum, n))
    return newRiemannSum

#finally test your code! run it on your function MyIntegrand between 3 and 7 - you should get 181.33...

Integration(MyIntegrand, 3, 7)

####
#There are lots of improvements you can make to this code
# 1) In your while loop in Integration, you iterate n by 1 each time
# This is really inefficient, can you suggest a better way of iterating n? You'll need to update your conditions accordingly
# 2) How else could you calculate the area of the function under the curve? Try out something else!
# 3) Google the probability density function of the standard normal distribution N(0, 1).
# Make an integrand function for this and integrate between x = 0 and x = 2. What do you get?
