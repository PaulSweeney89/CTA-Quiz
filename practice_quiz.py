# Practice Quiz

# Write a function which takes in two numbers and adds them together
def add(num1, num2):
    s = num1 + num2
    return s

# Check function
x = add(1, 2)
print(x)

# Write a function which takes in an array of numbers and returns a new array containing only the even numbers from the first array
def only_evens(arr):
    new_arr = []
    for e in arr:
        if e%2 == 0:
            new_arr.append(e)
    return(new_arr)

# Check function
y = only_evens([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(y)

#Write a function which takes in a string and replaces all occurrences of 'e' with '*' and returns the resulting string
def replace_char(string):
    new_string = ""
    for s in string:
        if s == 'e':
            new_string += '*'
        else:
            new_string += s
    return new_string

# Check function
z = replace_char("Hello World")
print(z)
