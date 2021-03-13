# Recursive Algorithms - Lecture 06
# Computing the greatest common divisor - Euclid Algorithm

# Iterative Implementation
def euclid(a, b):
	while b != 0:
		temp = b
		b  = a % b
		a = temp
	return a

print(euclid(35, 49))

# Recursive Implementation
def euclid_rec(a, b):
	if b ==0:
		return a
	else:
		return(euclid(b, a%b))

print(euclid_rec(35, 49))
