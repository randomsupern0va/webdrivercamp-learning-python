#!/usr/bin/python3

def common_elements(a, b):
	if not a and not b:
		print("Both sets are empty")
	
	common_el = a & b
	return common_el
  

if __name__=="__main__":
    set_a = { "API", "requests", "Selenium", "Python", "Behave"}
    set_b = { "Selenium", "Java", "Cucumber", "Maven", "API"}
    same_element = common_elements(set_a, set_b)
    [print(x) for x in sorted(list(same_element))]
