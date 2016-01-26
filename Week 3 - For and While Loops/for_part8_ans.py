#ex8 - calculate the mean of this list
x = [1, 4, 9, 16, 25, 36, 49]
# use a for loop to calculate the sum of x - call the variable x_sum
x_sum = 0
for i in range(0, len(x)):
    x_sum += x[i]
# create a variable called x_mean - it will be x_sum divided by how many values of x there are
x_mean = x_sum / len(x)
#print x_mean
print(x_mean)
