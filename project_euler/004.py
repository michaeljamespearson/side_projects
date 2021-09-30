def solution():
	palindromes = []
	for i in range(100,1000):
		for j in range(100,1000):
			val = i * j
			if (is_palindrome(val)):
				palindromes.append(val)
				
	highest = max(palindromes)
	print(highest)
	return highest	


def is_palindrome(number):
	num_string = str(number)
	for x in range(len(num_string)):
		if (num_string[x] != num_string[len(num_string)-x-1]):
			return False
	print("Value: ", num_string, " is a palindrome")
	return True	
