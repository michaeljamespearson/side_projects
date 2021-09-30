# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# 600851475143 = 71 * 839 * 1471 * 6857

import math
def solution(value):
	prime_factors = []
	curr_val = value

	while(curr_val not in prime_factors):
		for x in range(2,int(math.sqrt(curr_val))+1):
			if (curr_val % x == 0):
				print(x, " is a factor")
				print("curr val is ", curr_val)
				if(x not in prime_factors):
					prime_factors.append(x)
				curr_val = curr_val / x
				break
		if(curr_val == 1):
			break

	return max(prime_factors)
