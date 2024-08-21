# Function definition
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)








# Driver code
n = 10

for i in range(n):
    # function calling
    print(fib(i))