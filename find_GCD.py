"""
The process that will be followed in this function goes as thus:

First, create a list that will store all the divisors used in the
process

Next, take all the divisors that can divide through both of the
numbers without a remainder, and store them in the list

Select the final number on the list; this number will be the GCD
"""


# create function called "euclidean_alg" without inputs

def euclidean_alg():
    
# create two input variables the user will use to input the numbers

    num_1 = input("What's the first number? ")
    num_2 = input("What's the second number? ")
    
# turn these into integers and create an error statement that will
# display if the user inputs a non-integer value

    try:
        int_num_1 = int(num_1)
        int_num_2 = int(num_2)
    except ValueError:
        print("Only integers are allowed as inputs")
    
# create empty list for storage of divisors called "divisors"

    divisors = []

# create for loop with a lower bound of 2 and an upper bound of
# the lowest of the two numbers plus one

    for i in range(1, int_num_1+1 if int_num_1 <= int_num_2 else int_num_2+1):

# if and only if the number divides both numbers with a remainder 
# of 0, add the number to the list "divisors"

        if int_num_1 % i == 0 and int_num_2 % i == 0:
            divisors.append(i)

# create a variable called GCD and set its value as the last number 
# in the "divisors" list
    
    GCD = divisors[-1]

# create a variable that will be used to print out the GCD of the 
# two numbers in an orderly manner and return the outcome of the 
# entire function as this variable

    answer = "the GCD of " + str(num_1) + " and " + str(num_2) + " is " + str(GCD)
    return answer

print(euclidean_alg())
