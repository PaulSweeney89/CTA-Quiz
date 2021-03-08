# Recursive Algorithms - Lecture 06
# Computing the nth Fibonacci Number

# Iterative Implementation
def fib(n):
	i, n1, n2 = 1, 0, 1
	while i < n:
		temp = n1
		n1 = n2
		n2 = n1 + temp
		i += 1

	return n1

l1 = []
for i in range(0,6):
	x = fib(i)
	l1.append(x)
print("fib: ",l1)

# Recursive Implementation
def fib_rec(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	return fib(n-1) + fib(n-2)

l2 = []
for i in range(0,6):
	x = fib_rec(i)
	l2.append(x)
print("fib_rec: ",l2)

# https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/
def Fibonacci(n):
   
    # Check if input is 0 then it will
    # print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # Check if n is 0
    # then it will return 0
    elif n == 0:
        return 0
 
    # Check if n is 1,2
    # it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

l3 = []
for i in range(0,6):
	x = Fibonacci(i)
	l3.append(x)
print("Fibonacci: ", l3)


