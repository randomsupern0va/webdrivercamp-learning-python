#!/usr/bin/python3

def dict_update(dict_, key, value):
	if not dict_:
		print("The dictionary is empty")
	if not isinstance(key, str):
		print("The key must be a string")
	
		

	dict_[key] = value

	return dict_
			
			

if __name__=="__main__":
    dict_print = __import__('6_dict_print').dict_print
    dict_ = {"libs": (1,2,3), "x": "Selenium", "lang": ["Java"], "frame": "Behave", "set": set()}
    new_dict = dict_update(dict_, 'lang', "Python")
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)
    new_dict = dict_update(dict_, 'stars', 5)
    print(f"{'Updated Dict':.^20}")
    dict_print(new_dict)
