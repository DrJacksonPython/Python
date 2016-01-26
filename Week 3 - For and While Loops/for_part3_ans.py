#ex3
# we're going to add up all the numbers from 1 to 100
# for each number we're going to add it to my_sum, then print it at the end

my_sum = 0# create a variable called my_sum and set its value to 0
for i in range(1, 101): # create a for loop over the numbers 1 to 100
    my_sum = my_sum + i #you need to reassign the value of my_sum to my_sum + i

# print out the value of my_sum
print(my_sum)
