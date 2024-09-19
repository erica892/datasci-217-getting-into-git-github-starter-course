# Find the sum of all the multiples of 3 or 5 below 1000.

# first initialize a variable for a running sum
multiple_sum = 0
# next create a for loop to identify numbers that are multiples of 3 or 5 between 0 and 999
# and add them to the running sum
for i in range(1000):
   if i % 3 == 0 or i % 5 == 0:
       multiple_sum = multiple_sum + i
# finally, print the sum
print(multiple_sum)