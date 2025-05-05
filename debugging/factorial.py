#!/usr/bin/python3
import sys

def factorial(n):
    """Calculate factorial of a non-negative integer."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            print("Usage: ./factorial.py <number>")
            sys.exit(1)
        
        n = int(sys.argv[1])
        f = factorial(n)
        print(f)
    except ValueError as e:
        if "Factorial not defined" in str(e):
            print(e)
        else:
            print("Error: Please provide a valid integer")
        sys.exit(1)
    