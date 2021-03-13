# Recursive Algorithms - Lecture 06
# Computing a factorial

# Iterative Implementation
def factorial(n):
	answer = 1
	while n > 1:
		answer *= n
		n -= 1
	return answer

print(factorial(5)) 

# Recursive Implementation
def factorial_rec(n):
	if n <= 1:
		return 1
	else:
		return n*factorial_rec(n-1)

print(factorial(5))