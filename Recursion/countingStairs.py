# Helper method
def helper(n):
    if(n <= 1):
        return n
 
    return helper(n-1) + helper(n-2)
    

# function definition
def countNumberOfWays(s):
    return helper(s+1)











# driver code
n = 100000

# result
result = countNumberOfWays(n)

# print the result
print("The number of ways of climbing stairs are ", result)

# Doesnt work in case of large inputs
