#!/usr/bin/python3
def divide_safe(a, b):
	if not a and not b:
		return None

	try:
		result  =  a / b
	except ZeroDivisionError:
		print("Error: Division  by zero")
		return None
	except Exception as e:
		print("Error:", e)
		return None
	finally:
		print("Result:", result if 'result' in locals() else None)

	return result

if __name__ == "__main__":
    a = 9
    b = 3
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
    b = 0
    result = divide_safe(a, b)
    print(f"{a} / {b} = {result}")
