from math import sqrt

def is_prime(x):
	for i in range(2, int(sqrt(x)) + 1):
		if (x % i == 0):
			return False
	return True

def largest_prime_factor(x):
	for i in range(int(sqrt(x)), 1, -1):
		if x % i == 0:
			if(is_prime(i)):
				return i

print(largest_prime_factor(600851475143))