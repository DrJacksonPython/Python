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
    width = # what is the width of the region you are integrating over?
    riemannSum = #what should initialise your sum to be?
    for i in : #what values should your range run over?
        xLeft = #the left hand value of your partition. Draw a picture to help! split up the region [3, 5] into 8 evenly spaced points
        xRight = #the right hand value of your partition
        riemannSum += #what do you need to add to your riemannSum? You can use a function you've already built
    return riemannSum

