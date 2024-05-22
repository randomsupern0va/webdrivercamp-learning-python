#!/usr/bin/python3

def not_common_elements(a, b):
	if not a and not b:
		print("Both sets are empty")
	
	uncommon_elem = a ^ b
	return uncommon_elem

if __name__=="__main__":
    set_a = {"API", "requests", "Selenium", "Python", "Behave"}
    set_b = {"Selenium", "Java", "Cucumber", "Maven", "API"}
    elements = not_common_elements(set_a, set_b)
    [print(x) for x in sorted(list(elements))]
