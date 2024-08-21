
# Function definition
def factorial(n):
    if(n==0 or n==1):
        return 1
    

    return n * factorial(n-1)








# Driver code
n = 5

# Getting Result
result = factorial(n)

# print result
print("THe factorial of the number " + str(n) + " is " + str(result) )