#ex5
# we're going to calculate the sum of all the multiples of 3 and 5 less than 1000.
# you need to remove duplicates (they will be factors of ....)

#you need 3 loops - one to add all the multiples of 3, one to add all the multiples of 5
# and one to subtract all the duplicate multiples of .... (what would they be?)
# i've written the first loop for you

mult_sum = 0 #this variable will hold the sum
for i in range(1, 334):
    mult_sum += 3 * i # x += 2 is the same as x = x + 2

#create a second loop here to add the multiples of 5 less than or equal to 1000
for i in range(1, 201):
    mult_sum += 5 * i 
#create a third loop to subtract the multiples of .... (what would they be?) less than 1000 (use -=)
for i in range(1, 67):
    mult_sum -= 15 * i 
#print the value of mult_sum

print(mult_sum)
