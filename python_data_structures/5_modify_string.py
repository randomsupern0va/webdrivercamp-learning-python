#!/usr/bin/python3

string = """AbraCadabra
A new string voila!"""

some_string = string.casefold()

def remove_char(some_string):
	new_string = some_string.translate({ord('a'): None})

	return new_string

print(remove_char(some_string))

