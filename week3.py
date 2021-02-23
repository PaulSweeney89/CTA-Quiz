# Problem 1 - Find largest value in Array

arr = [1, 5, 15, 23, 6, 90, 89]

# set m = first value in array
m = arr[0]

for val in arr:

# compare each m against values in array 
# set m to the larger value
	if val > m:
		m = val

print(m)



# Problem 2 - Return a new array which is the reverse of the input array

arr = ['h', 'E', 'L', 'l', 'O']
new_arr = []

l = len(arr)
start_index = 0
end_index = l -1

while end_index >= 0:

	print("start index", start_index)
	print("end index", end_index)

	new_arr.append(arr[end_index])

	start_index = start_index + 1
	end_index = end_index - 1

print(new_arr)



# Problem 3 - Checks whether an element occurs in an array

arr = [1, 6, 7, 9, 20, 3]

# is 3 in the array?
target = 3

for ele in arr:
	if target == ele:
		print("Target ", target, "is in the array!")



# Problem 4 - returns the elements on odd positions in an array

arr = ["H", "E", "L", "L", "0"]

new_arr = []

for i in range(0, len(arr)):
	if i % 2 > 0:
		new_arr.append(arr[i])

print(new_arr)



# problem 5 - computes the running total of an array of numbers

arr = [1, 2, 3, 4, 5]

x = 0

for ele in arr:
	x = x + ele

print(x)



# problem 6 - prints a multiplication table for numbers up to 12

x = int(input("please enter a value:"))

for i in range(0, 13):

	y = x * i
	print(x, "x", i, "=", y)



# problem 7 -  prints the first 100 prime numbers

prime = []

for i in range(0, 250):
	if i % 2 > 0 and len(prime) <100:
		prime.append(i)

print(prime)
print("Are the first", len(prime), "prime numbers")



# problem 8 - s the numbers from 1 to 100 and for multiples of ’3’ print
# “Fizz” instead of the number and for the multiples of ’5’ print “Buzz”

for i in range(1, 101):
	
	if i % 3 == 0 and i % 5 == 0:
		print("FIZZ / BUZZ")
	elif i % 3 == 0:
		print("FIZZ")
	elif i % 5 == 0:
		print("BUZZ")
	else:
		print(i)