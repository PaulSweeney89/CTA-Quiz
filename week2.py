# Product or Sum

n = int(input("Please enter Number n: "))
ps = str(input("Please enter Product or Sum (p/s): "))

if ps == 'p':
    x = 1
    for value in range(1, n+1):
        x = x * value
    print(x)

if ps == 's':
    y = 0
    for value in range(0, n+1):
        y = y + value
    print(y)

if ps != 'p' or 'P' or 's' or 'S':
    print("Please enter product or sum (p/s)")