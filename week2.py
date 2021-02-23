# Week 2 
# Sum or Product

# User input interger value 
n = int(input("Please enter Number n: "))

# User select Product (p) or Sum (s)
ps = str(input("Please enter Product or Sum (p/s): "))

# If user selects Product (p)
if ps == 'p':
    x = 1													# EXAMPLE
    for value in range(1, n+1):								# n = 5, value = 1 ......value = n+1 = 6 - requires 6 iterations of loop
        x = x * value										# x = 1 * 1 * 2 * 3 * 4 * 5 = 120
    print(x)

if ps == 's':
    y = 0													# Example
    for value in range(0, n+1):								# n = 5, value = 0.......value = n+1 = 6 - requires 6 interations of loop
        y = y + value										# y = 0 + 1 + 2 + 3 + 4 + 5 = 15
    print(y)
