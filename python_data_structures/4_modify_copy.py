#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
old_element = list_.index(index)
new_list = list_[:]

for i in range(len(new_list)):
	if new_list[i] == old_element:
		new_list[i] = element_to_replace

print(new_list)
print(list_)

if index < 0 or index > len(new_list):
	print(new_list)

