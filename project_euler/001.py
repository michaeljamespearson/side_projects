#Problem 1

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def solution(max, factors):
	multiples = []
	total = 0
	for i in range(1,max):
		for x in factors:
			if(i % x == 0 and i not in multiples):
				multiples.append(i)
	print(multiples)
	for val in multiples:
		total = total + val
	print(total)

#test cases
solution(10,[3,5]) #expect 23
solution(1000,[3,5]) #solution 233,168
