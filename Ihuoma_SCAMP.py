# This shows a function that outputs the fibonacci sequence of a given number

def fib_Recursion(n):
    if n <= 1:
        return n
    else:
        return(fib_Recursion(n-1) + fib_Recursion(n-2))
nterms = int(input("Enter number of terms: "))

# checking the validity of number of terms
if nterms <= 0:
    print("Please enter a positive integer: ")
else:
    print("Fibonacci Sequence: ")
    for i in range(nterms):
        print(fib_Recursion(i))
