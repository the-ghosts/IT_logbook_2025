#math_utils.py
#Simple math helper functions for reuse in other scripts.

def add_numbers(a: float, b: float) -> float:
	#Return the sum of two numbers.
	return a +b


# Quick self-test (runs only when file executed directly)
if __name__ == "__main__":
    result = add_numbers(4, 6)
    print("4 + 6 =", result)
