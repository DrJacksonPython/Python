my_list = ["Anisa", "Sarah", "Nick", "Molly"]
for i in range(0, len(my_list)):
    print("Hello " + my_list[i] + "!")


for i in range(1, 10):
    print(i)

sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)


Sxy = 0
Sxx = 0
Syy = 0

x = [150, 162, 148, 172, 159, 179]
y = [63.1, 67.1, 68.7, 75.4, 72.0, 71.8]

if len(x) == len(y):
    for i in range(0, len(x)):
        Sxy += x[i] * y[i]
        Sxx += x[i] * x[i]
        Syy += y[i] * y[i]
    corr = Sxy / ( (Sxx * Syy) ** 0.5)
    print(corr); print(Sxy); print(Sxx); print(Syy)
else:
    print("x and y need to be the same length")
    

    
