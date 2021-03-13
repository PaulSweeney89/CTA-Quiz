# 1. Write an algorithm that returns the reverse of a given string.

def reverse(s):
	if s == "" or len(s) == 1:
		return s
	else: 
		# print(s[1:] + s[0])
		return reverse(s[1:]) + s[0]

print(reverse("HELLO"))

# 2. Write an algorithm that reverses an array in-place (i.e changes what is stored at each
# index), assume the input array contains numbers.

def rev_arr(a):
	if len(a) == 0:
		return a
	else:
		return a[::-1]

print(rev_arr([1, 2, 3, 4, 5]))
	
# 3. Write an algorithm that checks whether an element occurs in an array, assume unsorted.

def search(arr, target, index):
	if arr[index] == target:
		return True
	elif index == 0:
		return False
	else:
		return search(arr, target, index -1)

print(search([1, 7, 3, 10], 10, 3))

# 4. Write an algorithm that computes the sum of an array of numbers.

def add_arr(a):
	if len(a) == 1:
		return a[0]
	else:
		return a[0] + add_arr(a[1:])

print(add_arr([1, 2, 3, 4]))
	
# 5. Write an algorithm to produce calculate the Nth number in the Fibonacci sequence.
# Assume the sequence begins 0,1,1,2....

def fib(n):
	if n == 1:
		return 0
	elif n == 2:
		return 1
	return fib(n-1) + fib(n-2)

print(fib(6))


# 6. Write a recursive function that checks whether a string is a palindrome (a palindrome
# is a string that’s the same when reads forwards and backwards.)

def is_palindrome(str):
	if len(str) < 2:
		return True
	else:
		return str[0] == str[-1] and is_palindrome(str[1:-1])

print(is_palindrome("racecar"))
print(is_palindrome("FML"))

# 7. Given a number and a power, compute the result of the number raised to that power.
# For example 2^3 = 8.

# https://www.geeksforgeeks.org/python-program-to-find-the-power-of-a-number-using-recursion/

def power(n, p):
	if (p==0 or p==1):
		return n
	else:
		return n*power(n, p-1)

print(power(2, 3))

# 8. Given a string and a substring, compute how many times that substring appears in
# the string. For example “he” appears twice in the string “her and herself”.

# https://nicodem.tech/check-substring-in-a-string-using-recursion/

def string_search(sub,str):

  if len(sub)==0:
    return True

  if len(str)==0 and len(sub)>0:
    return False

  if sub[0]==str[0]:
    return string_search(sub[1:],str[1:])
  else:
    return string_search(sub,str[1:])

print(string_search("hell", "hello"))