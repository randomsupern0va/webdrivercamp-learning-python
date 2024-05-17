#!/usr/bin/python3
list_ = [5, 4, 3, 2, 1]
index = 1
element_to_replace = 5
old_element = list_.index(index)

for i in range(len(list_)):
	if list_[i] == old_element:
		list_[i] = element_to_replace
print(list_)

if index < 0 or index > len(list_):
	print(list_)

