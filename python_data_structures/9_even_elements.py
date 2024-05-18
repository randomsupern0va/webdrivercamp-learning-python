#!/usr/bin/python3

my_list = [5, 4, 3, 2, 1]
list_ = my_list[:]
new_list = []


for i in list_:
	if i % 2 == 0:
		new_list.append(True)
	else:
		new_list.append(False)
	

new_tuple = tuple(new_list)

print(my_list)
print(new_tuple)
