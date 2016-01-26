def MyIntegrand(x):
    return x**2 + 3 * x + 4

#print(Integrand(5))

def Area(Integrand, x1, x2):
    midpoint = 0.5 * (x1 + x2)
    width = x2 - x1
    return (width * Integrand(midpoint))

def RiemannSum(Integrand, a, b, numPoints):
    width = (b - a) / numPoints
    riemannSum = 0
    for i in range(0, numPoints):
        xLeft = a + i * width
        xRight = a + (i + 1) * width
        riemannSum += Area(Integrand, xLeft, xRight)
    return riemannSum

def Integration(Integrand, a, b, tol = 0.01):
    oldIntegral = 0
    newIntegral = oldIntegral + 100 * tol
    n = 1
    while abs(oldIntegral - newIntegral) > tol and n < 20:
        oldIntegral = newIntegral
        newIntegral = Integrator(Integrand, a, b, 2 ** n)
        n += 1
    print("The value of your integral is {}, completed in {} steps".format(newIntegral, n))
    return newIntegral
          
Integration(MyIntegrand, 3, 7)        
