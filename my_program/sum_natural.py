# Using for loop
number = int(input("Please enter a any number: "))
total = 0

for value in range(1, number + 1):
    total = total + value
print("The sum of natural numbers from 1 to {0} = {1}".format(number, total))

# Using a recursion loop
def sum_of_n_natural_numbers(num):
    if(num == 0):
     return num
    else:
     return (num + sum_of_n_natural_numbers(num -1))
 
number = int(input("Please enter a any number: "))
total_number = sum_of_n_natural_numbers(number)
print("The sum of natural numbers from 1 to {0} = {1}".format(number, total_number))

# Using while loop
number = int(input("Please enter a any number: "))
total = 0
value = 1

while (total <= value):
    total = total + value 
    value = value + 1
    print("The sum of natural numbers from 1 to {0} = {1}".format(number, total))