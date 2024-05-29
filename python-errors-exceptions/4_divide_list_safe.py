#!/usr/bin/python3
def divide_list_safe(list_1, list_2, list_len):
	if not list_1 and not list_2:
		return None

	new_list = []
	for i in range(list_len):
		try:
			result = list_1[i] / list_2[i]

		except ZeroDivisionError:
			print("Error: Division by zero")
			result = 0
		except TypeError:
			print("Error: Wrong type")
			result = 0
		except IndexError:
			print("Error: Index is out of range")
			result = 0
		finally:
			new_list.append(result)

	return new_list
if __name__ == "__main__":
    list_1 = [9, 2, 6]
    list_2 = [3, 2, 2]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
    print(10*"_")
    print()
    list_1 = [9, 2, 6, 10]
    list_2 = ["one", 0, 1, 2, 7]
    res = divide_list_safe(list_1, list_2, max(len(list_1), len(list_2)))
    print(res)
