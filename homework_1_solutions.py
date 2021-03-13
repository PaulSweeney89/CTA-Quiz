# Q1 solution
# Write an algorithm that returns the largest element in an array. Assume the array is unsorted

def largest(input):
	largest = input[0]
	for i in input:
		if i>largest:
			largest = i
	
	return largest
    
print(largest([1,2,888,12,84,9]))


#Q2 Solution
#Write an algorithm that returns a new array which is the reverse of the input

def reverse(input):
    output = []
    index = len(input)-1
    while (index >= 0):
        output.append(input[index])
        index-=1
        
    return output
    
print(reverse([1,2,3,4,5]))


#Q3 Solution
#Write an algorithm that checks whether an element occurs in an array.
def included(input_list, target):
    for e in input_list:
        if e == target:
            return True
            
    return False
    
print(included([1,2,3,4,5], 3))
print(included([1,2,3,4,5], 12))

#Q4 Solution
#Write an algorithm that returns the elements on odd positions in an array.

def odd_indices(input):
    output = []
    for i in range(len(input)):
        if (i%2) != 0:
            output.append(input[i])
    return output

print(odd_indices([1,2,3,4,5]))


#Q5 Solution
#Write an algorithm that computes the running total of an array of numbers.

def sum(input):
    total = 0;
    for i in input:
        total += i
    
    return total
    
print(sum([1,2,3,4]))


#Q6 Solution
#Write an algorithm that prints a multiplication table for numbers up to 12

def table(num, upto=13):
    for i in range(1,upto):
        print(f"{num} * {i} = {num*i}")

def all_tables():
    for i in range(13):
        print(f"Table for {i}")
        print("-----------")
        table(i)
        print("-----------")
        
all_tables()

#Q7 Solution
#Write an algorithm that prints the first 100 prime numbers.

def prime(num):
    for i in range(2, int(num/2)+1):
        if (num%i) == 0:
            return False
            
    return True

def first_N_primes(n=100):
    count = 0
    num = 2
    while(count<n):
        if prime(num):
            count+=1
            print(num)
        num+=1
        
first_N_primes()


#Q8 Solution
#Write an algorithm that prints the numbers from 1 to 100 and for multiples of ’3’ print
#“Fizz” instead of the number and for the multiples of ’5’ print “Buzz”

def fizz_buzz():
    for i in range(1,101):
        if (i%3) == 0:
            print("fizz")
        elif (i%5) == 0:
            print("buzz")
        else:
            print(i)

fizz_buzz()
