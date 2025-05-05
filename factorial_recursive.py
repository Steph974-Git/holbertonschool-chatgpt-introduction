#!/usr/bin/python3
import sys

def factorial(n):
	"""
	Calculate the factorial of a non-negative integer recursively.
	
	Parameters:
		n (int): A non-negative integer for which to calculate the factorial.
				 Factorial of n is the product of all positive integers less than
				 or equal to n.
	
	Returns:
		int: The factorial of n (n!).
		
	Raises:
		ValueError: If n is negative.
	"""
	if n < 0:
		raise ValueError("Factorial is not defined for negative numbers")
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)

if __name__ == "__main__":
	try:
		if len(sys.argv) < 2:
			print("Usage: ./factorial_recursive.py <number>")
			sys.exit(1)
		
		n = int(sys.argv[1])
		f = factorial(n)
		print(f)
	except ValueError as e:
		if "Factorial is not defined" in str(e):
			print(e)
		else:
			print(f"Error: Please provide a valid integer")
		sys.exit(1)
