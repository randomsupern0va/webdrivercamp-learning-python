#!/usr/bin/python3

def keys_number(d):
	if len(d) == 0:
		print("The dictionary is empty")
	
	keys_num =  len(d)
	return keys_num

    # YOUR CODE HERE
if __name__=="__main__":
    dict_ = {"lib": "requests", 1: "Selenium", "lang": "Python", "frame": "Behave"}
    number_of_keys = keys_number(dict_)
    print(f"The dictionary has {number_of_keys} keys")
